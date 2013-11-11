'''
Created on 25.09.2013

@author: hannes
'''

VISION_MODE_STREAM_ALL = "VISION_MODE_STREAM_ALL"
VISION_MODE_STREAM_BOTS = "VISION_MODE_STREAM_BOTS"
VISION_MODE_STREAM_OBJ = "VISION_MODE_STREAM_OBJECTS"

VISION_MODE_STOPPED = "VISION_MODE_STOPPED"
VISION_MODE_CALIBRATE_DIST = "VISION_MODE_CALIBRATE_DISTANCE"
VISION_MODE_CALIBRATE_TRANSF = "VISION_MODE_CALIBRATE_TRANSFORMATION"
VISION_MODE_TERMINATE = "VISION_MODE_TERMINATE"
VISION_MODE_NONE = "VISION_MODE_NONE"

VISION_STREAMING_MODES = [VISION_MODE_STREAM_ALL,
                          VISION_MODE_STREAM_BOTS,
                          VISION_MODE_STREAM_OBJ]

VISION_ALL_OTHER_MODES = [VISION_MODE_STOPPED,
                    VISION_MODE_CALIBRATE_DIST,
                    VISION_MODE_CALIBRATE_TRANSF,
                    VISION_MODE_TERMINATE,
                    VISION_MODE_NONE]

VISION_OBJ_BOT = "BOT"
VISION_OBJ_RECT = "RECTANGLE"
VISION_OBJ_LINE = "LINE"
VISION_OBJ_CIRCLE = "CIRCLE"
VISION_OBJ_DOT = "DOT"
VISION_OBJ_TEXT = "TEXT"
VISION_OBJ_IMG = "IMAGE"

class mrVisionObject():
    '''
    Class for vision objects
    
    type:        Defines type of object
    id:          Unique ID of object
    name:        Name of object (could be any string)
    location:    Center position (x,y) of object for bot,
                 rectangle circle and dot.
                 For text labels and images this position is the bottom
                 left corner of the label/image!
    points:      List of points [x1, y1, x2, y2, ...] for line
    angle:       View angle of bot object
    radius:      Radius of circle/dot or width of line
    size:        Size (w,h) of rectangle
    color:       Color of object (r,g,b,a)
    textcolor:   Color of text in textlabel [r,g,b,a]
    text:        Text if label
    src:         Source of image
    '''
    
    __type = None
    __id = None
    __name = "None"
    __location = (0.0,0.0)          # (x,y)
    __points = []               # [x1, y1, x2, y2, ...]
    __angle = 0.0
    __radius = 0.001            # 0.0 - 1.0
    __size = (0.25,0.25)        # (w,h)
    __color = (1,1,1,1)         # (r,g,b,a)
    __textcolor = (1,1,1,1)     # [r,g,b,a]
    __text = ""
    __src = ""
    
    def __init__( self, objType=None, objID=None, name="None", location=(0,0), points=[], angle=0.0,
                  radius=0.001, size=(0.25,0.25), color=(1,1,1,1), textcolor=[1,1,1,1], text="", src="" ):
        '''
        Constructor
        @param objType: Type of object
        @param objID: ID of object
        @param name: Name of object
        @param location: Tuple of (x,y) coordinates of objects location
        @param points: List [x1, y1, x2, y2, ...] of points of lines
        @param angle: Angle in degree of objects view direction
        @param radius: Radius of object
        @param size: Tuple of (w,h) width and height of the object
        @param color: RGBA color tuple of object
        @param textcolor: RGBA color list of text color inside label 
        @param text: Text for text label
        @param src: Source of image
        '''        
        self.__type = objType
        self.__id = objID
        self.__name = name
        self.__location = location
        self.__points = points
        self.__angle = angle
        self.__radius = radius
        self.__size = size
        self.__color = color
        self.__textcolor = textcolor
        self.__text = text
        self.__src = src
        
    def getType(self):
        return self.__type
    
    def getID(self):
        if self.__id != None:
            return int(self.__id)
        return -1
    
    def getName(self):
        return str(self.__name)
    
    def getLocation(self):
        return self.__location
    
    def getPoints(self):
        return self.__points
    
    def getAngle(self):
        return self.__angle
    
    def getRadius(self):
        return self.__radius
    
    def getSize(self):
        return self.__size
    
    def getColor(self):
        return self.__color
    
    def getTextColor(self):
        return self.__textcolor
    
    def getText(self):
        return str(self.__text)
    
    def getSrc(self):
        return str(self.__src)
    
    
    def setType(self, objType=None):
        if objType != None:
            self.__type = objType
        
    def setID(self, objID=None):
        self.__id = int(objID)
        
    def setName(self, name="None"):
        self.__name = str(name)
        
    def setLocation(self, location=(0,0)):
        if type(location) == tuple and len(location) == 2:
            self.__location = location
            
    def setPoints(self, points=[]):
        if type(points) == list:
            self.__points = points
            
    def setAngle(self, angle=0.0):
        self.__angle = angle
        
    def setRadius(self, radius=0.0):
        self.__radius = radius
        
    def setSize(self, size=(0,0)):
        if type(size) == tuple and len(size) == 2:
            self.__size = size
            
    def setColor(self, color=(1,1,1,1)):
        if type(color) == tuple and len(color) == 4:
            self.__color = color
            
    def setTextColor(self, color=[1,1,1,1]):
        if type(color) == list and len(color) == 4:
            self.__textcolor = color
            
    def setText(self, text=""):
        self.__text = str(text)
        
    def setSrc(self, src=""):
        self.__src = str(src)
        
            
    def __str__(self):
        '''
        Converts object to string
        '''
        return str(self.__id)+":"+self.__name
    