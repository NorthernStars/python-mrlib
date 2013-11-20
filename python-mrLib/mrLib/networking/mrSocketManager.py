'''
Created on 11.09.2013

@author: hannes
'''
from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM, SO_REUSEADDR, SOL_SOCKET

from select import select
from thread import start_new_thread

from mrNetworkListener import mrNetworkListener
from mrLib.networking.data.networkhandshake import connectionRequest, connectionEstablished, connectionAcknowlege, CreateFromDocument

class mrSocketManager(mrNetworkListener):
    '''
    Class for managing a socket connection
    '''
    
    __host = "127.0.0.1"
    __port = 9090
    __connectedClients = []
    __pendingClients = []
    __socket = socket()
    __stopSocket = False
    __connected = False
    __server = False
    __onClientAddedList = []
    __onDataRecievedList = []
    __udpOn = False
    __name = "client"
    __serverName = None
    __useHandshake = True
    __overwriteNewClients = False
    
    __recieveBufferSize = 16384
    

    def __init__(self, host="127.0.0.1", port=9090, server=False, udpOn=False, name="client", useHandshake=True, overwriteNewClients=False):
        '''
        Constructor
        @param host: Hostname or IP to create socket for. If omitted localhost is taken.
        @param port: Port number to use for socket connection. Default is 9090.
        @param server: Set True to start a server, if False or omitted a client socket is initiated.
        @param udpOn: If True udp socket is created
        @param name: Name of client/server for UDP handshake
        @param useHandshake: If true and udoOn is True, UDP handshake is used for connection
        @param overwriteNewClients: If True new connections overwriteing connections
        '''
        super(mrSocketManager, self).__init__()
        
        self.__host = host
        self.__port = port
        self.__server = server
        self.__socket = None
        self.__connected = False
        self.__onClientAddedList = []
        self.__pendingClients = []
        self.__onDataRecievedList = []
        self.__connectedClients = []
        self.__udpOn = udpOn
        self.__name = name
        self.__serverName = None
        self.__useHandshake = useHandshake
        self.__overwriteNewClients = False
        
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
            print "error on binding server to " + str(self.__host) + ":" + str(self.__port)
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
                        data, addr = self.__recvData(sock)
                        
                        # check for connection handshake
                        handshake = False
                        if self.__udpOn and self.__useHandshake:
                            handshake = self.__handshakeServer(data, addr)                            
                            
                        # spread data               
                        if not handshake and data:
                            # add remote side to connected clients
                            if not self.__udpOn and addr != None and addr not in self.__connectedClients:
                                self.__connectedClients.append(addr)
                             
                            # call listener
                            if not self.__udpOn or self.__isClientInList(self.__getClientName(addr)[0], addr):
                                self._processOnDataRecievedListener( addr, data )
                            
                    except:
                        # socket offline
                        if not self.__udpOn:
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
        except:
            return
        
        # check for handshake (UDP only)
        if self.__useHandshake and self.__udpOn:
            self.__handshakeClient()
        else:
            self.__connected = True
        
        while not self.__stopSocket:
            # read data and append to data buffer
            data, addr = self.__recvData()
            if data:
                self._processOnDataRecievedListener( addr, data )
            
        # close socket
        self.__connected = False
        self.__socket.close()
        
    def __handshakeClient(self):
        '''
        Connects to server using handshake
        '''
        # send request
        request = connectionRequest()
        request.clientname = str(self.__name)
        self.__send( request.toxml("utf-8", element_name="connectionrequest") )
        print "send connection request"
        
        # recieve response
        data = None
        while not data:
            data, addr= self.__recvData()
            
        dom = CreateFromDocument(data)
        if type(dom) == connectionAcknowlege:
            assert isinstance(dom, connectionAcknowlege)
            if dom.connectionallowed and dom.clientname == self.__name:
                # connection established
                self.__connected = True
                self.__serverName = str(dom.servername)
                self._processOnClientAddedListener(addr)
        
                # send established response to server
                established = connectionEstablished()
                self.__send( established.toxml("utf-8", element_name="connectionestablished") )
            else:
                print "connection not allowed"
        
        
    def __handshakeServer(self, data, addr):
        '''
        Connects client and server using handshake
        @return: True if data was handshake data 
        '''
        try:
            dom = CreateFromDocument(data)
            if type(dom) == connectionRequest:
                assert isinstance(dom, connectionRequest)
                clientname = str(dom.clientname) 
                
                # check if client already there
                if self.__overwriteNewClients or (not self.__isClientInList(clientname, addr) and not self.__isClientPending(addr) ):
                    # add client
                    self.__sendHandshakeAck(clientname, addr, True)
                    self.__addClientPending(clientname, addr)
                    
                else:
                    # refuse request
                    self.__sendHandshakeAck(clientname, addr, False)
                
            elif type(dom) == connectionEstablished:
                if self.__isClientPending(addr):
                    clientname, addr = self.__getClientPendingName(addr)
                    self.__removeClientPending(clientname, addr)
                    self.__addClientToList(clientname, addr)
                          
            else:
                return False
                              
                
        except:
            return False
            
        return True
        
    def __sendHandshakeAck(self, clientname, addr, allowed=True):
        '''
        Send handshake ackknowledge
        '''
        reply = connectionAcknowlege()
        reply.clientname = clientname
        reply.connectionallowed = allowed
        reply.servername = self.__name
        self.__sendto(reply.toxml("utf-8", element_name="connectionacknowlege"), addr)
        
    
    def getServerName(self):
        '''
        @return: Name of server
        '''
        return self.__serverName
        
        
    def __recvData(self, sock=None):
        '''
        Recieves data from remote site
        @param sock: Socket to use (TCP and server only)
        @return: data, addr
        '''
        data = None
        addr = None
        try:
            if self.isConnected() and self.__server:
                # server recieve
                if sock != None:
                    if not self.__udpOn:
                        data, addr = sock.recvfrom( self.__recieveBufferSize )
                    else:
                        data, addr = self.__socket.recvfrom( self.__recieveBufferSize )
            else:
                # client recieve
                data = self.__socket.recv( self.__recieveBufferSize )
                addr = (self.__host, self.__port)
        except:
            pass
        
        return data, addr
       
    def __isClientInList(self, clientname, addr):
        '''
        Checks if client is already connected
        @param clientname: Name of client
        @param addr: Address of client
        '''
        for e in self.__connectedClients:
            if type(e) == tuple and len(e) == 2 and type(e[1]) == tuple and len(e[1]) == 2:
                if e[0] == clientname and e[1][0] == addr[0]:
                    return True
                
        return False
    
    def __getClientName(self, addr):
        '''
        Gets name of pending client
        @param addr: Address information of client
        @return: Tuple (clientname, addr) of clientname and address information 
        '''
        clientname = None
        for c in self.__connectedClients:
            if type(c) == tuple and len(c) == 2:
                if addr == c[1]:
                    clientname = c[0]
        return clientname, addr
    
    def __addClientToList(self, clientname, addr):
        '''
        Adds client to list of connected clients
        @param clientname: Name of client
        @param addr: Address information of client
        @return: True if client added
        '''
        if type(clientname) == str and type(addr) == tuple and len(addr) == 2 and not self.__isClientInList(clientname, addr):
            self.__connectedClients.append( (clientname, addr) )
            self._processOnClientAddedListener( (clientname, addr) )
            return True
        
        return False
                    
    def __removeClientFormList(self, clientname, addr):
        '''
        Removes client from list of connected clients
        @param clientname: Name of client
        @param addr: Address information of client
        @return: True if client was in list and is removed
        '''
        for e in self.__connectedClients:
            if type(e) == tuple and len(e) == 2 and len(e[1]) == 2:
                if e[0] == clientname and e[1][0] == addr[0]:
                    self.__connectedClients.remove(e)
                    return True
        return False
    
    def __isClientPending(self, addr):
        '''
        Cheks if client is pending for auth
        @param clientname: Name of client
        @param addr: Address information of client
        @return: True if client is pending
        '''
        if self.__getClientPendingName(addr)[0] == None:
            return False
        return True
        
    def __getClientPendingName(self, addr):
        '''
        Gets name of pending client
        @param addr: Address information of client
        @return: Tuple (clientname, addr) of clientname and address information 
        '''
        clientname = None
        for c in self.__pendingClients:
            if type(c) == tuple and len(c) == 2:
                if addr == c[1]:
                    clientname = c[0]
        return clientname, addr
    
    
    def __addClientPending(self, clientname, addr):
        '''
        Adds client to pending list
        @param clientname: Name of client
        @param addr: Address information of client
        @return: True if client not already and list and added
        '''
        if type(clientname) == str and type(addr) == tuple and len(addr) == 2 and not self.__isClientPending(addr):
            self.__pendingClients.append( (clientname, addr) )
            return True
        
        return False
    
    def __removeClientPending(self, clientname, addr):
        '''
        Removes pending client from list
        @param clientname: Name of client
        @param addr: Address information of client
        @return: Tuple (clientname, addr) of clientname and address information 
        '''
        try:
            self.__pendingClients.remove( (clientname, addr) )
        except:
            pass
        return (clientname, addr)
    
    
    def stopSocket(self):
        '''
        Stops the socket
        '''
        self.__stopSocket = True
        self.__socket.close()
        self.__connected = False
    
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
                if sock != self.__socket:
                    self.__sendto(data, sock)
                        
    def __sendto(self, data, sock):
        '''
        Send data so specific client
        @param data: String data to send
        @param sock: Socket to use. Could be a socket object for tcp connections
        or addr or tuple (*, addr) of remote site for udp connections
        '''
        if self.isConnected() and type(data) == str and sock != None:
            if self.__udpOn:
                if len(sock) == 2 and type(sock[1]) == tuple:
                    self.__socket.sendto(data, sock[1])
                else:
                    self.__socket.sendto(data, sock)
            else:
                sock.send(data)
        
    
    def sendData(self, datapackage):
        '''
        Sends a data package object
        '''   
        if self.__connected:
            self.__send( datapackage )
            
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