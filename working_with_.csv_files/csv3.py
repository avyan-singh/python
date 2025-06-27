import PyPDF2
f=open("C:\\avyan\\python\\working_with_.csv_files\\Working_Business_Proposal.pdf","rb")
reader=PyPDF2.PdfReader(f)
for page in reader.pages:
    page_text=page.extract_text()
    print(page_text)