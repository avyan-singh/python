import csv
emails=[]
num=0
data=open("C:\\avyan\\python\\working_with_.csv_files\\example.csv", encoding='utf-8')
csv_data=csv.reader(data)
data_lines=list(csv_data)
for line in data_lines:
    emails.append(data_lines[num][3])
    num+=1  
print(emails)#emails

# full names
full_names=[]
num=0
for line in data_lines:
    full_names.append(data_lines[num][1] + " " + data_lines[num][2])
    num+=1
print(full_names) # full names
csv_file=open("C:\\avyan\\python\\working_with_.csv_files\\file1.csv", mode="w",newline='')
csv_writer=csv.writer(csv_file,delimiter=',')
csv_writer.writerow(["Full Name","class"])
csv_writer.writerows([['Jose','8th'],['John','8th']])