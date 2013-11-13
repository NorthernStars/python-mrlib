'''
Created on 25.10.2013

@author: northernstars
'''
from os.path import isfile

from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage

from kivy.graphics import Color, Rectangle, Line, Ellipse
from kivy.graphics.context_instructions import PushMatrix, PopMatrix, Rotate

from mrLib.networking.data.mrGraphicsData import mrGraphicsObject, mrGraphicsBot, mrGraphicsCircle, mrGraphicsDot, mrGraphicsText
from mrLib.networking.data.mrGraphicsData import mrGraphicsImage, mrGraphicsLine, mrGraphicsRectangle

class AbstractGraphicsSzenario(FloatLayout):
    '''
    Abstract class for creating a szenario
    1. To create szenario create subclass of this one.
       Create a constructor grabbing a widget as
       parameter and calling this superclass constructor.
    2. Override drawGui function to recieve vision
       data and create gui on this class.
    '''
    
    def convertPosition(self, pos=(0,0)):
        '''
        Converts relative positions
        @param pos: Position (x,y)
        @return: Converted position (x,y)
        '''
        if type(pos) == tuple:
            return (self.x+pos[0]*self.width, self.y+pos[1]*self.height)
        else:
            return self.x+pos*self.width
    
    def convertSize(self, size=(0,0)):
        '''
        Converts relative size
        @param size: Size (w,h)
        @return: Converted size (x,y)
        '''
        if type(size) == tuple:
            return (size[0]*self.width, size[1]*self.height)
        else:
            return size*self.width
    
    def convertPoints(self, points=[]):
        '''
        Converts relative points
        @param points: List [x1, y1, x2, y2, ...] of points
        @return: Converted list [x1, y1, x2, y2, ...] of pints
        '''
        isX = True
        retPoints = []
        for p in points:
            if isX:
                p = self.x+self.width*p
                isX = False
            else:
                p = self.y+self.height*p
                isX = True
            retPoints.append(p)
        return retPoints
    
    def drawObj(self, obj=None):
        '''
        Updates a object if object already on widget.
        Otherwise it will create a object
        Override this function to create your own
        apperance of ojects
        '''        
        assert isinstance(obj, mrGraphicsObject)

        if type(obj) == None:
            return False

        # get obj attributes
        objID = obj.getID()
        objname = obj.getName()
        location = self.convertPosition( obj.getLocation() )
        color = obj.getColor()
        wObj = None
        
        # draw objects
        with self.canvas:
            # set color
            Color( color[0], color[1], color[2], color[3] )
            
            if type(obj) == mrGraphicsBot:
                # draw bot
                assert isinstance(obj, mrGraphicsBot)
                size = self.convertSize( obj.getSize() )
                angle = obj.getAngle()
                viewBorder = 0.2
                p0 = ( location[0]-size[0]*0.5, location[1]-size[1]*0.5  )            # bottom left
                p1 = ( p0[0]+size[0], p0[1] )                               # bottom right
                p2 = ( p1[0], p1[1]+size[1] )                               # top right
                p3 = ( p0[0], p0[1]+size[1] )                               # top left
                pM = ( p0[0]+size[0]*viewBorder, p0[1]+(p3[1]-p0[1])*0.5 )  # middle between p0 and p3
                lineW = 1.2
                
                points = [ p0[0], p0[1], p1[0], p1[1], p2[0], p2[1], p3[0], p3[1], p0[0], p0[1]  ]  # outer line
                points2 = [ p1[0]-size[0]*viewBorder, p1[1]+size[1]*viewBorder,
                           pM[0], pM[1],
                           p2[0]-size[0]*viewBorder, p2[1]-size[1]*viewBorder,
                           p1[0]-size[0]*viewBorder, p1[1]+size[1]*viewBorder ]                     # view direction

                # draw object
                wObj = Widget( pos=p0 )
                lbl = Label( text=str(objID)+":"+objname, pos=p3 )
                lbl.texture_update()
                tsize = lbl.texture.size
                lbl.size = (tsize[0], tsize[1])
                
                # draw dot
                with wObj.canvas.before:
                    PushMatrix()
                    Rotate( angle=angle, axis=(0,0,1), origin=(location[0], location[1], 0) )                        
                with wObj.canvas.after:
                    PopMatrix()
                                            
                with wObj.canvas:
                    Color( color[0], color[1], color[2], color[3] )
                    Line( points=points, width=lineW )
                    Line( points=points2, width=lineW )
                   
                if angle != 0: 
                    with lbl.canvas.before:
                        PushMatrix()
                        Rotate( angle=angle, axis=(0,0,1), origin=(location[0], location[1], 0) )                        
                    with lbl.canvas.after:
                        PopMatrix()
                        
                        
            
            if type(obj) == mrGraphicsRectangle:
                # draw rectangle  
                assert isinstance(obj, mrGraphicsRectangle)
                size = self.convertSize( obj.getSize() )              
                pos = ( location[0]-size[0]/2, location[1]-size[1]/2 )
                angle = obj.getAngle()
                
                # draw new object
                wObj = Widget( size=size, pos=pos )
                
                # draw rectangle
                with wObj.canvas:
                    Color( color[0], color[1], color[2], color[3] )
                    Rectangle( size=size, pos=pos )
                    
                if angle != 0:
                    with wObj.canvas.before:
                        PushMatrix()
                        Rotate( angle=angle, axis=(0,0,1), origin=(location[0], location[1], 0) )                        
                    with wObj.canvas.after:
                        PopMatrix()                   


            if type(obj) == mrGraphicsLine:
                #draw line
                assert isinstance(obj, mrGraphicsLine)
                points = self.convertPoints( obj.getPoints() )
                width = self.convertSize( obj.getWidth() )       
                
                # draw new object
                wObj = Line( points=points, width=width )
            
            
            if type(obj) == mrGraphicsDot:
                #draw dot
                assert isinstance(obj, mrGraphicsDot)
                radius = self.convertSize( obj.getRadius() )
                size = (2*radius, 2*radius)
                pos = ( location[0]-radius, location[1]-radius  )
                
                # draw new object
                wObj = Ellipse( pos=pos, size=size  )
            
            
            if type(obj) == mrGraphicsCircle:
                #draw cricle
                assert isinstance(obj, mrGraphicsCircle)
                radius = self.convertSize( obj.getRadius() )
                width = self.convertSize( obj.getWidth() )
                
                # draw new object
                wObj = Line( circle=(location[0], location[1], radius), width=width )
                    
                    
            if type(obj) == mrGraphicsText:
                #draw text
                assert isinstance(obj, mrGraphicsText)
                text = obj.getText()
                textcolor = obj.getTextColor()
                fontsize = obj.getFontSize()
                angle = obj.getAngle()
                
                # draw new object
                padding = 5
                wObj = Label( text=text, pos=location, markup=True, color=textcolor )
                if fontsize != None:
                    print "set fontsize", fontsize
                    wObj.font_size = fontsize
                
                wObj.texture_update()
                size = wObj.texture.size
                wObj.size = (size[0]+2*padding, size[1]+2*padding)
                 
                with wObj.canvas.before:                        
                    PushMatrix()
                    Rotate( angle=angle, axis=(0,0,1), origin=(location[0], location[1], 0) )  
                    Color( color[0], color[1], color[2], color[3] )
                    Rectangle( pos=wObj.pos, size=wObj.size)   
                                            
                with wObj.canvas.after:                        
                    PopMatrix()
                        
                        
            if type(obj) == mrGraphicsImage:
                # draw image
                assert isinstance(obj, mrGraphicsImage)
                src = obj.getSource()
                keepRatio = obj.keepRatio()
                size = self.convertSize( obj.getSize() )                
                angle = obj.getAngle()
                
                if isfile(src):
                    wObj = AsyncImage( source=src, size=size, allow_stretch=True, keep_ratio=keepRatio )
                    wObj.texture_update()
                    pos = (location[0]-size[0]*0.5, location[1]-size[1]*0.5)
                    wObj.pos = pos
                    size = wObj.size
                    
                    if angle != 0:
                        with wObj.canvas.before:
                            PushMatrix()
                            Rotate( angle=angle, axis=(0,0,1), origin=(location[0], location[1], 0) )
                                                    
                        with wObj.canvas.after:
                            PopMatrix()
            
        # send update request to canvas
        self.canvas.ask_update()
        
        # return new object
        return wObj
    
    
    def clearObjects(self):
        '''
        Clears all objects from this widget or from canvas
        '''
        for obj in self.children:
            self.remove_widget(obj)
            obj = None
        
        self.clear_widgets()
        self.canvas.clear()
            
        
    def drawGui(self, data=None):
        '''
        Recives vision data and maniupulates widget
        @param data: List of objects of type mrGraphicsObject
        '''
        retList = []
        if type(data) == list:
            # clear drawn objects
                        
            # draw objects
            for obj in data:
                retList.append( self.drawObj(obj) )
                
        
        return retList

            
            