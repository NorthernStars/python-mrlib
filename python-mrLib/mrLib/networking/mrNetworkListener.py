'''
Created on 25.09.2013

@author: hannes
'''
from thread import start_new_thread

class mrNetworkListener(object):
    '''
    classdocs
    '''    
    __onClientAddedList = []
    __onDataRecievedList = []


    def __init__(self):
        '''
        Constructor
        '''
        self.__onClientAddedList = []
        self.__onDataRecievedList = []
    
    
    def _processOnClientAddedListener(self, clientData):
        '''
        Function to handle onClientAddedListener
        '''
        for listener in self.__onClientAddedList:
            if listener != None:
                start_new_thread( listener, (clientData) )
            
    def _processOnDataRecievedListener(self, addr, datapackage):
        '''
        Function to handle onDataRecievedListener
        '''
        for listener in self.__onDataRecievedList:
            if listener != None:
                listener(self, addr, datapackage)
            
    def addOnClientAddedListener(self, listener):
        '''
        Sets onClientAdded listener
        @param listener: Listener function.
        '''
        if listener not in self.__onClientAddedList:
            self.__onClientAddedList.append( listener )
        
    def addOnDataRecievedListener(self, listener):
        '''
        Sets onDataRecieved listener
        @param listener: Listener function
        '''
        if listener not in self.__onDataRecievedList:
            self.__onDataRecievedList.append( listener )
        
    def removeOnClientAddedListener(self, listener):
        '''
        Removes onClientAdded listener
        '''
        self.__onClientAddedList.remove( listener )
        
    def removeOnDataRecievedListener(self, listener):
        '''
        Removes onDataRecieved listener
        @param listener: Listener to remove
        '''
        self.__onDataRecievedList.remove( listener )