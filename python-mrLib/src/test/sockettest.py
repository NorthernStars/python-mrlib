'''
Created on 11.09.2013

@author: hannes
'''
from mrLib.networking.mrSocketManager import mrSocketManager
from time import sleep
import src.mrLib.networking.mrProtocol as mrProtocol

if __name__ == '__main__':
    
    print "test started ..."
    print "-----------------------------------"
    
    # generate data package
    data = mrProtocol.mrProtocolData()
    data.addDataItem("KEY1", "value1")
    data.addDataItem("KEY1", "value2")
    print data
    
    # create server
    server = mrSocketManager( server=True )
    
    # wait for server
    while not server.isConnected():
        pass
    
    # create clients
    client1 = mrSocketManager()   
    client2 = mrSocketManager()
    
    # wait for clients
    while not client1.isConnected() or not client2.isConnected():
        pass       
    sleep(1.0)
    
    data.setHost("Client 1")
    client1.sendData( data )
    sleep(0.5)
    print "Server Recv:", server.getFirstData()
    print "-----------------------------------"
    
    data.setHost("Client 2")
    client2.sendData( data )
    sleep(0.5)
    print "Server Recv:", server.getFirstData()
    print "-----------------------------------"
    
    data.setHost("Server")
    server.sendData( data )
    sleep(0.5)
    
    for msg in client1.getDataBuffer():
        print "Client1 Recv:", msg
        
    for msg in client2.getDataBuffer():
        print "Client2 Recv:", msg
    print "-----------------------------------"
    
    print "test finished"