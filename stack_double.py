##update code
##on open java file it starts running in the background

import urllib.request
import os
import datetime

store_lines = []
real_values = []
get_index = []
final_stock_tickers = []
keep_first_parse = []
keep_second_parse = []
qr_parse = []

def check_lower(word):
    c = False
    for a in range (len(word)):
        if(word[a].islower()):
            c = True
    return c

file = open('2018/11/7.csv', 'r')
text = file.read().strip()
file.close()
store_lines = text.splitlines()
for x in range(len(store_lines)):
    if(store_lines[x].__contains__(",")):
        real_values.append(store_lines[x])
for y in range(len(real_values)):
    get_index = real_values[y].split(",", 1)
    if(check_lower(get_index[0]) == False):
        final_stock_tickers.append(get_index[0])            #retrieves all of the stock quotes


#now = datetime.datetime.now()
#print(now.year)
if(os.path.exists("stock_data") == False):
    os.mkdir("stock_data")

def create_folder():
    for tick in range(len(final_stock_tickers)):
        if(final_stock_tickers[tick].__contains__('"')):
            final_stock_tickers[tick] = final_stock_tickers[tick].replace('"', '')
        if(os.path.exists("stock_data/" + final_stock_tickers[tick])):
            print("exists")
        else:
            os.mkdir("stock_data/" + final_stock_tickers[tick])
            create_folder()

create_folder()



#for loop
for d in range(len(final_stock_tickers)):
    link = "https://www.jamstockex.com/market-data/listed-companies/stock-performance/"+final_stock_tickers[d]+"/latest"
    data = urllib.request.urlopen(link)
    mybytes = data.read()
    webpage_code = mybytes.decode("utf8")
    data.close()
    #####################               write function for partitioning
    for x in range(len(webpage_code)):                              #get tables
        if (webpage_code[x:x + 25] == "table-striped table-hover"):
            for j in range(x, len(webpage_code)):
                keep_first_parse.append(webpage_code[j])
                if (webpage_code[j - 8:j] == "</table>"):
                    break

    first_partition  = ''.join(keep_first_parse)

    for x in range(len(first_partition)):                              #get Annual Returns data
        if (first_partition[x:x + 6] == "Annual"):
            for j in range(x, len(first_partition)):
                keep_second_parse.append(first_partition[j])
                if (webpage_code[j - 8:j] == "</table>"):
                    continue

    second_partition  = ''.join(keep_second_parse) #Annual returns partition
    third_partition = first_partition.replace(second_partition,'') #Quarterly Returns

    #parsing Quarterly Returns
    for x in range(len(third_partition)):
        if (third_partition[x:x + 7] == "<tbody>"):
            for j in range(x, len(third_partition)):
                qr_parse.append(third_partition[j])
                if (third_partition[j - 8:j] == "</tbody>"):
                    continue

    first_qr_partition  = ''.join(qr_parse)
    next_qr_parse = []

    #parse by tables --tr
    for x in range(len(first_qr_partition)):
        if (first_qr_partition[x:x + 4] == "<tr>"):
            for j in range(x, len(first_qr_partition)):
                next_qr_parse.append(first_qr_partition[j])
                if (first_qr_partition[j - 5:j] == "</tr>"):
                    break

    next_p_parse = []

    second_qr_partition  = ''.join(next_qr_parse)
    for x in range(len(second_qr_partition)):
        if (second_qr_partition[x:x + 3] == "<td"):
            for j in range(x, len(second_qr_partition)):
                next_p_parse.append(second_qr_partition[j])
                if (second_qr_partition[j - 5:j] == "</td>"):
                    break

    last_partition  = ''.join(next_p_parse)
    final_way = last_partition.replace('"', '')
    final_way = final_way.replace('class=text-right', '')
    final_way = final_way.replace(' ', '')
    final_way = final_way.replace('<td>', '')
    final_way = final_way.replace('</td>', '')

    data = final_way.splitlines()
    years = []
    dollars = []
    for f in range(len(data)):
        if(data[f].__contains__("$") == False):
            years.append(data[f])
        else:
            dollars.append(data[f])

    f = open("stock_data/"+final_stock_tickers[d]+"/Quarterly_Returns.txt", "a")
    for s in range(len(years)):
        t = ((3*s)+s)
        u = t + 4
        get_year = years[s]
        get_dollars = dollars[t:u]
        final_output = []
        final_output.append(get_year)
        final_output.extend(get_dollars)
        save_data = ''.join(final_output)
        final_data = save_data.replace('$', '/')
        f.write(final_data + "\n")
    f.close()

    annual_first_parse = []
    for x in range(len(second_partition)):
        if (second_partition[x:x + 3] == "<td"):
            for j in range(x, len(second_partition)):
                annual_first_parse.append(second_partition[j])
                if (second_partition[j - 5:j] == "</td>"):
                    break

    third_annual_partition  = ''.join(annual_first_parse)
    final_way = third_annual_partition.replace('"', '')
    final_way = final_way.replace('class=text-right', '')
    final_way = final_way.replace(' ', '')
    final_way = final_way.replace('<td>', '')
    final_way = final_way.replace('</td>', '')
    final_way = final_way.replace('$', '')
    final_way = final_way.replace(',', '')
    final_way = final_way.replace('.00', '')
    f = open("stock_data/"+final_stock_tickers[d]+"/Annual_Returns.txt", "a")
    f.write(final_way)
    f.close()








