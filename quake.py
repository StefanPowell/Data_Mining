import urllib.request

keep_first_parse = []

link = "http://ds.iris.edu/seismon/eventlist/index.phtml"
data = urllib.request.urlopen(link)
mybytes = data.read()
webpage_code = mybytes.decode("utf8")
data.close()

def web_partition(start, end):
    for x in range(len(webpage_code)):  # get tables
        if (webpage_code[x:x + 7] == "<tbody>"):
            for j in range(x, len(webpage_code)):
                keep_first_parse.append(webpage_code[j])
                if (webpage_code[j - 8:j] == "<tbody>"):
                    break


first_partition  = ''.join(keep_first_parse)
print(first_partition )