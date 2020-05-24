import pymysql, string, sys, decimal

connWXdst = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='NWPO3_Weather')

curDestination = connWXdst.cursor()

months = ['1', '2','3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
#months = ['7', '8', '9', '10', '11', '12']

#years = ['1985', '1986', '1987', '1988', '1989']
#years = ['1990', '1991', '1992', '1993', '1994']
#years = ['1995','1996', '1997', '1998', '1999']
#years = ['2000', '2001', '2002', '2003', '2004','2005']
#years = ['2006', '2007', '2008', '2009', '2010', '2011']
#years = ['2012', '2013', '2014', '2015', '2016', '2017']
years = ['2017']

def getDays(month):
    if month in [2]:
        days = 28
    elif month in [4, 6, 9, 11, 12]:
        days = 30
    else:
        days = 31
    return days

def getTemp(year, month):
    sql = "select format(avg(Temperature), 2) from `Combined` WHERE Year(TimePST) = " + year + " AND Month(TimePST) = " + month
    curDestination.execute(sql)
    ave_temp = curDestination.fetchone()
    #print ave_temp
    return ave_temp

def getWind(year, month):
    sql = "select format(avg(WindSpeed), 2) from `Combined` WHERE Year(TimePST) = " + year + " AND Month(TimePST) = " + month
    curDestination.execute(sql)
    ave_wind = curDestination.fetchone()
    return ave_wind

def getGust(year, month):
    sql = "select format(max(Gust), 2) from `Combined` WHERE Year(TimePST) = " + year + " AND Month(TimePST) = " + month
    curDestination.execute(sql)
    gust = curDestination.fetchone()
    return gust

def getWindrun(year, month):
    days =  str(getDays(month))
    sql = "select format((sum(WindSpeed) / count(WindSpeed)) * 24 * " + str(days) + ", 2) from `Combined` WHERE Year(TimePST) = " + year + " AND Month(TimePST) = " + month
    #print sql
    curDestination.execute(sql)
    windrun = curDestination.fetchone()
    return windrun

#def getRain(year, month):
    #sql = "select format(sum(TotRN_5), 2) from `Combined_copy` WHERE YEAR = " + year + " AND MONTH = " + month
    #curDestination.execute(sql)
    #tot_rain = curDestination.fetchone()
    #return tot_rain




def main():
    dataWX = []
    #years = sys.argv[1]
    #for year in range(2009, 2009):
    for year in years:
        print('\n')
        print(year)
        print("Month  Ave. Temp. Ave. Wind  Max Gust Wind Run")
        print("        Deg. (F)     MPH       MPH     Miles")
        print ''
        for month in months:
            #print month
            #tp = decimal.Decimal(getTemp(year, month)[0].quantize(decimal.Decimal('.01')))
            tp = getTemp(year, month)[0]
            #print tp
            #tp = decimal.Decimal(str(tp)).quantize(decimal.Decimal('.01'))
            #print tp
            ws = float(getWind(year, month)[0])
            ws = str(ws)
            ws = ws.split('.')
            if len(ws[1]) == 1:
                ws = str(ws[0]) + '.' + str(ws[1]) + '0'
            else:
                ws = str(ws[0]) + '.' + str(ws[1])
            wr = getWindrun(year, month)[0]            
            wg = float(getGust(year, month)[0])
            wg = str(wg)
            wg = wg.split('.')
            if len(wg[1]) == 1:
                wg = str(wg[0]) + '.' + str(wg[1]) + '0'
            else:
                wg = str(wg[0]) + '.' + str(wg[1])
            wr = getWindrun(year, month)[0]
            #print wr
            #rn = float(getRain(year, month)[0])
            #rn = str(rn)
            #rn = rn.split('.')
            #if len(rn[1]) ==1:
                #rn = str(rn[0]) + '.' + str(rn[1]) + '0'
            #else:
                #rn = str(rn[0]) + '.' + str(rn[1])            
            print "%3s %2s %7s %4s %5s %3s %4s %1s %9s %2s" %(month, "|", tp, "|", ws, "|", wg, "|", wr,"|")
            
            

if __name__ == "__main__":
    sys.exit(main())
    
    
    

    ##print(year)
    ##print("Month  Ave. Temp. Ave. Wind  Max Gust Wind Run Total Rain")
    ###print("        Deg. (F)      MPH      MPH      Miles     in.")
    ##print(month, "Deg. (F)      MPH      MPH      Miles     in.")
    ## create funtion for each item as query works on entire dataset            
    #sql = "select avg(AvgAT) , avg(AWS) , max(gust), sum(TotRN_5), year, month from Combined_copy where year = " + str(year) + " And month = " + str(month)
    ##print sql
    #curDestination.execute(sql)
    ##rows = curDestination.fetchall()
    #rows = curDestination.fetchone()
    #for row in rows:
        #dataWX.append(row)
    ##dataWX.append(row)
    ##for i in range(0, len(dataWX)):
    #i = 0
    #tp = dataWX[0]
    #ws = dataWX[1]
    #wg = dataWX[2]
    #rn = dataWX[3]
    #yr = dataWX[4]
    ##print yr
    #mo = dataWX[5]
    #wr = getWindrun(yr, mo)
    #wr = wr[0]
    ##print mo, "-", yr
    ##print "Temp: " + str(tp) + "Wind: " + str(ws) + "Gust: " + str(wg) + "Rain: " + str(rn)
            #print "%3s %2s %5d %5s %5d %4s %4d %3s %5d %2s %4d %5s" %(mo, "|", tp, "|", ws, "|", wg, "|", wr, "|", rn, "|")
