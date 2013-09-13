'''
Created on 11.09.2013

@author: hannes
'''
import socket
from select import select
from thread import start_new_thread
from src.mrLib.networking.mrProtocol import mrProtocolData
from mrProtocol import PROTOCOL_ENCODING, createFromDataPackage
import DataPackage

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
    __onClientAdded = []
    __onDataRecieved = []
    
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
        self.__socket = None
        self.__dataBuffer = []
        self.__connected = False
        self.__onClientAdded = []
        self.__onDataRecieved = []
        
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
        try:
            self.__socket.bind( (self.__host, self.__port) )
            self.__socket.listen(1)
            self.__connected = True
        except:
            return
        
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
                    self.__onClientAddedListener(sockdata)
                    
                else:
                    # recieved data
                    try:
                        # read data and append to data buffer
                        data = sock.recv( self.__recieveBufferSize )
                        if data:
                            datapackage = DataPackage.CreateFromDocument(data)
                            self.__addDatapackage( datapackage )
                            self.__onDataRecievedListener(datapackage)
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
        try:
            self.__socket.connect( (self.__host, self.__port) )
            self.__connected = True
        except:
            return
        
        while not self.__stopSocket:
            # read data and append to data buffer
            data = self.__socket.recv( self.__recieveBufferSize )
            if data:
                datapackage = DataPackage.CreateFromDocument(data)
                self.__addDatapackage( datapackage )
                self.__onDataRecievedListener(datapackage)
            
        # close socket
        self.__connected = False
        self.__socket.close()
        
    def __addDatapackage(self, datapackage=None):
        '''
        Adds a data package to data buffer
        '''
        try:
            protocoldata = createFromDataPackage(datapackage)
            if protocoldata:
                self.__dataBuffer.append( protocoldata )
        except:
            pass
        
    def __onClientAddedListener(self, clientData):
        '''
        Function to handle onClientAddedListener
        '''
        for listener in self.__onClientAdded:
            listener(clientData)
            
    def __onDataRecievedListener(self, datapackage):
        '''
        Function to handle onDataRecievedListener
        '''
        for listener in self.__onDataRecieved:
            listener(self, datapackage)
            
    def addOnClientAddedListener(self, listener):
        '''
        Sets onClientAdded listener
        @param listener: Listener function.
        Arguments of listener function is a tuple of
        socket and client address data (sock, (host, port)).
        '''
        if listener not in self.__onClientAdded:
            self.__onClientAdded.append( listener )
        
    def addOnDataRecievedListener(self, listener):
        '''
        Sets onDataRecieved listener
        @param listener: Listener function
        Argument of listener function is the mrSocketManager
        that recieved new data and the datapackage.
        '''
        if listener not in self.__onDataRecieved:
            self.__onDataRecieved.append( listener )
        
    def removeOnClientAddedListener(self, listener ):
        '''
        Removes onClientAdded listener
        '''
        self.__onClientAdded.remove( listener )
        
    def removeOnDataRecievedListener(self, listener):
        '''
        Removes onDataRecieved listener
        @param listener: Listener to remove
        '''
        self.__onDataRecieved.remove( listener )
    
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
        if self.__connected and type(datapackage) == mrProtocolData:
            self.__send( datapackage.toDataPackage().toxml(encoding=PROTOCOL_ENCODING) )
            
    def pushRecvData(self, dataPackage):
        '''
        Pushed data package into recieve buffer
        '''
        self.__addDatapackage( dataPackage )
        self.__onDataRecievedListener( dataPackage )
            
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