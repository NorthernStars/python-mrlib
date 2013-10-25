'''
Created on 25.10.2013

@author: northernstars
'''
from kivy.uix.widget import Widget

class AbstractGraphicsSzenario(Widget):
    '''
    Abstract class for creating a szenario
    1. To create szenario create subclass of this one.
       Create a constructor grabbing a widget as
       parameter and calling this superclass constructor.
    2. Override drawGui function to recieve vision
       data and create gui on this class.
    '''
        
    def drawGui(self, data=None):
        '''
        Recives vision data and maniupulates widget
        @param data: mrVisionData object
        '''
        pass