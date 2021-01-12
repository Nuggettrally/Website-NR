#!/usr/bin/env python3

import cgi
import urllib
import webbrowser
import os
import cgitb

def main():
    cgitb.enable()
    callingURL = os.environ["HTTP_HOST"] # get the url
    #callingURL = 'www.rudhamlawyers.com.au' # get the url
    #showURL('//' + callingURL)
    #callingURL = 'www.nuggettrally.com.au' # get the url
    #showURL('//' + callingURL)
    #callingURL = 'www.nuggettrally.com' # get the url
    #showURL('//' + callingURL)
    #callingURL = 'nuggettrally.com.au' # get the url
    #showURL(callingURL)
    #showURL('//' + callingURL)
    #callingURL = 'nuggettrally.com' # get the url
    #showURL(callingURL)
    #showURL('//' + callingURL)
    # useURL = callingURL + '/nr/'
    useURL = showURL('//' + callingURL)
    #redirectURL = showURL('//' + callingURL)
    #urllib.request.request(useURL)
    #urllib.request.urlopen(useURL)
    #urllib.urlopen(useURL).read()
    #contents = processInput(redirectURL)   # process input into a page
    contents = processInput(useURL)   # process input into a page
    print(contents)
    #print('<html>')
    #print('  <head>')
    #print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 
    #print('  </head>')
    #print('</html>')
    webbrowser.open_new_tab(useURL)
    
def showURL(chkURL):
    s = urllib.parse.urlsplit(chkURL)
    if "rudhamlawyers" in s.netloc:
        newpath = "/rl/"
    else:
        newpath = "/nr/"
    #tmpURL = ('http', s.netloc, newpath, '', '')
    newURL = urllib.parse.urlunsplit(('http', s.netloc, newpath, '', ''))
    return(newURL)
        
    
def processInput(useURL):  
    '''Process input parameters and return the final page as a string.'''
    return fileToStr('callingTemplate.html').format(**locals())

# standard code for future cgi scripts from here on
def fileToStr(fileName): 
    """Return a string containing the contents of the named file."""
    fin = open(fileName); 
    contents = fin.read();  
    fin.close() 
    return contents

try:
    print("Content-type: text/html\n\n")   # say generating html
    main() 
except:
    cgi.print_exception()                 # catch and print errors


