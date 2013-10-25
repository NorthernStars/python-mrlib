'''
Created on 25.10.2013

@author: northernstars
'''
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, Line, Ellipse
from kivy.graphics.context_instructions import PushMatrix, PopMatrix, Rotate

from mrLib.networking.data.mrVisionData import mrVisionObject
from mrLib.networking.data.mrVisionData import VISION_OBJ_BOT, VISION_OBJ_RECT, VISION_OBJ_LINE, VISION_OBJ_DOT, VISION_OBJ_CIRCLE, VISION_OBJ_TEXT

class AbstractGraphicsSzenario(Widget):
    '''
    Abstract class for creating a szenario
    1. To create szenario create subclass of this one.
       Create a constructor grabbing a widget as
       parameter and calling this superclass constructor.
    2. Override drawGui function to recieve vision
       data and create gui on this class.
    '''
    _guiObjs = {}
    
    def _updateObj(self, obj=mrVisionObject()):
        '''
        Updates a object if object already on widget.
        Otherwise it will create a object
        Override this function to create your own
        apperance of ojects
        '''
        assert isinstance(obj, mrVisionObject)

        # get obj attributes
        typ = obj.getType()
        bid = obj.getID()
        name = obj.getName()
        loc = obj.getLocation()
        angle = obj.getAngle()
        radius = obj.getRadius()
        size = obj.getSize()
        color = obj.getColor()
        objname = str(bid)+":"+name
        text = obj.getText()
        
        # get object from widget children or canvas or None if not found
        wObj = self._getObjFromWidget(obj)
        update = False
        if wObj != None:
            update = True
        
        # draw objects
        with self.canvas:
            # set color
            Color( color[0], color[1], color[2], color[3] )
            
            if typ == VISION_OBJ_BOT:
                # draw bot
                pos = ( loc[0]-radius, loc[1]-radius  )
                size = (5,5)
                if update:
                    # update object
                    assert isinstance(wObj, Widget)
                    if type(wObj) == Widget:
                        wObj.canvas.clear()
                else:
                    # draw new object
                    wObj = Widget( pos=pos )
                    lbl = Label( text="  "+objname, pos=wObj.pos )
                    lbl.texture_update()
                    tsize = lbl.texture.size
                    lbl.size = (tsize[0], tsize[1])
                    wObj.add_widget( lbl )
                
                # draw dot
                if type(wObj) == Widget:                        
                    with wObj.canvas:
                        Color( color[0], color[1], color[2], color[3] )
                        Ellipse( pos=pos, size=size  )
            
            if typ == VISION_OBJ_RECT:
                # draw rectangle
                pos = ( loc[0]-size[0]/2, loc[1]-size[1]/2 )
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
                        
                    
                    
            
            if typ == VISION_OBJ_LINE:
                #draw line
                points = loc              
                if update:
                    # update object
                    assert isinstance(wObj, Line)
                    wObj.points = points
                    wObj.width = radius
                else:
                    # draw new object
                    wObj = Line( points=points, width=radius )
            
            if typ == VISION_OBJ_DOT:
                #draw dot
                pos = ( loc[0]-radius/2, loc[1]-radius/2  )                
                size = (radius, radius)
                if update:
                    # update object
                    assert isinstance(wObj, Ellipse)
                    wObj.pos = pos
                    wObj.size = size
                else:
                    # draw new object        
                    wObj = Ellipse( pos=pos, size=size  )
            
            if typ == VISION_OBJ_CIRCLE:
                #draw cricle
                if update:
                    # update object
                    assert isinstance(wObj, Line)                
                    wObj.circle = (loc[0], loc[1], radius)
                else:
                    # draw new object
                    wObj = Line( circle=(loc[0], loc[1], radius) )
                    
            if typ == VISION_OBJ_TEXT:
                #draw cricle
                if update:
                    # update object
                    assert isinstance(wObj, Label)                
                    wObj.text = text
                else:
                    # draw new object
                    padding = 5
                    wObj = Label( text=text, pos=loc, markup=True )
                    wObj.texture_update()
                    size = wObj.texture.size
                    wObj.size = (size[0]+2*padding, size[1]+2*padding)
                    
                    with wObj.canvas.before:
                        PushMatrix()
                        Rotate( angle=angle, axis=(0,0,1), origin=(loc[0], loc[1], 0) )                        
                    with wObj.canvas.after:
                        PopMatrix()
                    
                    with wObj.canvas.before:
                        Color(1,1,1,0.1)
                        Rectangle( pos=wObj.pos, size=wObj.size)
        
        # check if to add new object
        if not update and wObj != None:    
            self._guiObjs[objname] = wObj
            
        # send update request to canvas
        self.canvas.ask_update()
        
        
    def _getObjFromWidget(self, obj=mrVisionObject()):
        '''
        Searches for a object in object list
        and returns it.
        If no object can be found it returns None
        @param obj: mrVisionObject to search for
        @return: Widget object or None
        '''
        assert isinstance(obj, mrVisionObject)
        objname = str(obj.getID())+":"+obj.getName()
        
        for key in self._guiObjs.keys():
            if key == objname:
                # found object
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
            if obj in self.canvas.children:
                self.canvas.remove(obj)
            obj = None
            
        self.__drawCounts = 0
        self._guiObjs = {}
            
        
    def drawGui(self, data=None):
        '''
        Recives vision data and maniupulates widget
        @param data: mrVisionData object
        '''
        if type(data) == list:
            # clear drawn objects
            self._clearObjects()
        
            self.__drawCounts += 1
                        
            # draw objects
            for obj in data:
                self._updateObj(obj)
            
            