#!/usr/bin/env python3

import cgi
#import pymysql
#import pymysql.cursors

def main(): # NEW except for the call to processInput
    verdata = "In Main Module"
    #try:
	    #import pymysql
        #pymysql.install_as_MySQLdb()
        #verdata = "Import successful"
    #except ImportError:
        #pass
        #verdata = "Import failed"
    # Open database connection
    #db = pymysql.connect("192.168.0.120","dave","su8a&4ru","rally" )
    #print ("In Main Module")
    #verdata = "In Main Module, post import"
    #db = pymysql.connect(host='localhost',user='root',password='sl1me$b4lL',db='rally',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    # prepare a cursor object using cursor() method
    #print ("Connected to db")
    #verdata = "Connected to db"
    #cur = db.cursor()

    # execute SQL query using execute() method.
    #cur.execute("SELECT VERSION()")
    #print ("Version Executed")
    #verdata = "Version Executed"

    # Fetch a single row using fetchone() method.
    #verdata = cur.fetchone()
    #print ("Database version : %s " % verdata)

    # disconnect from server
    #print ("Closing Database")
    #db.close()
    contents = processInput(verdata)   # process input into a page
    print(contents)
    
def processInput(verdata):  
    '''Process input parameters and return the final page as a string.'''
    progress = int(verdata) # transform input to output data
    #num1 = int(numStr1) # transform input to output data
    #num2 = int(numStr2)
    #total = num1+num2
    return fileToStr('dbTemplate.html').format(**locals())

# standard code for future cgi scripts from here on
def fileToStr(fileName): 
    """Return a string containing the contents of the named file."""
    fin = open(fileName); 
    contents = fin.read();  
    fin.close() 
    return contents

try:   # NEW
    print("Content-type: text/html\n\n")   # say generating html
    main() 
except:
    cgi.print_exception()                 # catch and print errors
    #print("Error")   # say generating html


