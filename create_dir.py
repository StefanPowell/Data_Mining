import getpass
import os
import datetime

now = datetime.datetime.now()
username = getpass.getuser()
days_in_each_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
directory_location = "C:/Users/"+username+"/Documents/dates"

##if Mac or Linux main directory may not be the same

def create_main(dir):
    os.mkdir(dir)

def create_years():
    for x in range(6):
        years = now.year - x
        new_dir = [directory_location, "/", str(years)]
        new_dir = ''.join(new_dir)
        if (os.path.isdir(new_dir) == False):
            os.mkdir(new_dir)

def create_months(current_year_dir):
    for f in range(1,13):
        each_month_dir = [current_year_dir, "/", str(f)]
        month_directory = ''.join(each_month_dir)
        if(os.path.isdir(month_directory) == False):
            os.mkdir(month_directory)

def create_days(month, year):
    new_dir = [directory_location, "/", str(year), "/", str(month)]
    month_directory = ''.join(new_dir)
    if(os.listdir(month_directory) == []):
        for m in range(1, days_in_each_month[month]+1):
            create_day = [str(year), "-", str(month), "-", str(m)]
            current_day = ''.join(create_day)
            new_date = datetime.datetime.strptime(current_day, '%Y-%m-%d')
            if(new_date.weekday() != 6 and new_date.weekday() != 5):
                day_dir = [month_directory, "/", str(m)]
                create_dir_day = ''.join(day_dir)
                os.mkdir(create_dir_day)

def start():
    if(os.path.isdir(directory_location)):
        year = now.year - 5
        new_dir = [directory_location, "/", str(year)]
        five_years_ago_directory = ''.join(new_dir)
        if(os.path.isdir(five_years_ago_directory)):
            for i in range(6):
                current = now.year - i
                new_dir = [directory_location, "/", str(current)]
                current_year_dir = ''.join(new_dir)
                if(os.listdir(current_year_dir) == []):
                    create_months(current_year_dir)
                    start()
                for z in range(1,13):
                    create_days(z, current)
        else:
            create_years()
            start()
    else:
        create_main(directory_location)
        start()
start()



