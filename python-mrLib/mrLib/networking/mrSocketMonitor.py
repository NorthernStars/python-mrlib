'''
Created on 13.09.2013

@author: hannes
'''
from mrSocketManager import mrSocketManager
from time import time

class mrSocketMonitor(object):
    '''
    Class to monitor network traffic
    '''
    __manager = mrSocketManager()
    __dataBuffer = []
    __record = False
    __replay = False
    __startTime = 0.0

    def __init__(self, socketManager):
        '''
        Constructor
        @param socketManager: SocketManager to 
        '''
        self.__manager = mrSocketManager()
        self.__manager = socketManager
        self.clearDataBuffer()
        self.__manager.addOnDataRecievedListener( self.__onDataRecievedListener )
    
    def __onDataRecievedListener(self, socket, data):
        '''
        onDataRecievedListener function
        '''
        if self.__record:
            self.__dataBuffer.append( data )
    
    def startRecord(self):
        '''
        Starts recording
        '''
        self.__record = True
        self.__startTime = time()
        
    def stopRecord(self):
        '''
        Stops recording
        '''
        self.__record = False
    
    def startReplay(self):
        '''
        Starts replay mode
        '''
        self.__replay = False
    
    def stopReplay(self):
        '''
        Stops replay mode
        '''
        self.__replay = True
        
    def getDataBuffer(self):
        '''
        Returns the data buffer
        '''
        return self.__dataBuffer
    
    def clearDataBuffer(self):
        '''
        Clears the data buffer
        '''
        self.__dataBuffer = []
        
    def getBufferSize(self):
        '''
        Returns buffer size
        '''
        return len(self.__dataBuffer) 
        
    def updateTimestamp(self, timestamp):
        '''
        Updates timestamp of replay mode
        and pushes data to socket manager
        '''
        if not self.__replay:
            for data in self.__dataBuffer:
                # check if to send data
                if (data.timestamp - self.__startTime) <= timestamp: 
                    data.timestamp = time()
                    self.__manager.pushRecvData(data)
                    self.__dataBuffer.remove( data )