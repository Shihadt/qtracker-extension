#!/usr/bin/env python3

import httplib2
import datetime
import time
import json


AUTH_KEY = ''
REFRESH_RATE = 100
def format(num):
    if num < 9:
        return '0'+ str(num)
    return str(num)

def changeToTime(num):
    hour = int(num)
    minute = int((num*60)%60)
    totalTime = format(hour) + ":" + format(minute)
    return totalTime

def setTitle(data):
    print(data)
    print("---")

def currectStatus(data):
    daily_logs = len(data['daily_logs']) -1
    if int(data['daily_logs'][daily_logs]['in_out']) == 0:
        print("IN")
    else:
        print("OUT")

def printData(data):
    day = len(data['payload']['monthlyData'])-1
    today = data['payload']['monthlyData'][day]

    setTitle(changeToTime(today['hours_burned']))
    currectStatus(today)
    print("Burned Time   : " + changeToTime(today['hours_burned']))
    print("Clocked Time  : " + changeToTime(today['hours_clocked']))
    print("Break Duration: " + changeToTime(today['break_duration']))


def apiCall():
    
    now = datetime.datetime.now()
    
    _, content = httplib2.Http().request(\
    "http://qtracker.qburst.com/v2/api/attendance-tracker/user/monthly-status?month="+
    str(now.month)+
    "&year="+str(now.year),headers={'Authorization':AUTH_KEY})
    
    data = json.loads(content)
    printData(data)
    time.sleep(REFRESH_RATE)
    

def main():
    apiCall()

if __name__ == '__main__':
    main()
