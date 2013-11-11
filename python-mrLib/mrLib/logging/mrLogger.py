'''
Created on 12.09.2013

@author: hannes
'''
from time import strftime
from os import remove
from os.path import isfile

LOG_LEVEL = {"debug": 0,
             "info": 1,
             "default": 2,
             "error": 3}
LOG_LEVEL_COLOR = {"error": "#ff8585",
                   "default": "#eeeeee",
                   "info": "#e6f1ff",
                   "debug": "#ffcc88" }

LOGGER_LOG_FILE = "logger.log"
LOGGER_LOG_HTML_FILE = "logger.html"
LOGGER_LOG_LEVEL = LOG_LEVEL["default"]
LOGGER_LOG_TO_FILE = True
LOGGER_LOG_TO_HTML_FILE = True

def __getLogColor(level=LOG_LEVEL['default']):
    '''
    Returns color of log level
    '''
    key = LOG_LEVEL['default']
    
    # search for key name
    for key in LOG_LEVEL.keys():
        if LOG_LEVEL[key] == level:
            break;
    
    if key in LOG_LEVEL_COLOR:
        return str( LOG_LEVEL_COLOR[key] )
    return str( LOG_LEVEL_COLOR['default'] )

def logInfo(msg=""):
    '''
    Logs a message as info
    '''
    log(msg, LOG_LEVEL["info"])
    
def logDebug(msg=""):
    '''
    Logs a message as debug
    '''
    log(msg, LOG_LEVEL["debug"])
    
def logError(msg=""):
    '''
    Logs a message as error
    '''
    log(msg, LOG_LEVEL["error"])

def log(msg="", level=LOG_LEVEL["default"]):
    '''
    Logs a message
    '''
    if level >= LOGGER_LOG_LEVEL:
        if LOGGER_LOG_TO_FILE:
            if LOGGER_LOG_TO_HTML_FILE:
                logToHtmlFile(msg, level)
            else:
                logToLogFile(msg, level)
        else:
            logToScreen(msg, level)
    
    
def logToLogFile(msg="", level=LOG_LEVEL["default"]):
    '''
    Logs message to log file
    '''
    if level >= LOGGER_LOG_LEVEL:
        txt =  strftime( "%Y/%m/%d - %H:%M:%S" ) + ":\t" + msg + "\n"
        fp = file( LOGGER_LOG_FILE, 'a' )
        fp.write( txt )
        fp.close()
    
def logToHtmlFile(msg="", level=LOG_LEVEL["default"]):
    '''
    Logs message to html file
    '''
    if level >= LOGGER_LOG_LEVEL:
        # create html 
        html = "<div style=\"width: 100%; padding: 2px; margin: 2px; background-color:" 
        html += __getLogColor(level) + "\"><b>"
        html += strftime( "%Y/%m/%d - %H:%M:%S" )
        html += ":</b><span style=\"padding-left: 2%;\">" + str(msg) + "</span></div>"
        
        fp = file( LOGGER_LOG_HTML_FILE, 'a' )
        fp.write( html )
        fp.close()

def logToScreen(msg="", level=LOG_LEVEL["default"]):
    '''
    Logs message to screen
    '''
    if level >= LOGGER_LOG_LEVEL:
        print strftime( "%Y/%m/%d - %H:%M:%S" ), ":\t", msg
        
def logClear():
    '''
    Clears log file
    '''
    if LOGGER_LOG_TO_FILE:
        if LOGGER_LOG_TO_HTML_FILE:
            if isfile( LOGGER_LOG_HTML_FILE ):
                remove( LOGGER_LOG_HTML_FILE )
        else:
            if isfile( LOGGER_LOG_FILE ):
                remove( LOGGER_LOG_FILE )
    
