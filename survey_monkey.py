import glob, os
import csv
import urllib.request

path = "/home/pt/Desktop/survey_response"
links = []
keep_first_parse = []
respondents = []
clean_data = []

os.chdir(path)
for file in glob.glob("*.html"):
    links.append(file)

directory = "file:///home/pt/Desktop/survey_response/"


def web_partition(start, end, code):
    for x in range(len(code)):  # get tables
        if (code[x:x + len(start)] == start):
            for j in range(x, len(code)):
                keep_first_parse.append(code[j])
                if (code[j - len(end):j] == end):
                    break
    return keep_first_parse

def check_array(val, arrayval):
    found = 0
    for y in range(len(arrayval)):
        if(val == arrayval[y]):
            found = 1
    return found

with open('/home/pt/Desktop/survey_response/survey.csv','rt')as f:
    data = csv.reader(f)
    for row in data:
        try:
            respondents.append(int(row[0]))
        except:
            print("")

with open('survey.csv', mode='a') as survey_data:
    survey_writer = csv.writer(survey_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    l = 0
    for z in range(len(links)):

        main_file = links[z]
        full_link = directory + main_file

        file_number = main_file.replace('SurveyMonkey', '')
        file_number = file_number.replace('.html', '')
        output_str = "Respondent " + file_number + " already added"
        add_str = "Adding Respondent " + file_number

        if(check_array(int(file_number), respondents) == 1):
            print(output_str)
        else:
            data = urllib.request.urlopen(full_link)
            mybytes = data.read()
            webpage_code = mybytes.decode("utf8")
            data.close()

            first_partition = ''.join(web_partition('<div id="element-container" class="">', 'div class="footer full-width-section mui-dark-theme">', webpage_code));

            keep_first_parse.clear()

            web_data = ''
            web_data = (''.join(web_partition('<span>', '</span>', first_partition)))
            keep_first_parse.clear()

            web_data = web_data.replace('<<', '<')
            web_data = web_data.replace('<span>', '')

            clean_data = web_data.split("</span>")
            for x in range( (len(clean_data)) - 10):
               clean_data.pop(x)
            try:
                survey_writer.writerow([file_number, clean_data[0], clean_data[1], clean_data[2], clean_data[3], clean_data[4], clean_data[5], clean_data[6], clean_data[7], clean_data[8], clean_data[9]])
                print(add_str)
            except Exception as e:
                error_msg = "Error: " + str(e) + " at Respondent " + file_number
                print(error_msg)
            clean_data.clear()
