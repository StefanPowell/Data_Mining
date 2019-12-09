import urllib.request, json, tkinter
from datetime import datetime

dateTimeObj = datetime.now()

with urllib.request.urlopen("https://cdn-nfs.faireconomy.media/ff_calendar_thisweek.json") as url:
    data = json.loads(url.read().decode())

data_today = []
high_impact = []

def today_data():
    for x in range(len(data)):
        data_dict = data[x]
        datetime = data_dict["date"]
        datetime = datetime.split("T")
        date = datetime[0]
        time = datetime[1]
        dateStr = dateTimeObj.strftime("%Y-%m-%d")
        if(str(date) == dateStr):
            data_today.append(data_dict)
    return data_today

def impact(data):
    for x in range(len(data)):
        data_dict = data[x]
        impact = data_dict["impact"]
        if(impact == "Medium"):
            high_impact.append(data_dict)
    return high_impact


print(today_data())





