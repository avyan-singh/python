import csv
emails=[]
data=open("C:\\avyan\\python\\working_with_.csv_files\\example.csv", encoding='utf-8')
csv_data=csv.reader(data)
data_lines=list(csv_data)
for line in data_lines:
    emails.append(line[3])
print(emails)#emails

# full names
full_names=[]
for line in data_lines:
    full_names.append(line[1] + " " + line[2])
print(full_names) # full names
csv_file=open("C:\\avyan\\python\\working_with_.csv_files\\file1.csv", mode="w",newline='')
csv_writer=csv.writer(csv_file,delimiter=',')
csv_writer.writerow(["Full Name","Email"])
for lines in data_lines:
    csv_writer.writerow([lines[1]+' '+lines[2],lines[3]])

