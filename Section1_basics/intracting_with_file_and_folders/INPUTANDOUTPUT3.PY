with open("myfile5.csv", "r") as file:
    file.seek(0)  
    data = file.read() 
data = data[21:]  # Remove the first element (header row)
print(data)
supervisor_id={}
for id,name,supervisorid in data:
    if supervisorid !=None:
        supervisor_id.setdefault(name,[]).append(supervisorid)
print(supervisor_id)