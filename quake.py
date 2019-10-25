import urllib.request
import re
import csv

keep_first_parse = []

link = "http://ds.iris.edu/seismon/eventlist/index.phtml"
data = urllib.request.urlopen(link)
mybytes = data.read()
webpage_code = mybytes.decode("utf8")
data.close()


def web_partition(start, end, code):
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


first_partition = ''.join(web_partition("<tbody>", "</tbody>", webpage_code));


remove_array = ['<tbody>', '<tr>', '<td  >', '</td> ', "<td class=' latlon' >", "<td class=' mag' > ", "<td class=' dep' > ", "<td class=' region' > <a href='"
                "<TD class='evid'>&nbsp;&nbsp;<a href=", "<td class=' big mag' >"]
strip_data = clean_data(remove_array, first_partition);
strip_data = re.sub('\n<td class=.*?</tr> ', '', strip_data, flags=re.DOTALL)

#remove newlines
strip_data = strip_data.replace('\n\n', '\n')

quake_array = strip_data.split("\n")
quake_array.pop(0)
quake_array.pop(0)
quake_array.pop()
quake_array.pop()

c = 0
for m in range(len(quake_array)):
       try:
           if len(quake_array[c+1]) > 10:
               #remove only first one
               quake_array.pop(c)
           if len(quake_array[c + 2]) > 10:
               # remove both first and second
               quake_array.pop(c)
               quake_array.pop(c+1)
           if len(quake_array[c + 3]) > 10:
               # remove first, second and third
               quake_array.pop(c)
               quake_array.pop(c+1)
               quake_array.pop(c+2)
           if len(quake_array[c + 4]) > 10:
               #remove first, second, third and fourth
               quake_array.pop(c)
               quake_array.pop(c + 1)
               quake_array.pop(c + 2)
               quake_array.pop(c + 3)
       except:
           print("")

c = 0
with open('earthquake_data.csv', mode='w') as earthquake_data:
    quake_writer = csv.writer(earthquake_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    quake_writer.writerow(["Date and Time", "Latitude", "Longitude", "Magnitude", "Depth"])
    for m in range(len(quake_array)):
        try:
            quake_writer.writerow([quake_array[0 + c], quake_array[1 + c], quake_array[2 + c], quake_array[3 + c], quake_array[4 + c]])
            c = c + 5
        except:
            print(" ")
