import pymysql, string, sys, decimal

sys.path.insert(0, '/Users/Neal/Documents/WeatherData/NWPO3H')

import GetWX_nwpo3h

months = ['1', '2','3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
month_names = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
years = ['1985', '1986', '1987', '1988', '1989', 
         '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999',
         '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
         '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']    
#types = ['getTemp', 'getWind', 'getGust', 'getWindrun']
#print_types = {'getTemp':'Average Temperature - Degrees Fahrenheit', 'getWind':'Average Wind Speed - MPH', 'getGust':'Maximum Wind Gust - MPH', 'getWindrun': 'Wind Run - Miles ((ave. wind speed * 24) * <no. days in mo.>)'}

types = ['getMaxTemp', 'getMinTemp', 'getMaxBP', 'getMinBP']
print_types = {'getMaxTemp':'Max Temperature - Degrees Fahrenheit', 'getMinTemp':'Min Temperature - Degrees Fahrenheit', 'getMaxBP':'Max Barometer - Inches Hg', 'getMinBP':'Max Barometer - Inches Hg'}

dataWX = []
spacer = '      '

reports = GetWX_nwpo3h.GetWX()

for type in types:
    print '\n'
    print print_types[type]
    print_months = '{0:^8s} {1:^12s} {2:^12s} {3:^12s} {4:^12s} {5:^12s} {6:^12s} {7:^12s} {8:^12s} {9:^12s} {10:^12s} {11:^12s} {12:^12s}'.format(spacer, 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    print print_months
    for year in years:
        if int(year)%10 == 0:
            print print_months
        values = []
        for month in months:
            run = 'reports.' + type + '(year, month)'
            tp = eval(run)            
            values.append(str(tp))
        print '{0:6s} {1:>12s} {2:>12s} {3:>12s} {4:>12s} {5:>12s} {6:>12s} {7:>12s} {8:>12s} {9:>12s} {10:>12s} {11:>12s} {12:>12s}' .format(year, values[0], values[1], values[2], values[3], values[4], values[5],values[6], values[7], values[8],values[9], values[10], values[11])
