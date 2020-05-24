#class reports_mwpo3h():

    #def getDays(self, month):
        #if month in [2]:
            #days = 28
        #elif month in [4, 6, 9, 11, 12]:
            #days = 30
        #else:
            #days = 31
        #return days
    
    #def getTemp(self, year, month):
        #sql = "select format(avg(Temperature), 2) from `Combined` WHERE Year(TimePST) = " + year + " AND Month(TimePST) = " + month
        #curDestination.execute(sql)
        #ave_temp = curDestination.fetchone()
        #return str(ave_temp[0])
    
    #def getWind(self, year, month):
        #sql = "select format(avg(WindSpeed), 2) from `Combined` WHERE Year(TimePST) = " + year + " AND Month(TimePST) = " + month
        #curDestination.execute(sql)
        #ave_wind = curDestination.fetchone()
        #ave_wind = ave_wind[0]
        #return ave_wind
    
    #def getGust(self, year, month):
        #sql = "select format(max(Gust), 2) from `Combined` WHERE Year(TimePST) = " + year + " AND Month(TimePST) = " + month
        #curDestination.execute(sql)
        #gust = curDestination.fetchone()
        #return gust[0]
    
    #def getWindrun(self, year, month):
        #days =  str(reports.getDays(month))
        #sql = "select format((sum(WindSpeed) / count(WindSpeed)) * 24 * " + str(days) + ", 2) from `Combined` WHERE Year(TimePST) = " + year + " AND Month(TimePST) = " + month
        #curDestination.execute(sql)
        #windrun = curDestination.fetchone()
        #windrun = windrun[0]
        #return windrun
    
import pymysql, string, sys, decimal

connWXdst = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='NWPO3_Weather')

curDestination = connWXdst.cursor()    
   
months = ['1', '2','3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
month_names = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
years = ['1985', '1986', '1987', '1988', '1989', 
         '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999',
         '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
         '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']    
types = ['getTemp', 'getWind', 'getGust', 'getWindrun']
print_types = {'getTemp':'Average Temperature - Degrees Fahrenheit', 'getWind':'Average Wind Speed - MPH', 'getGust':'Maximum Wind Gust - MPH', 'getWindrun': 'Wind Run - Miles'}
dataWX = []
spacer = '      '

reports = reports_mwpo3h()


for type in types:
    print print_types[type]
    print_months = '{0:^8s} {1:^12s} {2:^12s} {3:^12s} {4:^12s} {5:^12s} {6:^12s} {7:^12s} {8:^12s} {9:^12s} {10:^12s} {11:^12s} {12:^12s}'.format(spacer, 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    print print_months
    for year in years:
        if int(year)%10 == 0:
            print print_months
        values = []
        for month in months:
            #print(year, month)
            run = 'reports.' + type + '(year, month)'
            #print(run)
            tp = eval(run)            
            #tp = reports.getWindrun(year, month)
            #print tp[0]
            values.append(str(tp))
        #print '{0:6s} {1:6s} {2:6s} {3:6s} {4:6s} {5:6s} {6:6s} {7:6s} {8:6s} {9:6s} {10:6s} {11:6s} {12:6s}' .format(year, values[0], values[1], values[2], values[3], values[4], values[5],values[6], values[7], values[8],values[9], values[10], values[11])
        print '{0:6s} {1:>12s} {2:>12s} {3:>12s} {4:>12s} {5:>12s} {6:>12s} {7:>12s} {8:>12s} {9:>12s} {10:>12s} {11:>12s} {12:>12s}' .format(year, values[0], values[1], values[2], values[3], values[4], values[5],values[6], values[7], values[8],values[9], values[10], values[11])
        #line = str(year)
        #for i in range(0, 11):
            #line = line + str(values[i])
        #print line
       
           
