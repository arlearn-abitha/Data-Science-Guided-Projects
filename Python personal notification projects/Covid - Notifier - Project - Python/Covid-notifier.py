# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 15:17:39 2021

@author: abith
"""

import requests
import json
import plyer
import datetime
import time
r = requests.get('https://corona-rest-api.herokuapp.com/Api/india')
#print(type(r))
news = r.text
#print(news)
dict1 = {'many': 5, 'sad': 'emoji', 'certain': 'death'}
#print(type(json.dumps(dict1)))
dict2 = json.loads(news)
#print(dict2)
newsdict = dict2['Success']
#print(newsdict)
#print("Tests Per One Million: ", str(newsdict['testsPerOneMillion']))
tod = datetime.date.today()
todstr=tod.strftime('(%d-%m-%y)')

plyer.notification.notify(
    title = 'Covid-19 Notification  '+todstr,
    message = 'Total Cases: '+str(newsdict['cases'])+"\n"
    "Today's cases: "+str(newsdict['todayCases'])+'\n'
    'No. of Deaths: '+str(newsdict['deaths'])+'\n',
    app_icon=r'C:\Users\abith\Desktop\covid.ico',
    timeout=10
    
    )
time.sleep(5*60*60)