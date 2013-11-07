'''
Created on 11.09.2013

@author: hannes
'''
from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM, SO_REUSEADDR, SOL_SOCKET

from select import select
from thread import start_new_thread
from copy import copy

from mrNetworkListener import mrNetworkListener

class mrSocketManager(mrNetworkListener):
    '''
    Class for managing a socket connection
    '''
    
    __host = "127.0.0.1"
    __port = 9090
    __connectedClients = []
    __socket = socket()
    __stopSocket = False
    __dataBuffer = []
    __connected = False
    __server = False
    __onClientAddedList = []
    __onDataRecievedList = []
    __udpOn = False
    
    __recieveBufferSize = 4096
    

    def __init__(self, host="127.0.0.1", port=9090, server=False, udpOn=False):
        '''
        Constructor
        @param host: Hostname or IP to create socket for. If omitted localhost is taken.
        @param port: Port number to use for socket connection. Default is 9090.
        @param server: Set True to start a server, if False or omitted a client socket is initiated.
        @param udpOn: If True udp socket is created
        '''
        super(mrSocketManager, self).__init__()
        
        self.__host = host
        self.__port = port
        self.__server = server
        self.__socket = None
        self.__dataBuffer = []
        self.__connected = False
        self.__onClientAddedList = []
        self.__onDataRecievedList = []
        self.__connectedClients = []
        self.__udpOn = udpOn
        
        if server:
            start_new_thread( self.__startServerSocket, () )
        else:
            start_new_thread( self.__startClientSocket, () )
        
    def __startServerSocket(self):
        '''
        Starts server socket
        '''
        # initiate socket
        self.__stopSocket = False
        if not self.__udpOn:
            # TCP socket
            self.__socket = socket( AF_INET, SOCK_STREAM )            
        else:
            # UDP socket
            self.__socket = socket( AF_INET, SOCK_DGRAM )
            
        self.__socket.setsockopt( SOL_SOCKET, SO_REUSEADDR, 1 )
            
            
        try:
            self.__socket.bind( (self.__host, self.__port) )
            
            if not self.__udpOn:
                self.__socket.listen(1)
                              
            self.__connected = True            
        except:
            return
        
        self.__connectedClients.append( self.__socket )
        
        sock = socket()
        while not self.__stopSocket:
            # get list of sockets
            if not self.__udpOn:
                read_sockets = select( self.__connectedClients, [], [] )
                read_sockets = read_sockets[0]
            else:
                read_sockets = self.__connectedClients
            
            # check all read ready sockets
            for sock in read_sockets:
                
                if sock == self.__socket and not self.__udpOn:
                    # new connection
                    sockdata = self.__socket.accept()
                    self.__connectedClients.append( sockdata[0] )
                    self._processOnClientAddedListener(sockdata)
                    
                else:
                    # recieved data
                    try:
                        # read data and append to data buffer
                        if not self.__udpOn:
                            data, addr = sock.recvfrom( self.__recieveBufferSize )
                        else:
                            data, addr = self.__socket.recvfrom( self.__recieveBufferSize )
                            
                        # spread data                 
                        if data:
                            # add remote side to connected clients
                            if self.__udpOn and addr not in self.__connectedClients:
                                self.__connectedClients.append(addr)
                             
                            self._processOnDataRecievedListener( data )
                            
                    except:
                        # socket offline
                        sock.close()
                        self.__connectedClients.remove(sock)
                        continue
        
        # close socket
        self.__connected = False
        self.__socket.close()
        
    
    def __startClientSocket(self):
        '''
        Starts client socket
        '''
        # initiate socket
        if not self.__udpOn:
            # TCP SOCKET
            self.__socket = socket(AF_INET, SOCK_STREAM)
        else:
            # UDP Socket
            self.__socket = socket(AF_INET, SOCK_DGRAM)
            
        try:
            self.__socket.connect( (self.__host, self.__port) )
            self.__connected = True
        except:
            return
        
        while not self.__stopSocket:
            # read data and append to data buffer
            try:
                data = self.__socket.recv( self.__recieveBufferSize )
                if data:
                    self._processOnDataRecievedListener( data )
            except:
                pass
            
        # close socket
        self.__connected = False
        self.__socket.close()
        
    def __addDatapackage(self, datapackage=None):
        '''
        Adds a data package to data buffer
        '''
        try:
            self.__dataBuffer.append( copy(datapackage) )
        except:
            pass
    
    def stopSocket(self):
        '''
        Stops the socket
        '''
        self.__stopSocket = True
        self.__socket.close()
        self.__connected = False
    
    def getDataBuffer(self):
        '''
        Returns the data package buffer
        '''
        return self.__dataBuffer
    
    def getFirstData(self):
        '''
        Returns first data in data buffer
        '''
        #print "data buffer", self.__dataBuffer.__repr__()
        if len(self.__dataBuffer) > 0:
            data = self.__dataBuffer[0]
            self.__dataBuffer.remove(data)
            return data
        return None
    
    def hasNextData(self):
        '''
        Returns True if data buffer has more items
        '''
        if len(self.__dataBuffer) > 0:
            return True
        return False
    
    def __send(self, data):
        '''
        Sends string  with socket
        '''
        if not self.__server:
            # send data as client
            self.__socket.send( data )
        else:
            # send data as server
            sock = socket()        
            for sock in self.__connectedClients:
                # TCP socket
                if sock != self.__socket:
                    if not self.__udpOn:
                        sock.send(data)
                    else:
                        self.__socket.sendto(data, sock)
    
    def sendData(self, datapackage):
        '''
        Sends a data package object
        '''   
        if self.__connected:
            self.__send( datapackage )

            
    def pushRecvData(self, dataPackage):
        '''
        Pushed data package into recieve buffer
        '''
        self.__addDatapackage( dataPackage )
        self._processOnDataRecievedListener( dataPackage )
            
    def isConnected(self):
        '''
        Returns True if socket is connected
        '''
        return self.__connected
    
    def countClients(self):
        '''
        Returns number of connected clients
        '''
        return len(self.__connectedClients)
    
    def getSocketAddress(self):
        '''
        Returns socket address
        '''
        if self.__socket != None:
            return self.__socket.getsockname()
        return None