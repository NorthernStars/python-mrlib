'''
Created on 11.11.2013

@author: northernstars
'''
from time import sleep

from mrLib.networking.mrSocketManager import mrSocketManager

def onClientAddedListener(clientdata):
    print( "SERVER: new client " + str(clientdata[1]) + " added" )
    
def onDataRecievedListener(socket, addr, data):
    print( str(socket.getSocketAddress()) + " recieved data: " + str(data) + "\n" )

if __name__ == '__main__':
    
    # create server
    print "creating server"
    server = mrSocketManager(server=True, udpOn=True, name="server", useHandshake=True)
    
    # wait for server
    while not server.isConnected():
        pass
    
    # create client
    print "creating client"
    client1 = mrSocketManager(udpOn=True, name="client1", useHandshake=True)
    
    
    client1.addOnDataRecievedListener(onDataRecievedListener)
    server.addOnClientAddedListener(onClientAddedListener)
    server.addOnDataRecievedListener(onDataRecievedListener)
    
    sleep(1)
    
    # wait for client
    while not client1.isConnected():
        pass
    
    sleep(1)
    
    # send data
    client1.sendData("hallo")
    server.sendData("hallo2")
    
    sleep(5)
    print "ENDE"