'''
Created on 12.11.2013

@author: northernstars
'''

class mrGraphicsObject(object):
    '''
    Class for graphic objects
    
    id:          Unique ID of object
    location:    Center position (x,y) of object for bot,
                 rectangle circle and dot.
                 For text labels and images this position is the bottom
                 left corner of the label/image!
    '''    
    __id = None
    __location = (0.0,0.0)          # (x,y)
    __color = (1,1,1,1)         # (r,g,b,a)
    __name = "None"
    
    def __init__( self, objID=None, location=(0,0), color=(1,1,1,1), name="" ):
        '''
        Constructor
        @param objID: ID of object        
        @param location: Tuple of (x,y) coordinates of objects location
        @param color: RGBA color tuple of object
        '''    
        self.setID(objID)
        self.setLocation(location)
        self.setName(name)
        self.setColor(color)
        
    def getID(self):
        if self.__id != None:
            return self.__id
        return -1
    
    def getLocation(self):
        return self.__location
    
    def getColor(self):
        return self.__color
    
    def setID(self, objID=None):
        if objID == None:
            objID = -1
        self.__id = objID
        
    def setLocation(self, location=(0,0)):
        if type(location) == tuple and len(location) == 2:
            self.__location = location
            
    def setColor(self, color=(1,1,1,1)):
        if type(color) == tuple and len(color) == 4:
            self.__color = color
            
    def getName(self):
        return str(self.__name)
    
    def setName(self, name="None"):
        self.__name = str(name)
            
    def __str__(self):
        '''
        Converts object to string
        '''
        return str(self.__id)+":"+self.__name
    
    
class mrGraphicsAngleObject(mrGraphicsObject):
    '''
    Abstract object for objects with angle
    angle:       Angle of object
    '''
    __angle = ""
    
    def __init__(self, objID=None, location=(0,0), color=(1,1,1,1), name="", angle=0.0):
        '''
        Constructor
        @param objID: ID of object        
        @param location: Tuple of (x,y) coordinates of objects location
        @param color: RGBA color tuple of object
        @param angle: Angle in degree of objects
        '''
        mrGraphicsObject.__init__(self, objID=objID, location=location, color=color, name=name)
        self.setAngle(angle)
    
    def getAngle(self):
        return self.__angle
    
    def setAngle(self, angle=0.0):
        self.__angle = angle
        
    
class mrGraphicsBot(mrGraphicsAngleObject):
    '''
    Class for graphic bots 
    '''
    __size = (0.25,0.25)        # (w,h)
    
    def __init__( self, objID=None, location=(0,0), color=(1,1,1,1), name="", angle=0.0, size=(0.01, 0.01) ):
        '''
        Constructor
        @param objID: ID of object        
        @param location: Tuple of (x,y) coordinates of objects location
        @param color: RGBA color tuple of object
        @param angle: Angle in degree of objects
        @param name: Name of object
        '''
        mrGraphicsAngleObject.__init__(self, objID=objID, location=location, color=color, name=name, angle=angle)
        self.setSize(size)
        
    def getSize(self):
        return self.__size
    
    def setSize(self, size=(0,0)):
        if type(size) == tuple and len(size) == 2:
            self.__size = size        
        
        
    
class mrGraphicsRectangle(mrGraphicsAngleObject):
    '''
    Class for drawing rectangle
    '''
    __size = (0.25,0.25)        # (w,h)
    
    def __init__(self, objID=None, location=(0,0), color=(1,1,1,1), name="", angle=0.0, size=(0.25, 0.25)):
        '''
        Constructor
        @param objID: ID of object        
        @param location: Tuple of (x,y) coordinates of objects location
        @param color: RGBA color tuple of object
        @param angle: Angle in degree of objects
        @param size: Tuple of (w,h) width and height of the object
        '''
        mrGraphicsAngleObject.__init__(self, objID=objID, location=location, color=color, name=name, angle=angle)
        self.setSize(size)
        
    def getSize(self):
        return self.__size
    
    def setSize(self, size=(0,0)):
        if type(size) == tuple and len(size) == 2:
            self.__size = size
            
            
class mrGraphicsLine(mrGraphicsObject):
    '''
    Class for drawing lines
    '''
    __width = 1.0
    __points = []   # [x1, y1, x2, y2, ...]
    
    def __init__(self, objID=None, location=(0,0), color=(1,1,1,1), name="", points=[] , width=0.5):
        '''
        Constructor
        @param objID: ID of object        
        @param location: Tuple of (x,y) coordinates of objects location
        @param color: RGBA color tuple of object
        @param points: List [x1, y1, x2, y2, ...] of points of lines
        @param width: [UNUSED] Width of line
        '''
        mrGraphicsObject.__init__(self, objID=objID, location=location, color=color, name=name)
        self.setPoints(points)
        self.setWidth(width)
 
    def getPoints(self):
        return self.__points
    
    def setPoints(self, points=[]):
        if type(points) == list:
            self.__points = points
            
    def getWidth(self):
        return self.__width
        
    def setWidth(self, width=1.0):
        self.__width = width
        

class mrGraphicsEllipse(mrGraphicsRectangle):
    '''
    Class for drawing Ellipses
    '''
    
    def __init__(self, objID=None, location=(0,0), color=(1,1,1,1), name="", angle=0.0, size=(0.25, 0.25)):
        '''
        Constructor
        @param objID: ID of object        
        @param location: Tuple of (x,y) coordinates of objects location
        @param color: RGBA color tuple of object
        @param angle: Angle in degree of objects
        @param size: Tuple of (w,h) width and height of the object
        '''
        mrGraphicsRectangle.__init__(self, objID=objID, location=location, color=color, name=name, angle=angle, size=size)
        
        
class mrGraphicsDot(mrGraphicsEllipse):
    '''
    Class for drawing a dot
    '''
    __radius = 0.01
    
    def __init__(self, objID=None, location=(0,0), color=(1,1,1,1), name="", radius=0.01):
        '''
        Constructor
        @param objID: ID of object        
        @param location: Tuple of (x,y) coordinates of objects location
        @param color: RGBA color tuple of object
        @param radius: Radius of object 
        '''
        mrGraphicsEllipse.__init__(self, objID=objID, location=location, color=color, name=name, angle=0.0, size=(2*radius, 2*radius))
        self.setRadius(radius)
    
    def getRadius(self):
        return self.__radius
    
    def setRadius(self, radius=0.0):
        self.__radius = radius
        
        
class mrGraphicsCircle(mrGraphicsObject):
    '''
    Class for drawing circle
    '''
    __radius = 0.01
    __width = 1.0
    
    def __init__(self, objID=None, location=(0,0), color=(1,1,1,1), name="", radius=0.01, width=0.5):
        '''
        Constructor
        @param objID: ID of object        
        @param location: Tuple of (x,y) coordinates of objects location
        @param color: RGBA color tuple of object
        @param radius: Radius of object 
        @param width: [UNUSED] Width of line
        '''
        mrGraphicsObject.__init__(self, objID=objID, location=location, name=name, color=color)
        self.setRadius(radius)
        self.setWidth(width)
    
    def getRadius(self):
        return self.__radius
    
    def setRadius(self, radius=0.0):
        self.__radius = radius
        
    def getWidth(self):
        return self.__width
        
    def setWidth(self, width=1.0):
        self.__width = width
        
        
class mrGraphicsText(mrGraphicsAngleObject):
    '''
    Class for drawing text labels
    '''
    __textcolor = (1,1,1,1)     # [r,g,b,a]
    __text = ""
    __fontsize = 12
    
    def __init__(self, objID=None, location=(0,0), color=(1,1,1,1), name="", angle=0.0, text="", textcolor=[1,1,1,1], fontsize=12):
        '''
        Constructor
        @param objID: ID of object        
        @param location: Tuple of (x,y) coordinates of objects location
        @param color: RGBA color tuple of object
        @param angle: Angle in degree of objects
        @param text: Text of label
        '''
        mrGraphicsAngleObject.__init__(self, objID=objID, location=location, color=color, name=name, angle=angle)
        self.setText(text)
        self.setTextColor(textcolor)
        
    def getTextColor(self):
        return self.__textcolor
    
    def getText(self):
        return str(self.__text)
    
    def getFontSize(self):
        return self.__fontsize
    
    def setTextColor(self, color=[1,1,1,1]):
        if type(color) == list and len(color) == 4:
            self.__textcolor = color
            
    def setText(self, text=""):
        self.__text = str(text)
        
    def setFontSize(self, fontsize=12):
        self.__fontsize = fontsize
       
    
class mrGraphicsImage(mrGraphicsRectangle):
    '''
    Class for drawing image
    '''
    __src = ""
    __keepRatio = False
    
    def __init__(self, objID=None, location=(0,0), color=(1,1,1,1), name="", angle=0.0, size=(0.25, 0.25), src="", keepRatio=False):
        '''
        Constructor
        @param objID: ID of object        
        @param location: Tuple of (x,y) coordinates of objects location
        @param color: RGBA color tuple of object
        @param angle: Angle in degree of objects
        '''
        mrGraphicsRectangle.__init__(self, objID=objID, location=location, color=color, name=name, angle=angle, size=size)     
        self.setSource(src)
        self.setKeepRatio(keepRatio)
    
    def getSource(self):
        return str(self.__src)
    
    def setKeepRatio(self, keepRatio=False):
        self.__keepRatio = keepRatio
        
    def setSource(self, src=""):
        self.__src = str(src)
        
    def keepRatio(self):
        return self.__keepRatio