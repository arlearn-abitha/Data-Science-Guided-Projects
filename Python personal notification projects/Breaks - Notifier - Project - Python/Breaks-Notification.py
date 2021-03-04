# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 08:44:45 2021

@author: abith
"""

import plyer
import datetime
import time

tod = datetime.date.today()
nowstr= tod.strftime('%d-%m-%y')

plyer.notification.notify(
    title='Personal Reminder: '+nowstr,
    message='Go walk for 15 minutes, Abitha.\n It will help you recover from your Backache ',
    app_icon=r'C:\Users\abith\Desktop\Personal_Reminder.ico',
    timeout=3    
    )
time.sleep(45*60)