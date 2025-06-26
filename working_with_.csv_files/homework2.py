import re
import PyPDF2
f=open("C:\\avyan\\python\\working_with_.csv_files\\Find_the_Phone_Number.pdf","rb")
pdf_reader=PyPDF2.PdfReader(f)
num_pages=len(pdf_reader.pages)
num=0
while num_pages > num:
    page=pdf_reader.pages[num].extract_text()
    matches=    re.findall(r'\d{3}[()\-\.]\d{3}[()\-\.]?\d{4}', page)
    if matches:
        print(matches)
        print(num)
    num += 1
