'''
Created on 11.09.2013

@author: hannes
'''
import socket
from select import select
from thread import start_new_thread

class mrSocketManager(object):
    '''
    Class for managing a socket connection
    '''
    
    __host = "127.0.0.1"
    __port = 9090
    __connectedClients = []
    __socket = socket.socket()
    __stopSocket = False
    __dataBuffer = []
    __connected = False
    __server = False
    
    __recieveBufferSize = 4096
    

    def __init__(self, host="127.0.0.1", port=9090, server=False):
        '''
        Constructor
        @param host: Hostname or IP to create socket for. If omitted localhost is taken.
        @param port: Port number to use for socket connection. Default is 9090.
        @param server: Set True to start a server, if False or omitted a client socket is initiated.
        '''
        self.__host = host
        self.__port = port
        self.__server = server
        
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
        self.__socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__socket.bind( (self.__host, self.__port) )
        self.__socket.listen(1)
        self.__connected = True
        
        self.__connectedClients.append( self.__socket )
        sock = socket.socket()
        
        while not self.__stopSocket:
            # get list of sockets
            read_sockets = select( self.__connectedClients, [], [] )
            read_sockets = read_sockets[0]
            
            # check al read ready sockets
            for sock in read_sockets:
                
                if sock == self.__socket:
                    # new connection
                    sockdata = self.__socket.accept()
                    self.__connectedClients.append( sockdata[0] )
                    
                else:
                    # recieved data
                    try:
                        # read data and append to data buffer
                        data = sock.recv( self.__recieveBufferSize )
                        if data:
                            self.__dataBuffer.append( data )
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
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.connect( (self.__host, self.__port) )
        self.__connected = True
        
        while not self.__stopSocket:
            # read data and append to data buffer
            data = self.__socket.recv( self.__recieveBufferSize )
            if data:
                self.__dataBuffer.append( data )
            
        # close socket
        print "client offline"
        self.__connected = False
        self.__socket.close()
            
    
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
        tmpDataBuffer = self.__dataBuffer
        self.__dataBuffer = []
        return tmpDataBuffer
    
    def __send(self, data):
        '''
        Sends xml string  with socket
        '''
        if not self.__server:
            # send data as client
            self.__socket.send( data )
            
        else:
            # send data as server
            sock = socket.socket()
            for sock in self.__connectedClients:
                if sock != self.__socket:
                    sock.send(data)
    
    def sendData(self, datapackage):
        '''
        Sends a data package object
        '''   
        if self.__connected:
            self.__send( datapackage.toxml() )
            
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