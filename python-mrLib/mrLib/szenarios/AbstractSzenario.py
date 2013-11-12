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
    _guiObjs = {}
    
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
    
    def _updateObj(self, obj=None):
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
        loc = self.convertPosition( obj.getLocation() )
        color = obj.getColor()
        
        # get object from widget children or canvas or None if not found
        wObj = self._getObjFromWidget(obj)
        update = False
        if wObj != None:
            update = True
        
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
                p0 = ( loc[0]-size[0]*0.5, loc[1]-size[1]*0.5  )            # bottom left
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

                if update:
                    # update object
                    assert isinstance(wObj, list)
                    if type(wObj) == list:
                        wObj[0].canvas.clear()
                        
                else:
                    # draw new object
                    wObj = [Widget( pos=p0 )]
                    lbl = Label( text=str(objID)+":"+objname, pos=p3 )
                    lbl.texture_update()
                    tsize = lbl.texture.size
                    lbl.size = (tsize[0], tsize[1])
                    wObj.append(lbl)
                
                # draw dot
                if type(wObj) == list and len(wObj) > 0:
                    with wObj[0].canvas.before:
                        PushMatrix()
                        Rotate( angle=angle, axis=(0,0,1), origin=(loc[0], loc[1], 0) )                        
                    with wObj[0].canvas.after:
                        PopMatrix()
                                                
                    with wObj[0].canvas:
                        Color( color[0], color[1], color[2], color[3] )
                        Line( points=points, width=lineW )
                        Line( points=points2, width=lineW )
                        
                    with wObj[1].canvas.before:
                        PushMatrix()
                        Rotate( angle=angle, axis=(0,0,1), origin=(loc[0], loc[1], 0) )                        
                    with wObj[1].canvas.after:
                        PopMatrix()
                        
                        
            
            if type(obj) == mrGraphicsRectangle:
                # draw rectangle  
                assert isinstance(obj, mrGraphicsRectangle)
                size = self.convertSize( obj.getSize() )              
                pos = ( loc[0]-size[0]/2, loc[1]-size[1]/2 )
                angle = obj.getAngle()
                if update:
                    # update object
                    assert isinstance(wObj, Widget)
                    if type(wObj) == Widget:
                        wObj.canvas.clear()
                else:
                    # draw new object
                    wObj = Widget( size=size, pos=pos )
                
                # draw rectangle
                if type(wObj) == Widget :
                    with wObj.canvas.before:
                        PushMatrix()
                        Rotate( angle=angle, axis=(0,0,1), origin=(loc[0], loc[1], 0) )                        
                    with wObj.canvas.after:
                        PopMatrix()
                        
                    with wObj.canvas:
                        Color( color[0], color[1], color[2], color[3] )
                        Rectangle( size=size, pos=pos )


            if type(obj) == mrGraphicsLine:
                #draw line
                assert isinstance(obj, mrGraphicsLine)
                points = self.convertPoints( obj.getPoints() )
                width = self.convertSize( obj.getWidth() )       
                if update:
                    # update object
                    assert isinstance(wObj, Line)
                    wObj.points = points
                    wObj.width = width
                else:
                    # draw new object
                    wObj = Line( points=points, width=width )
            
            
            if type(obj) == mrGraphicsDot:
                #draw dot
                assert isinstance(obj, mrGraphicsDot)
                radius = self.convertSize( obj.getRadius() )
                size = (2*radius, 2*radius)
                pos = ( loc[0]-radius, loc[1]-radius  )
                if update:
                    # update object
                    assert isinstance(wObj, Ellipse)
                    wObj.pos = pos
                    wObj.size = size
                else:
                    # draw new object
                    wObj = Ellipse( pos=pos, size=size  )
            
            
            if type(obj) == mrGraphicsCircle:
                #draw cricle
                assert isinstance(obj, mrGraphicsCircle)
                radius = self.convertSize( obj.getRadius() )
                width = self.convertSize( obj.getWidth() )
                if update:
                    # update object
                    assert isinstance(wObj, Line)                
                    wObj.circle = (loc[0], loc[1], radius)
                else:
                    # draw new object
                    wObj = Line( circle=(loc[0], loc[1], radius), width=width )
                    
                    
            if type(obj) == mrGraphicsText:
                #draw text
                assert isinstance(obj, mrGraphicsText)
                text = obj.getText()
                textcolor = obj.getTextColor()
                angle = obj.getAngle()
                if update:
                    # update object
                    assert isinstance(wObj, Label)                
                    wObj.text = text
                else:
                    # draw new object
                    padding = 5
                    wObj = Label( text=text, pos=loc, markup=True, color=textcolor )
                    wObj.texture_update()
                    size = wObj.texture.size
                    wObj.size = (size[0]+2*padding, size[1]+2*padding)
                    
                    with wObj.canvas.before:                        
                        PushMatrix()
                        Rotate( angle=angle, axis=(0,0,1), origin=(loc[0], loc[1], 0) )  
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
                if update:
                    # update object
                    assert isinstance(wObj, AsyncImage)
                    if wObj.source != src:
                        wObj.source = src
                        wObj.reload()
                    wObj.pos = loc
                    wObj.keep_ratio = keepRatio
                    wObj.size = size
                    size = wObj.size
                    pos = (loc[0]-size[0]*0.5, loc[1]-size[1]*0.5)
                    wObj.pos = pos
                else:
                    # draw new object
                    if isfile(src):
                        wObj = AsyncImage( source=src, size=size, allow_stretch=True, keep_ratio=keepRatio )
                        size = wObj.size
                        pos = (loc[0]-size[0]*0.5, loc[1]-size[1]*0.5)
                        wObj.pos = pos
                        
                        with wObj.canvas.before:
                            PushMatrix()
                            Rotate( angle=angle, axis=(0,0,1), origin=(loc[0], loc[1], 0) )                        
                        with wObj.canvas.after:
                            PopMatrix()
        
        # check if to add new object
        if not update and wObj != None:
            objname = str(objID)+":"+objname
            self._guiObjs[objname] = wObj
            
        # send update request to canvas
        self.canvas.ask_update()
        
        
    def _getObjFromWidget(self, obj=mrGraphicsObject()):
        '''
        Searches for a object in object list
        and returns it.
        If no object can be found it returns None
        @param obj: mrVisionObject to search for
        @return: Widget object or None
        '''
        assert isinstance(obj, mrGraphicsObject)
        objname = str(obj.getID())+":"+obj.getName()
        
        for key in self._guiObjs.keys():
            if str(key) == objname:
                return self._guiObjs[key]
        
        return None
    
    
    def _clearObjects(self):
        '''
        Clears all objects in self._guiObjs
        from this widget or from canvas
        '''
        for obj in self._guiObjs:
            if obj in self.children:
                self.remove_widget(obj)
            try:
                if obj in self.canvas.children:
                    self.canvas.remove(obj)
            except:
                pass
            obj = None
            
        self._guiObjs = {}
            
        
    def drawGui(self, data=None):
        '''
        Recives vision data and maniupulates widget
        @param data: List of objects of type mrGraphicsObject
        '''
        if type(data) == list:
            # clear drawn objects
            self._clearObjects()
                        
            # draw objects
            for obj in data:
                self._updateObj(obj)
                
            return True
        
        return False
            
            