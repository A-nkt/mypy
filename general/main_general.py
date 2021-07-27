from general_core import * 

def integerchecker(x):
  return IntegerChecker(x)

def countdays(year,month):
  return CountDays(year,month)

def month1to13(month):
  return Month1to13(month)

def xlist(interval=1,syr=2000,fyr=2020,month=True,v_month=1):
  return XList(sep=interval,syr=syr,fyr=fyr,monthTF=month,vmonth=v_month)

def make_date(df,syr=2001,fyr=2019):
  return Make_Date(df,syr=syr,fyr=fyr)

class Basic():
  def monthlist(self):
    monthlist = ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec"]
    return monthlist
