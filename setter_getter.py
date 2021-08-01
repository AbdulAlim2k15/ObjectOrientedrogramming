class book:
       

    def setName(self,name,author):
        self.bookName = name
        self.authorName = author
        

    def getName(self):
        book  = self.bookName +" by "+ self.authorName
        return book

book1 = book()
book1.setName("Python Programming","Abdul Alim")
print(book1.getName())