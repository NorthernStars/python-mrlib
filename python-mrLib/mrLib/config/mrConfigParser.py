'''
Created on 11.09.2013

@author: hannes
'''
from ConfigParser import ConfigParser
from os.path import isfile

class mrConfigParser(object):
    '''
    Class to parse config file
    '''
    __config = ConfigParser()
    __cfgFile = "config.ini"

    def __init__(self, cfgFile="config.ini"):
        '''
        Constructor
        @param cfgFile: Filepath of config file
        '''
        self.__config = ConfigParser()
        
        # check if file exsists
        if isfile(cfgFile):
            self.__config.read(cfgFile)
            self.__cfgFile = cfgFile
        
    def getSections(self):
        '''
        Returns list of section names
        '''
        return self.__config.sections()
    
    def getOptions(self, section):
        '''
        Returns list of options in a section
        '''
        if self.__config.has_section(section):
            return self.__config.options(section)
        return None
    
    def getConfigValue(self, section, option):
        '''
        Returns a config value of a option inside a section
        '''
        if self.__config.has_option(section, option):
            return self.__config.get(section, option)
        return None
    
    def getConfigValueBool(self, section, option):
        '''
        Returns a boolean config value of a option inside a section
        '''
        if self.__config.has_option(section, option):
            return self.__config.getboolean(section, option)
        return None
    
    def getConfigValueInt(self, section, option):
        '''
        Returns a integer config value of a option inside a section
        '''
        if self.__config.has_option(section, option):
            return self.__config.getint(section, option)
        return None
    
    def getConfigValueFloat(self, section, option):
        '''
        Returns a float config value of a option inside a section
        '''
        if self.__config.has_option(section, option):
            return self.__config.getfloat(section, option)
        return None
    
    def setConfigValue(self, section, option, value):
        '''
        Sets a config Value
        '''
        self.__config.set(section, option, value)
        
    def saveConfig(self, cfgFile=None):
        '''
        Saves config to file.
        @param cfgFile: Filepath of config file.
        If filepath is None or omitted, config is saved
        to filepath used at initiation  
        '''
        if cfgFile == None:
            cfgFile = self.__cfgFile
            
        fp = open( cfgFile, 'w' )
        self.__config.write( fp )
        fp.close()