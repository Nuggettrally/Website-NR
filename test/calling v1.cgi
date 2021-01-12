#!/usr/bin/env python3

import cgi
import urllib
import os

def main():
    callingURL = os.environ["HTTP_HOST"] # get the url
    contents = processInput(callingURL)   # process input into a page
    print(contents)
    
def processInput(callingURL):  
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


