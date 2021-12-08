import numpy as np

def countdays(year,month):
    """
    Parameters
    --------
    year : int
      年
    month : int
      月
    """
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

def month1to13(month):
    month=int(month)
    if month==13:
        month=1
    else:
        pass
    return month 

def xlist(interval=1,syr=2000,fyr=2020,month_is=True,v_month=1):
    """
    Parameters
    ----------
    interval : int
      年の間隔
    syr : int
      開始年
    fyr : int
      最後の年
    month_is : bool
      月の表示の有無
    v_month : int
    　表示の月について

    Returns
    ----------
    x_index : list
      データリスト
    """
    x_index = []
    for year in range(syr,fyr,interval):
      if month_is == True:
        for month in range(1,13,1):
          if month == v_month:
            x_index.append(str(year)+"/"+str(month).zfill(2))
      else:
        x_index.append(str(year))
    return x_index

def make_date(df,syr=2001,fyr=2019):
    """
    parameter 
    --------
    df : DataFrame
      対象のデータセット
    syr : int
      開始年
    fyr : int
      終了年
    """
    i = 0
    for yr in range(syr,fyr,1):
        for mn in range(1,13,1):
            df.loc[i,"date"] = str(yr)+"/"+str(mn).zfill(2)
            i += 1
    return df

def make_time_series(df,syr=2001,fyr=2021):
    """
    Parameter
    -------
    df : DataFrame
      input dataframe
    syr : int
      start year
    fyr : int
      finial year

    Returns
    -------
    df : DataFrame
      input dataframe
    """
    i = 0
    for yr in range(syr,fyr,1):
      for mn in range(1,13,1):
        df.loc[i,'time'] = yr + (mn-1)/12
        i += 1
    return df

def monthlist(sep=2,only_head=False):
    monthlist = ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec"]
    for i in range(12):
      if i%sep != 0:
        monthlist[i] = ""
    if only_head:
      for i in range(12):
        monthlist[i] = monthlist[i][0]
    return monthlist

def season_to_month(season):
    """
    season : str
      djf or mam or jja or son
    """
    if season == 'DJF':
      month = [12,1,2]
    elif season == 'MAM':
      month = [3,4,5]
    elif season == 'JJA':
      month = [6,7,8]
    elif season == 'SON':
      month = [9,10,11]
    return month

def to_trend(df,file_path=None,val=3):
    val = str(val)
    df.to_csv(file_path,index=False,header=False,sep=" ",float_format="%.{}f".format(val))
