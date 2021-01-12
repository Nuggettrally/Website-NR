#!/usr/bin/env python3

import cgi
import pymysql
#import mysql.connector
#import MySQLdb

def main(): # NEW except for the call to processInput
    # Open database connection
    db = pymysql.connect("localhost","root","su8a&4ru","rally" )
    #db = mysql.connector.connect("localhost","dave","su8a&4ru","rally" )
    #db = MySQLdb.connect("localhost","dave","su8a&4ru","rally" )

    # prepare a cursor object using cursor() method
    cur = db.cursor()

    # execute SQL query using execute() method.
    cur.execute("SELECT VERSION()")

    # Fetch a single row using fetchone() method.
    verdata = cur.fetchone()
    #print ("Database version : %s " % data)

    # disconnect from server
    contents = processInput(verdata)   # process input into a page
    print(contents)
    db.close()
    
def processInput(verdata):  
    '''Process input parameters and return the final page as a string.'''
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


