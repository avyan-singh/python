def paper_doll(text):
    i=0
    string1=""
    while not i>len(text)-1:
        string1=string1+text[i]*3
        i+=1    
  
    return string1

print(paper_doll('Hello'))# --> 'HHHeeellllllooo'
print(paper_doll('Mississippi'))#--> 'MMMiiissssssiiippppppiii'