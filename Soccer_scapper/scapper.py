import urllib.request
import re
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException
import re
import time

from bs4 import BeautifulSoup
import json
import requests
import pandas as pd

options = Options()

driver = webdriver.Chrome (service=Service (ChromeDriverManager().install()),
                           options=options)
driver.get('https://www.whoscored.com/Matches/1694372/Live/Europe-Champions-League-2022-2023-Real-Madrid-Liverpool#chalkboard')
driver.implicitly_wait(10)
content = driver.page_source



webpage_code = content






def web_partition(start, end, code):
    keep_first_parse = []
    for x in range(len(code)):  # get tables
        if (code[x:x + len(start)] == start):
            for j in range(x, len(code)):
                keep_first_parse.append(code[j])
                if (code[j - len(end):j] == end):
                    break
    return keep_first_parse

def clean_data(array_data, partition):
    for y in range(len(array_data)):
        partition = partition.replace(array_data[y], '')
    return partition




print(''.join(web_partition("<script>", "</script>", webpage_code)))

driver.quit()



# first_partition = ''.join(web_partition("<!--Page Ticker-->", "<!-- /Page Ticker -->", webpage_code));
# second_partition = ''.join(web_partition("Market Summary", "<!-- /Page Ticker -->", first_partition));

# remove_array = ['<li>', '<br />', '</li>', '</a>', '</div>', '</ul>', '<img style="height:16px"', 'src="/img/none.png"',
#                 'src="/img/down.png">', '<!-- /Page Ticker -->', '>', '        ', '    ', '<a', 'src="/img/up.png']
# strip_data = clean_data(remove_array, second_partition);

# all = strip_data.splitlines()
# remove_blanks = []
# for x in range(len(all)):
#     for y in all[x]:
#         if(y != ' '):
#             remove_blanks.append(all[x])
#             break
#
# data = []
# final_array = []
#
# for z in remove_blanks:
#     if(z[0:4] != "href"):
#         data.append(z)
# for y in data[1:]:
#     if(y != '"'):
#         final_array.append(y)
#
#

