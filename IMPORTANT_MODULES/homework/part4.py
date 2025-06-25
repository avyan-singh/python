# This code searches for phone numbers in a specific format (XXX-XXX-XXXX) across multiple directories.
# It prints the found phone numbers and the file where they were found.
import re
import os
found=False
dir=['C:\\avyan\\python\\instructions\\extracted_content\\One',
'C:\\avyan\\python\\instructions\\extracted_content\\Two',
'C:\\avyan\\python\\instructions\\extracted_content\\Three',
'C:\\avyan\\python\\instructions\\extracted_content\\Four',
'C:\\avyan\\python\\instructions\\extracted_content\\Five']
num=-1
while not found==True:
    if os.path.exists(dir[0]):
        files = os.listdir(dir[0])
        for file in files:
            num+=1
            f=os.path.join(dir[0],files[num])
            if os.path.exists(f):
                f=open(f,'r')
                text=f.read()
                if re.findall(r'\d{3}-\d{3}-\d{4}',text):
                    print(re.findall(r'\d{3}-\d{3}-\d{4}',text))
                    print(f)
                    found=True
    if os.path.exists(dir[1]):
        num1=-1
        files = os.listdir(dir[1])    
        for file in files:
            num1+=1
            f=os.path.join(dir[1],files[num1])
            if os.path.exists(f):
                f=open(f,'r')
                text=f.read()
                if re.findall(r'\d{3}-\d{3}-\d{4}',text):
                    print(re.findall(r'\d{3}-\d{3}-\d{4}',text))
                    print(f)
                    found=True
    if os.path.exists(dir[2]):
        num2=-1
        files = os.listdir(dir[2])    
        for file in files:
            num2+=1
            f=os.path.join(dir[2],files[num2])
            if os.path.exists(f):
                f=open(f,'r')
                text=f.read()
                if re.findall(r'\d{3}-\d{3}-\d{4}',text):
                    print(re.findall(r'\d{3}-\d{3}-\d{4}',text))
                    print(f)
                    found=True
    if os.path.exists(dir[3]):
        num3=-1
        files = os.listdir(dir[3])    
        for file in files:
            num3+=1
            f=os.path.join(dir[3],files[num3])
            if os.path.exists(f):
                f=open(f,'r')
                text=f.read()
                if re.findall(r'\d{3}-\d{3}-\d{4}',text):
                    print(re.findall(r'\d{3}-\d{3}-\d{4}',text))
                    print(f)
                    found=True

    if os.path.exists(dir[4]):
        num4=-1
        files = os.listdir(dir[4])    
        for file in files:
            num4+=1
            f=os.path.join(dir[4],files[num4])
            if os.path.exists(f):
                f=open(f,'r')
                text=f.read()
                if re.findall(r'\d{3}-\d{3}-\d{4}',text):
                    print(re.findall(r'\d{3}-\d{3}-\d{4}',text))
                    print(f)
                    found=True
   