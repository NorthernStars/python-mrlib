'''
Created on 25.09.2013

@author: hannes
'''

VISION_MODE_STREAM_ALL = "VISION_MODE_STREAM_ALL"
VISION_MODE_STREAM_BOTS = "VISION_MODE_STREAM_BOTS"
VISION_MODE_STREAM_BG_OBJ = "VISION_MODE_STREAM_BG_OBJ"
VISION_MODE_STREAM_OBJ = "VISION_MODE_STREAM_OBJ"
VISION_MODE_STOPPED = "VISION_MODE_STOPPED"
VISION_MODE_CALIBRATE_DIST = "VISION_MODE_CALIB_DIST"
VISION_MODE_CALIBRATE_TRANSF = "VISION_MODE_CALIB_TRANSF"
VISION_MODE_TERMINATE = "VISION_MODE_TERMINATE"
VISION_MODE_NONE = "VISION_MODE_NONE"

VISION_STREAMING_MODES = [VISION_MODE_STREAM_ALL,
                          VISION_MODE_STREAM_BG_OBJ,
                          VISION_MODE_STREAM_BOTS,
                          VISION_MODE_STREAM_OBJ]

VISION_OBJ_BOT = "VISION_OBJ_BOT"
VISION_OBJ_RECT = "VISION_OBJ_RECT"

class mrVisionObject():
    '''
    Class for vision objects
    '''
    
    __type = None
    __id = None
    __name = "None"
    __location = (0,0)      # (x,y)
    __angle = 0.0
    __radius = 0.0
    __size = (0,0)          # (w,h)
    
    def __init__( self, objType=None, objID=None, name="None", location=(0,0), angle=0.0, radius=0.0, size=(0,0) ):
        '''
        Constructor
        @param objType: Type of object
        @param objID: ID of object
        @param name: Name of object
        @param location: Tuple of (x,y) coordinates of objects location
        @param angle: Angle in degree of objects view direction
        @param radius: Radius of object
        @param size: Tuple of (w,h) width and height of the object
        '''        
        self.__type = objType
        self.__id = objID
        self.__name = name
        self.__location = location
        self.__angle = angle
        self.__radius = radius
        self.__size = size
        
    def getType(self):
        return self.__type
    
    def getID(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def getLocation(self):
        return self.__location
    
    def getAngle(self):
        return self.__angle
    
    def getRadius(self):
        return self.__radius
    
    def getSize(self):
        return self.__size
    
    def setType(self, objType=None):
        if objType != None:
            self.__type = objType
        
    def setID(self, objID=None):
        self.__id = objID
        
    def setName(self, name="None"):
        self.__name = name
        
    def setLocation(self, location=(0,0)):
        if type(location) == tuple and len(location) == 2:
            self.__location = location
            
    def setAngle(self, angle=0.0):
        self.__angle = angle
        
    def setRadius(self, radius=0.0):
        self.__radius = radius
        
    def setSize(self, size=(0,0)):
        if type(size) == tuple and len(size) == 2:
            self.__size = size
    