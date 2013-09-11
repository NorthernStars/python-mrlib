'''
Created on 11.09.2013

@author: hannes
'''
from mrLib.networking.mrSocketManager import mrSocketManager
from time import sleep

if __name__ == '__main__':
    
    server = mrSocketManager( server=True )
    
    # wait for server
    while not server.isConnected():
        pass
    
    client1 = mrSocketManager()   
    client2 = mrSocketManager()
    
    # wait for clients
    while not client1.isConnected() or not client2.isConnected():
        pass
       
    sleep(1.0)
    client1.sendData( "test client 1" )
    sleep(0.5)
    client2.sendData( "test client 2" )
    sleep(0.5)
    server.sendData("server test")
    sleep(1.0)