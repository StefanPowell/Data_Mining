import urllib.request
import re
import csv

link = "https://www.jamstockex.com/"
data = urllib.request.urlopen(link)
mybytes = data.read()
webpage_code = mybytes.decode("utf8")
data.close()

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

first_partition = ''.join(web_partition("<!--Page Ticker-->", "<!-- /Page Ticker -->", webpage_code));
second_partition = ''.join(web_partition("Market Summary", "<!-- /Page Ticker -->", first_partition));

remove_array = ['<li>', '<br />', '</li>', '</a>', '</div>', '</ul>', '<img style="height:16px"', 'src="/img/none.png"',
                'src="/img/down.png">', '<!-- /Page Ticker -->', '>', '        ', '    ', '<a', 'src="/img/up.png']
strip_data = clean_data(remove_array, second_partition);

all = strip_data.splitlines()
remove_blanks = []
for x in range(len(all)):
    for y in all[x]:
        if(y != ' '):
            remove_blanks.append(all[x])
            break

data = []
final_array = []

for z in remove_blanks:
    if(z[0:4] != "href"):
        data.append(z)
for y in data[1:]:
    if(y != '"'):
        final_array.append(y)


print(final_array)

