'''
Created on 11.09.2013

@author: hannes
'''

from mrLib.networking.mrSocketManager import mrSocketManager
from src.mrLib.networking.mrSocketMonitor import mrSocketMonitor
from src.mrLib.networking import mrProtocol
from src.mrLib.logger import mrLogger
from time import sleep

# LISTENER FUNCTIONS
def onClientAddedListener(clientdata):
    mrLogger.log( "new client " + str(clientdata[1]) + " added", mrLogger.LOG_LEVEL['info'] )
    
def onDataRecievedListener(socket, data):
    mrLogger.log( str(socket.getSocketAddress()) + " recieved data", mrLogger.LOG_LEVEL['info'] )


# MAIN FUNCTION
if __name__ == '__main__':
    
    print "test started ..."
    mrLogger.logClear()
    mrLogger.LOGGER_LOG_LEVEL = mrLogger.LOG_LEVEL['debug']
    mrLogger.log( "sockettest started" )
    
    # generate data package
    data = mrProtocol.mrProtocolData()
    data.addDataItem("KEY1", "value1")
    data.addDataItem("KEY1", "value2")
    
    # create server
    server = mrSocketManager( server=True )
    
    # wait for server
    while not server.isConnected():
        pass
    
    # enable socket monitor
    monitor = mrSocketMonitor( server )
    
    # create clients
    client1 = mrSocketManager()   
    client2 = mrSocketManager()
    
    # wait for clients
    while not client1.isConnected() or not client2.isConnected():
        pass
    
    # set listener
    server.addOnClientAddedListener( onClientAddedListener )
    server.addOnDataRecievedListener( onDataRecievedListener )
    client1.addOnDataRecievedListener( onDataRecievedListener )
    client2.addOnDataRecievedListener( onDataRecievedListener )
           
    sleep(1.0)
    
    data.setHost("Client 1")
    client1.sendData( data )
    sleep(0.5)
    mrLogger.log( "Server Recv: " + str(server.getFirstData()), mrLogger.LOG_LEVEL['debug'] )
    
    data.setHost("Client 2")
    client2.sendData( data )
    sleep(0.5)
    mrLogger.log( "Server Recv: " + str(server.getFirstData()), mrLogger.LOG_LEVEL['debug'] )
    
    data.setHost("Server")
    server.sendData( data )
    sleep(0.5)
    
    while client1.hasNextData():
        mrLogger.log( "Client1 Recv: " + str(client1.getFirstData()), mrLogger.LOG_LEVEL['debug'] )
        
    while client2.hasNextData():
        mrLogger.log( "Client2 Recv: " + str(client2.getFirstData()), mrLogger.LOG_LEVEL['debug'] )
        
        
    # replay monitored data
    monitor.startReplay()
    timestamp = 0.0
    while monitor.getBufferSize() > 0:
        monitor.updateTimestamp(timestamp)
        timestamp += 1000
        
    while server.hasNextData():
        mrLogger.log( "Server Recv: " + str(server.getFirstData()), mrLogger.LOG_LEVEL['debug'] )
    
    server.removeOnClientAddedListener(onClientAddedListener)
    
    mrLogger.log( "sockettest finished" )
    print "test finished"