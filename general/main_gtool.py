import sys
sys.path.append("/mnt/dg1/nakata/PyCode/init/")
from lib import *


class Make_data:
  def __init__(self,file):
    self.file = file

  def to_DataFrame(self,method="monthly",syr=1950,fyr=2021,index=1):
    self.df = pd.DataFrame()
    harea = pygtool.gtcalic.get_area(dlon=2.8125,dlat=2.8125,er=6370e3)
    for yr in range(syr,fyr,1):
      for mn in range(1,13,1):
        dat = pygtool.read2d(self.file,count=index)
        dat = dat.getarr(timestep=index-1)
        self.df.loc[index-1,"year"] = str(yr)
        self.df.loc[index-1,"month"] = str(mn).zfill(2)
        self.df.loc[index-1,"dat"] = np.sum(dat[:,:] * harea[:,:] * int(general.main_general.countdays(yr,mn)) * 86400 * 1e-9)
        index += 1
    if method == "monthly":
      return self.df
    elif method == "yearly":
      self.dx = pd.DataFrame()
      index = 0;i = 0
      for yr in range(syr,fyr,1):
        data = []
        for mn in range(1,13,1):
          data.append(self.df.loc[index,"dat"])
          index += 1
        self.dx.loc[i,"year"] = str(yr)
        self.dx.loc[i,"dat"] = sum(data)
        i += 1
      return self.dx
       
