import pymysql
from Tkinter import *

connWXdst = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='HMSC_Weather')
curDestination = connWXdst.cursor()

def queryTable():
    print ("Year: %s\nMonth: %s" % (year.get(), month.get()))
    #windrun = sql = "select (sum(AWS) / count(AWS)) * 24 * 30 from `Combined_copy` WHERE YEAR = 2009 AND MONTH = 11"
    print sql#, windrun
    curDestination.execute(sql)
    windrun = curDestination.fetchone()
    rows = curDestination.fetchall()
    print("WR:, %s", windrun)
    dataWX = []
    for row in rows:
        dataWX.append(row)    
    getData(dataWX) 

def getRain():
    sql = "select sum(TotRN_5) from `Combined_copy` WHERE YEAR = " + year.get() + " AND MONTH = " + month.get()
    print sql
    curDestination.execute(sql)
    rain = curDestination.fetchone()
    print(rain)
    text = "Rain: " + str(rain[0]) + '"'
    result.set(text)    
    
def getWindrun():
    days =  getDays(month.get)
    sql = "select (sum(AWS) / count(AWS)) * 24 * " + str(days) + " from `Combined_copy` WHERE YEAR = " + year.get() + " AND MONTH = " + month.get()
    print sql#, windrun
    curDestination.execute(sql)
    windrun = curDestination.fetchone()
    print(windrun)
    text = "Wind Run: {:.2f}" .format(windrun[0])
    text = text + " Miles"
    result.set(text)

def getGust():
    sql = "select max(Gust), TimePST from `Combined_copy` WHERE YEAR = " + year.get() + " AND MONTH = " + month.get()
    print sql
    curDestination.execute(sql)
    gust = curDestination.fetchone()
    print(gust)
    text = "Max getGust: " + str(gust[0]) + "MPH"
    result.set(text)    

def getAll():
    #sql = "select sum(TotRN_5) As '"'Total Rain'"', (sum(AWS) / count(AWS)) * 24 * 30 As '"'Wind Run'"', max(Gust) As '"'Max Gust'"' from `Combined_copy` WHERE YEAR = 2010 AND MONTH = 1"
    sql = "select sum(TotRN_5) As '"'Total Rain'"', (sum(AWS) / count(AWS)) * 24 * 30 As '"'Wind Run'"', max(Gust) As '"'Max Gust'"' from `Combined_copy` WHERE YEAR = " + str(year.get()) + " AND MONTH = " + str(month.get())
    print sql
    curDestination.execute(sql)
    all = curDestination.fetchall()
    print(all)
    rain = str(all[0][0])
    print(rain)
    windrun = "{:.2f}" .format(all[0][1])
    gust = str(all[0][2])
    text = "Rain: " + rain + '"' + " - Wind Run: " + windrun + " Miles" + " - Gust: " + gust + " MPH"
    result.set(text)     
    

def getDays(month):
    if month in [2]:
        days = 28
    elif month in [4, 6, 9, 11, 12]:
        days = 30
    else:
        days = 31
    return days
        

def getData(dataWX):
    #rows = dataWX
    #print(len(dataWX))
    for  x in range(0, len(dataWX)):
        print(dataWX[x])




master = Tk()
var = IntVar()
result = StringVar()
result.set("No Data")   


#MODES = [
    #("Monochrome", "1"),
    #("Grayscale", "L"),
    #("True color", "RGB"),
    #("Color separation", "CMYK"),
#]

#v = StringVar()
#v.set("L") # initialize

#for text, mode in MODES:
    #b = Radiobutton(master, text=text, variable=v, value=mode)
    #print(text, mode)
    #b.pack(anchor=W)


#frame = Frame(width=768, height=576, bg="", colormap="new")
#frame.pack()

#Frame(master, width=1000, height=100, background="bisque")
#Frame(master, width=50, height = 50, background="#b22222")

#frame1.pack(fill=None, expand=False)
#frame2.place(relx=.5, rely=.5, anchor="c")

 
Label(master, text="Year").grid(row=0, column=0)
Label(master, text="Month").grid(row=1,column=0)
Label(master, textvariable=result).grid(row=9)

#year = Entry(master).grid(row=0, column=1)
#month = Entry(master).grid(row=1, column=1)

year = Entry(master)
month = Entry(master)

year.grid(row=0, column=1)
month.grid(row=1, column=1)

#year.grid(row=0, column=1)
#month.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=10, column=0, sticky=W, pady=4)
#Button(master, text='Calc', command=getWindrun, ShowChoice).grid(row=4, column=1, sticky=W, pady=4)

Radiobutton(master, text="Rain", variable=var, value=1,command=getRain).grid(row=5, column=0, sticky=W, pady=4)
Radiobutton(master, text="Wind Run", variable=var, value=2,command=getWindrun).grid(row=6, column=0, sticky=W, pady=4)
Radiobutton(master, text="Wind Gust", variable=var, value=3,command=getGust).grid(row=7, column=0, sticky=W, pady=4)
Radiobutton(master, text="All", variable=var, value=4,command=getAll).grid(row=8, column=0, sticky=W, pady=4)

mainloop()

