class Book:
     def __init__(self,author,title,pages):
         self.author=author
         self.title=title
         self.pages=pages
    #  def myprint(self):
    #      return f"{self.author} wrote {self.title}"
     def __str__(self):
         return f"{self.author} wrote {self.title}"
     def __len__(self):
         return self.pages
     def __del__(self):
         print('An instance of the book have been deleted')
book=Book('Jose','Python is great',200)
print(book)
print(len(book))


       