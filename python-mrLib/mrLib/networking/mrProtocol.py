'''
Created on 11.09.2013

@author: hannes
'''
from DataPackage import DataPackage, Data, Item
from time import time
from datetime import datetime

PROTOCOL_TYPE_NONE = "None"
PROTOCOL_TYPE_VISIONOBJECTS = "VisionObjects"
PROTOCOL_TYPE_VISIONBOTS = "VisionBots"
PROTOCOL_TYPE_GAMEDATA = "GameData"

PROTOCOL_ENCODING= "utf-8"


def createFromDataPackage(dataPackage=None):
    '''
    Converts data package to protocol data object
    @return: mrProtocolData object
    '''
    #dataPackage = DataPackage()
    try:
        # get basic data
        host = str(dataPackage.host)
        dataType = str(dataPackage.type)
        timestamp = float(dataPackage.timestamp)
        
        # create new protocl data object
        protocolData = mrProtocolData(
                                      host=host,
                                      dataType=dataType,
                                      timestamp=timestamp )
        
        # get data
        for item in dataPackage.Data.Item:
            protocolData.addDataItem(item.key, item.val)
            
        return protocolData
    except:
        return None


class mrProtocolData(object):
    '''
    Class for transmitting mixed-reality data
    '''
    
    __host = "localhost"
    __dataType = PROTOCOL_TYPE_NONE
    __data = {}
    __timestamp = None


    def __init__(self, dataType=PROTOCOL_TYPE_NONE, host="localhost", timestamp=None):
        '''
        Constructor
        @param dataType: Protocol data type
        @param host: Name of host
        @param timestamp: Timestamp of data
        '''
        self.__dataType = dataType
        self.__data = {}
        
        if type(host) == str:
            self.__host = host
            
        if timestamp != None:
            self.__timestamp = timestamp
    
    def getHost(self):
        '''
        Returns host of data
        '''
        return self.__host
    
    def getDataType(self):
        '''
        Returns data type
        '''
        return self.__dataType
    
    def getTimestamp(self):
        '''
        Returns timestamp of data
        '''
        return self.__timestamp
    
    def getData(self):
        '''
        Returns dictionary of data
        '''
        return self.__data
    
    def addDataItem(self, key, value):
        '''
        Adds a new data item to data dictionary
        '''
        if key in self.__data and type(self.__data[key]) == list:
            # key already available
            self.__data[key].append(value)
        else:
            #key not available or value is no list
            self.__data[key] = [value]
            
    def getDataItem(self, key):
        '''
        Returns value of data dictionary entry
        or None if key is not available
        '''
        if key in self.__data:
            return self.__data[key]
        return None
    
    def hasKey(self, key):
        '''
        Returns key, if in data dictionary
        '''
        if key in self.__data:
            return True
        return False
    
    def hasValue(self, value):
        '''
        Returns key of valueor None if not found
        '''
        for key in self.__data:
            if type(self.__data[key]) == list:
                for val in self.__data[key]:
                    if val == value:
                        return key
        return None
                    
    def hasItem(self, key, value):
        '''
        Returns true if data directory has a item with
        specified key and value
        '''
        if key in self.__data and type(self.__data[key]) == list:
            for val in self.__data[key]:
                if val == value:
                    return True
        return False
    
    def updateTimestamp(self):
        '''
        Updates the timestamp of data
        '''
        self.__timestamp = time()
        
    def setHost(self, host):
        '''
        Sets the host of data
        '''
        self.__host = str(host)
        
    def setDataTye(self, dataType):
        '''
        Sets the type of data
        '''
        self.__dataType = str(dataType)
        
    def clearData(self):
        '''
        Clears all data
        '''
        self.__data = {}
        
    def setData(self, data):
        '''
        Sets data dictionary
        '''
        if type(data) == dict:
            self.__data= data
    
    def toDataPackage(self):
        '''
        Converts protocol data to data package
        Sets timestamp if never updateTimestamp was called
        @return: DataPackage object
        '''
        # create data package
        dataPackage = DataPackage()
        dataPackage.host = self.__host
        dataPackage.type = self.__dataType
        
        if self.__timestamp == None:
            dataPackage.timestamp = time()
        
        # create data list
        data = Data()
        
        for key in self.__data:
            if type(self.__data[key]) == list:
                for val in self.__data[key]:
                    item = Item( str(key), str(val) )  
                    data.Item.append( item )
        
        # add data to data package
        dataPackage.Data = data
        
        return dataPackage
    
    def __str__(self):
        '''
        Overrides objects string method
        '''
        txt = str(self.__host) + " : " + str(self.__dataType) + " : "
        if self.__timestamp != None:
            txt += str( datetime.fromtimestamp(self.__timestamp) )
        else:
            txt += "-notime-"
        
        for key in self.__data:
            if type(self.__data[key]) == list and len(self.__data[key]) > 0:
                txt += "\n\t" + str(key) + ":"
                for val in self.__data[key]:
                    if txt.endswith(":"):
                        txt += " " + str(val)
                    else:
                        txt += ", " + str(val)
                        
        return txt