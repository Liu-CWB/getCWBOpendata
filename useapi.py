import requests
import urllib
import os

api = 'your api'
webpath = 'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/'
dataname = 'data file name you want download' #ex:M-A0061-072.grb2
allwebname = webpath+dataname+'?Authorization='+api+'&downloadType=WEB&format=the data format you want download'
#ex: allwebname = webpath+dataname+'?Authorization='+api+'&downloadType=WEB&format=GRIB2'
print(allwebname)
topath = 'your download file path'
urllib.request.urlretrieve(allwebname,os.path.join(topath,dataname))
