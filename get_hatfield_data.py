#get data files from HMSC weather site, write to local file and format for mysql insert

import urllib2, csv, subprocess, sys, os

years = sys.argv[1]
#print years

baseurl = "http://weather.hmsc.oregonstate.edu/weather/weatherproject/archive/" + str(years) + "/HMSC_"
basepath = "/Users/Neal/Documents/WeatherData/HMSC/" + years + "/"
#print baseurl
#print basepath

#years = ["2015", "2016", "2017"]
#years = ["2015"]
months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
#months = ["07", "08", "09", "10", "11", "12"]

header = '"DT","RD","WS","WD","SIG","WG","AvgAT","MaxAT","MinAT","AvgRH","AvgBP","TotRN","DailyRN","Batt",\n'

lines = []
weather_data = []

#for year in years:
for month in months:
    year = years
    #target = year + month
    targetfile = baseurl + year + month + ".dat"
    writefile = basepath + year + month + ".dat"
    print targetfile
    print writefile
    csvfile = open(writefile, 'w')
    #print header
    weatherwriter = csv.writer(csvfile, quoting = csv.QUOTE_NONE)
    csvfile.write(header)
    data = urllib2.urlopen(targetfile)
    for line in data:
        #print line
        lines.append(line)
        testline = line[1:5]
        #don't write original headers 
        if testline == year:
            # print testline
            csvfile.write(line)
    csvfile.close()
    #cleanup remove stray CR/LF
    subprocess.call(["dos2unix", writefile])
    #add CR/LF for csv import to mysql
    subprocess.call(["unix2dos", writefile])
            
                
            