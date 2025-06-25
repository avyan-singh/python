import os
import re

base_dir = 'C:\\avyan\\python\\instructions\\extracted_content\\'

base_dir='C:\\avyan\\python\\instructions\\extracted_content\\'
dirs=[os.path.join(base_dir,d) for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir,d))]
for dir in dirs:
    for filename in os.listdir(dir):
        file_path = os.path.join(dir, filename)
        with open(file_path, 'r') as f:
            text=f.read()    
            matches = re.findall(r'\d{3}-\d{3}-\d{4}', text)
            if matches:
                print(matches)
                print(file_path)
                break
        