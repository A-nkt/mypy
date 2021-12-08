import pandas as pd
import numpy as np


class read_data:
    def __init__(self,data_path, save=False, path_out=None,colname=False):
        """
        csv形式で読み取れる関数
        
        Parameters
        -----------
        data_path : str
            ファイルのパス
        save : bool
            保存の有無
        path_out : str
            出力ファイルパス
        
        Returns
        ----------
        xr : pd.DataFrame
            csv形式
        """
        self.xr = pd.DataFrame();iy = 0
        path = data_path
        with open(path) as f:
            for s_line in f:
                s2_line = s_line.split(" ")
                j = 0
                for s3 in s2_line:
                    if not s3 == "":
                        self.xr.loc[iy,j] = s3
                        j += 1
                iy += 1
        for k in range(len(self.xr)):
            self.xr.loc[k,6] = self.xr.loc[k,6].split("\n")[0]

            for t in range(3,7,1):
                self.xr.loc[k,t] = float(self.xr.loc[k,t])
                
        if save:
            self.xr.to_csv(path_out,index=False,header=None)

        if colname:
            self.xr = self.xr.rename(columns={3:"フィッテイング結果",4:"長期トレンド",5:"季節サイクル",6:"Growth Rate"})

    def to_csv(self):
      return self.xr

    def make_time_series(self,syr=2001,fyr=2021):
        i = 0
        for yr in range(syr,fyr,1):
          for mn in range(1,13,1):
            self.xr.loc[i,"time"] = yr + (mn-1)/12
            i += 1
        return self.xr
    
    def make_date(self,year_row=0,month_row=1):
        """
        date列作成関数
        
        Parameters
        ----------
        df : pd.DataFrame
            対象のデータセット
        year_row : int
            年の列 (default : 0)
        month_row : int
            月の列 (default : 1)
        
        Returns
        ----------
        df : pd.DataFrame
            date列作成後
        """
        for k in range(len(self.xr)):
            self.xr.loc[k,"date"] = str(self.xr.loc[k,year_row]) +"/"+ str(self.xr.loc[k,month_row]).zfill(2)
            self.xr.loc[k,0] = int(self.xr.loc[k,year_row])
        return self.xr

    def climate_value(self,year_col,season_col):
        """
        気候値変換関数
        
        Parameters
        -----------
        df : pd.DataDrame
            対象のデータ
        
        Parameters
        -----------
        dy_new : 気候値変換
        """
        dy_new = pd.DataFrame()
        for j in range(1,13,1):
            data = []
            for k in range(len(self.xr)):
                if int(self.xr.loc[k,year_col]) == j:
                    data.append(self.xr.loc[k,season_col])
            dy_new.loc[j,"cval"] = np.mean(data)
            dy_new.loc[j,"max"] = np.max(data)
            dy_new.loc[j,"min"] = np.min(data)
        return dy_new
