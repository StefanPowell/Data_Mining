import urllib.request
keep_first_parse = []

keywords = input("Enter keywords.. ")
link_keywords = keywords.replace(' ', '+')
link = "https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20190117205956&SearchText="+link_keywords

def aliexpress():
    data = urllib.request.urlopen(link)
    mybytes = data.read()
    webpage_code = mybytes.decode("utf8")
    data.close()
    for x in range(len(webpage_code)):                              #get tables
        if (webpage_code[x:x + 21] == 'class="store $p4pLog"'):
            for j in range(x, len(webpage_code)):
                keep_first_parse.append(webpage_code[j])
                if (webpage_code[j - 4:j] == "</a>"):
                    break
    test  = ''.join(map(str, keep_first_parse))
    new_listing = test.split("\n")
    for x in new_listing:
        print(x)

def amazon():
    print("amazon")

def ebay():
    print("ebay")