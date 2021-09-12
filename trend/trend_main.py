import pandas as pd
import numpy as np


class variation:
    @classmethod
    def to_csv(self,data_path, save=False, path_out=None):
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
        xr = pd.DataFrame();iy = 0
        path = data_path
        with open(path) as f:
            for s_line in f:
                s2_line = s_line.split(" ")
                j = 0
                for s3 in s2_line:
                    if not s3 == "":
                        xr.loc[iy,j] = s3
                        j += 1
                iy += 1
        for k in range(len(xr)):
            xr.loc[k,6] = xr.loc[k,6].split("\n")[0]

            for t in range(3,7,1):
                xr.loc[k,t] = float(xr.loc[k,t])
                
        if save:
            xr.to_csv(path_out,index=False,header=None)
        return xr
    
    @classmethod
    def make_date(self,df,year_row=0,month_row=1):
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
        for k in range(len(df)):
            df.loc[k,"date"] = str(df.loc[k,year_row]) +"/"+ str(df.loc[k,month_row]).zfill(2)
            df.loc[k,0] = int(df.loc[k,year_row])
        return df

    @classmethod
    def make_colname(self,df):
        """
        列名変更関数

        Parameters
        ---------
        df : pd.DataFrame
          対象のデータセット

        Returns
        ---------
        df : pd.DataFrame
          結果
        """
        df = df.rename(columns={3:"フィッテイング結果",4:"長期トレンド",5:"季節サイクル",6:"Growth Rate"})

        return df


    
    @classmethod
    def climate_value(self,df):
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
            for k in range(len(df)):
                if int(df.loc[k,1]) == j:
                    data.append(df.loc[k,5])
            dy_new.loc[j,"cval"] = np.mean(data)
        return dy_new
