import PyPDF2
from PyPDF2 import PdfReader
f=open("C:\\avyan\\python\\working_with_.csv_files\\Working_Business_Proposal.pdf","rb")
pdf_reader=PdfReader(f)
num_pages=len(pdf_reader.pages)
print(num_pages)
page_one=pdf_reader.pages[0]
text_of_page1=page_one.extract_text()
print(text_of_page1)
first_page=pdf_reader.pages[0]
pdf_writer=PyPDF2.PdfWriter()
pdf_writer.add_page(first_page)
pdf_new=open("C:\\avyan\\python\\working_with_.csv_files\\new_file.pdf", mode="wb")
pdf_writer.write(pdf_new)
# making new pdf file
