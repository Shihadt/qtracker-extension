#!/usr/bin/env python3

import httplib2
import datetime
import time
import json
import os


AUTH_KEY = ''
REFRESH_RATE = 1
def format(num):
    if num <= 9:
        return '0'+ str(num)
    return str(num)

def toIST(t):
	hour = int(t[:2]) + 5
	minute = int(t[3:])+30
	if minute >=60:
		hour=hour+1
		minute = minute-60
	return format(hour) + ":" + format(minute)

def minuteToHour(m):
	hour = int(m/60)
	minute = int(m%60)
	return format(hour)+":"+format(minute)

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

    yourdate = toIST(data['first_in_time'][11:16])


    if int(data['daily_logs'][daily_logs]['in_out']) == 0:
        print("IN" + " :: " + yourdate)
    else:
        print("OUT" + " :: " + yourdate)


def printData(data):
    day = len(data['payload']['monthlyData'])-1
    today = data['payload']['monthlyData'][day]

    setTitle(changeToTime(today['hours_burned']))
    currectStatus(today)
    print("Burned Time   : " + changeToTime(today['hours_burned']))
    print("Clocked Time  : " + changeToTime(today['hours_clocked']))
    print("Break Duration: " + minuteToHour(today['break_duration']))

    # if int(today['hours_clocked'])>=9:
    #     sendNotification()

def apiCall():

    now = datetime.datetime.now()


    response, content = httplib2.Http().request(\
    "http://qtracker.qburst.com/v2/api/attendance-tracker/user/monthly-status?month="+
    str(now.month)+
    "&year="+str(now.year),headers={'Authorization':AUTH_KEY})

    if response.status !=200:
        print("Error code " + str(response.status))
        return
    data = json.loads(content)
    printData(data)



def main():
    apiCall()

if __name__ == '__main__':
    main()
