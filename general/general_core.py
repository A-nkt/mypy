import numpy as np


def IntegerChecker(x):
    x=int(x)
    if x<=9:
        x="0"+str(x)
    else:
        x=str(x)
    return x


def CountDays(year,month):
    year_4=int(20+int(year))
    month=int(month)
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        days=31
    elif month==4 or month==6 or month==9 or month==11:
        days=30
    elif month==2:
        if year_4%4==0:
            days=29
        elif year_4%4!=0:
            days=28    
    return str(days)

def Month1to13(month):
    month=int(month)
    if month==13:
        month=1
    else:
        pass
    return month    

def XList(sep=1,syr=2001,fyr=2020,monthTF=True,vmonth=1):
  """
  Parameters
  ----------
  sep : int
    interval year
  syr : int
    start year
  fyr : int
    final year
  monthTF : bool
    use month or not
  vmonth : int
    use month

  Returns
  ----------
  x_index : list
    date list
  """
  x_index = []
  year_list = list(np.arange(syr,fyr,1))
  for inx,year in enumerate(year_list):
    if inx%sep == 0:
      if monthTF == True:
        for month in range(1,13,1):
          if month == vmonth:
            x_index.append(str(year)+"/"+IntegerChecker(month))
      else:
        x_index.append(str(year))
    else:
      x_index.append("")
  return x_index

def Make_Date(df,syr=2001,fyr=2019):
  """
  parameter 
  --------
  df : DataFrame
  syr : int
  fyr : int
  """
  i = 0
  for yr in range(syr,fyr,1):
    for mn in range(1,13,1):
      df.loc[i,"date"] = str(yr)+"/"+IntegerChecker(mn)
      i += 1
  return df

