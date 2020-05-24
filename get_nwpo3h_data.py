#get data files from HMSC weather site, write to local file and format for mysql insert

import urllib2, csv, subprocess, sys, os, pymysql, time
from datetime import datetime
#years = [1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
years = [2012]

months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

connWXdst = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='NWPO3_Weather')
curDestination = connWXdst.cursor()

time.strftime('%Y-%m-%d %H:%M:%S')

def utc2local (utc):
    epoch = time.mktime(utc.timetuple())
    offset = datetime.fromtimestamp (epoch) - datetime.utcfromtimestamp (epoch)
    return utc + offset
def testforzero(line):
    line = line.split('.')
    print len(line)

for year in years:
    print year
    baseurl = "http://www.ndbc.noaa.gov/view_text_file.php?filename=nwpo3h" + str(year) + ".txt.gz&dir=data/historical/stdmet/"
    basepath = "/Users/Neal/Documents/WeatherData/NWPO3H/" + str(year) + "/" 
    if not os.path.exists(basepath):
        os.mkdir(basepath)
    targetfile = baseurl
    data = urllib2.urlopen(targetfile)
    for line in data:
        lines = []
        formatline = []
        formatlines = []
        #print line
        testline = line[0:2]
        #print testline
        testyear = str(year)[2:4]
        #print testyear
        #don't write headers 
        if testline <> 'YY':
            if testline in ['85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99']:
                millennium = '19'
            else: 
                millennium = '20'
            #for two digit year 
            #UTC_Year = millennium + testline
            #for four digit year
            UTC_Year = year
            inline = line.replace(' ', ',')
            nline = inline.replace(' ', '\n')
            sline = nline.split(',')
            lines.append(sline)
            #rebuild line without blank values
            for i in range(0, len(lines[0])):
                if lines[0][i] <> '':
                    #print(i, lines[0][i])
                    formatline.append(lines[0][i])
            formatlines.append(formatline)
            #look for headers 
            #print formatlines[0][0]
            if formatlines[0][0] not in ('#YY', '#yr'):
                #print formatlines
                YY = testyear
                YY = int(YY)
                MM = int(formatlines[0][1])
                DD = int(formatlines[0][2])           
                hh = (formatlines[0][3])
                UTC = str(UTC_Year) + '-' + str(MM) + '-' + str(DD) + ' ' + str(hh) + ':00:00'
                UTC = datetime.strptime(UTC, '%Y-%m-%d %H:%M:%S')
                timelocal = utc2local(UTC)
                timelocal = str(timelocal)
                WD = int(formatlines[0][5])
                WSPD = float((formatlines[0][6]))*(25/11)
                GST = float((formatlines[0][7]))*(25/11)
                BAR = float((formatlines[0][12]))*0.029529983071445
                ATMP = (float((formatlines[0][13]))*1.8) + 32                  
                sql = "INSERT INTO Combined (TimePST, Year, Month, Day, Hour, WindDirection, WindSpeed, Gust, Barometer, Temperature) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                #print(timelocal, YY, MM, DD, hh, WD, WSPD, GST, BAR, ATMP)         
                try:
                    curDestination.execute(sql, (timelocal, YY, MM, DD, hh, WD, WSPD, GST, BAR, ATMP))
                except pymysql.err.DataError:
                    print "execpt ", formatline
                    ATMP = (float((formatlines[0][12]))*1.8) + 32                


curDestination.close()
connWXdst.commit()
print "Commit"
connWXdst.close()


            
                
            