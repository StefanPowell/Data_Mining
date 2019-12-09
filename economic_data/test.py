import urllib.request, json, tkinter
from datetime import datetime

dateTimeObj = datetime.now()

with urllib.request.urlopen("https://cdn-nfs.faireconomy.media/ff_calendar_thisweek.json") as url:
    data = json.loads(url.read().decode())

data_today = []
high_impact = []
Economicdata = []

def today_data():
    for x in range(len(data)):
        data_dict = data[x]
        datetime = data_dict["date"]
        datetime = datetime.split("T")
        date = datetime[0]
        time = datetime[1]
        dateStr = dateTimeObj.strftime("%Y-%m-%d")

        #if(str(date) != dateStr):

        data_today.append(data_dict)
    return data_today

def impact(level, data):
    for x in range(len(data)):
        data_dict = data[x]
        impact = data_dict["impact"]
        if(impact == level):
            high_impact.append(data_dict)
    return high_impact

def start():
    #focus on high impact
    get_data_today = today_data()
    high_impact_news = impact("High", get_data_today)
    for y in high_impact_news:
        if(y['forecast'] == ''):
            continue
        else:
            datetime = y["date"]
            datetime = datetime.split("T")
            time = datetime[1].split("-")
            time = time[0]
            print(time)


            #print(y['title'])
            #print(y['forecast'])
            #print(y['previous'])
            #print(y['country'])
            #print(y['date'])

start()

class _currency_:
    def __init__(self, symbol, country):
        self.symbol = symbol
        self.country = country

class economic_data:
    def __init__(self, name, currency, direction, effect):
        self.name = name
        self.currency = currency
        self.direction = direction
        self.effect = effect
        Economicdata.append(self)


def create_economic_data():
    economic_data("German ZEW Economic Sentiment", "EUR", "up", "positive")


create_economic_data()
#for data in Economicdata:
#    print(data.name)





