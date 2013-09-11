'''
Created on 11.09.2013

@author: hannes
'''
from mrLib.networking.mrSocketManager import mrSocketManager
from time import sleep
from time import time
import src.mrLib.networking.DataPackage as DataPackage

if __name__ == '__main__':
    
    print "test started ..."
    print "-----------------------------------"
    
    # generate data package
    datapackage = DataPackage.DataPackage()
    datapackage.timestamp = time()
    datapackage.data = DataPackage.Data()
    datapackage.data.item.append( DataPackage.Item("KEY1", "value1") )
    datapackage.data.item.append( DataPackage.Item("KEY2", "value2") )

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
    datapackage.host = "client 1"
    datapackage.timestamp = time()
    client1.sendData( datapackage )
    sleep(0.5)
    print "Server Recv:", server.getDataBuffer()[0]
    print "-----------------------------------"
    
    datapackage.host = "client 2"
    datapackage.timestamp = time()
    client2.sendData( datapackage )
    sleep(0.5)
    print "Server Recv:", server.getDataBuffer()[0]
    print "-----------------------------------"
    
    datapackage.host = "server"
    datapackage.timestamp = time()
    server.sendData( datapackage )
    sleep(0.5)
    
    for msg in client1.getDataBuffer():
        print "Client1 Recv:", msg
        
    for msg in client2.getDataBuffer():
        print "Client2 Recv:", msg
    print "-----------------------------------"
    
    print "test finished"