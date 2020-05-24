import pymysql

connWXdst = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='NWPO3_Weather')

curDestination = connWXdst.cursor()

class GetWX():
    
    def getDays(self, month):
        if month in [2]:
            days = 28
        elif month in [4, 6, 9, 11, 12]:
            days = 30
        else:
            days = 31
        return days
    
    def getTemp(self, year, month):
        sql = "select format(avg(Temperature), 2) from `Combined` WHERE Year(TimePST) = " + year + " AND Month(TimePST) = " + month
        curDestination.execute(sql)
        ave_temp = curDestination.fetchone()
        return str(ave_temp[0])
    
    def getWind(self, year, month):
        sql = "select format(avg(WindSpeed), 2) from `Combined` WHERE Year(TimePST) = " + year + " AND Month(TimePST) = " + month
        curDestination.execute(sql)
        ave_wind = curDestination.fetchone()
        #ave_wind = ave_wind[0]
        return ave_wind[0]
    
    def getGust(self, year, month):
        sql = "select format(max(Gust), 2), ANY_VALUE(TimePST) from `Combined` WHERE Year(TimePST) = " + year + " AND Month(TimePST) = " + month + " Group By Gust Order By Gust DESC Limit 1"
        curDestination.execute(sql)
        gust = curDestination.fetchone()
        if gust in [None, 'None']:
            gust = ['0.00', '1000-01-01 00:00:00']
        #print gust
        #print gust[0], gust[1]
        return gust[0], gust[1]
    
    def getWindrun(self, year, month):
        days =  str(GetWX.getDays(self, month))
        sql = "select format((sum(WindSpeed) / count(WindSpeed)) * 24 * " + str(days) + ", 2) from `Combined` WHERE Year(TimePST) = " + year + " AND Month(TimePST) = " + month
        curDestination.execute(sql)
        windrun = curDestination.fetchone()
        windrun = windrun[0]
        return windrun
    
    def getMaxTemp(self, year, month):
        sql = "select format(max(Temperature), 2) from `Combined` WHERE Year = " + year + " AND Month = " + month
        #print sql
        curDestination.execute(sql)
        max_temp = curDestination.fetchone()
        return str(max_temp[0])
    
    def getMinTemp(self, year, month):
        sql = "select format(min(Temperature), 2) from `Combined` WHERE Year = " + year + " AND Month = " + month + " And Temperature > 0"
        #print sql
        curDestination.execute(sql)
        max_temp = curDestination.fetchone()
        return str(max_temp[0])    
    
    def getMaxBP(self, year, month):
        sql = "select format(max(Barometer), 2) from `Combined` WHERE Barometer <> 295.27 And Year = " + year + " AND Month = " + month
        curDestination.execute(sql)
        max_bp = curDestination.fetchone()
        #ave_wind = ave_wind[0]
        return max_bp[0]    
    
    def getMinBP(self, year, month):
        sql = "select format(min(Barometer), 2) from `Combined` WHERE Barometer <> 295.27 And Year = " + year + " AND Month = " + month
        curDestination.execute(sql)
        min_bp = curDestination.fetchone()
        #ave_wind = ave_wind[0]
        return min_bp[0]        
       
           
