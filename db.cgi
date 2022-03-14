#!/usr/bin/env python3

import cgi
import pymysql
import pymysql.cursors

def main(): # NEW except for the call to processInput
    pymysql.install_as_MySQLdb()
    # Open database connection
    db = pymysql.connect(
        host = '192.168.0.120', 
        user = 'dave', 
        passwd = 'm1nIcO0p3rS', 
        db = 'rally', 
        port = 3307)
    verdata = "In Main Module"
    try:
        # prepare a cursor object using cursor() method
        cur = db.cursor()

        # execute SQL query using execute() method.
        #cur.execute("SELECT VERSION()")
        #verdata = "Version Executed"
        sql = '''CREATE TABLE testdetails (
               car_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
               activityother VARCHAR(100) NULL,
               amountpaid FLOAT UNSIGNED NOT NULL,
               camslicno INT UNSIGNED NULL,
               driverdpi FLOAT NULL,
               eventauth VARCHAR(10) NOT NULL DEFAULT "CAMS",
               eventnumbstages SMALLINT UNSIGNED NULL,
               eventseriesyr SMALLINT UNSIGNED NOT NULL,
               firstname VARCHAR(30) NOT NULL,
               radiotimept FLOAT UNSIGNED NULL,
               sectionlength MEDIUMINT UNSIGNED NOT NULL,
               state VARCHAR(3) NULL DEFAULT 'SA',
               chgdate TIMESTAMP NOT NULL,
               aasaliexp DATE NULL,
               daterenewed DATE NOT NULL,
               firstcardue TIME NULL,
               sectiontime TIME NOT NULL,
               activityhistvehicle ENUM('Y', 'N') NULL DEFAULT 'Y',
               drvnwheels ENUM('FWD', 'RWD', '4WD') NULL,
               emailvalid ENUM('Y', 'N') NOT NULL,
               jumpstart ENUM('Y', 'N') NULL,
               membermag ENUM('E', 'P', 'N') NOT NULL,
               membertype ENUM('F', 'S', 'J') NOT NULL,
               paymenttype ENUM('Csh', 'Chq', 'EFT', 'M/O') NOT NULL,
               sectiontype ENUM('Special Stage', 'Liaison', 'Road Section', 'Service', 'Regroup', 'Section', 'Division') NOT NULL,
               sex ENUM('M', 'F') NULL,
               eventnoheats SMALLINT UNSIGNED NOT NULL DEFAULT 1
               )'''
        cur.execute(sql)
        # Fetch a single row using fetchone() method.
        #verdata = cur.fetchone()
        # SQL query string
        sqlQuery = '''show tables'''   
        # Execute the sqlQuery
        verdata = cur.execute(sqlQuery)
    except Exception as e:

        verdata = e

    # disconnect from server
    db.close()
    contents = processInput(verdata)   # process input into a page
    print(contents)
    
def processInput(verdata):  
    '''Process input parameters and return the final page as a string.'''
    progress = verdata # transform input to output data
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


