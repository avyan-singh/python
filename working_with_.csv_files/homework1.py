import PyPDF2
import csv
link = "C:\\avyan\\python\\working_with_.csv_files\\find_the_link.csv"
opened_file = open(link, encoding='utf-8')
text =csv.reader(opened_file)
lines= list(text)
num=0
mystring = ""
for line in lines:
    mystring += lines[num][num]
    num += 1
print(mystring)