
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

def xlist(interval=1,syr=2000,fyr=2020,month=True,v_month=1):
    """
    Parameters
    ----------
    interval : int
      年の間隔
    syr : int
      開始年
    fyr : int
      最後の年
    monthTF : bool
      月の表示の有無
    vmonth : int
    　表示の月について

    Returns
    ----------
    x_index : list
      データリスト
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
            df.loc[i,"date"] = str(yr)+"/"+IntegerChecker(mn)
            i += 1
    return df

class Basic():
    def monthlist(self):
        monthlist = ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec"]
        return monthlist
