class Book :
    def __init (self):
        self.bookid =0
        self.page = 0
        self.price=0
    def inter_data (self):
        self.bookid = int (input ("enter a book id :"))
        self.page = int(input ("enter a page no : "))
        self.price = int(input ("enter a price :"))
    def show_data (self):
        print ("bookid :" , self.bookid)
        print ("book page  :" , self.page)
        print ("book price  :" , self.price)
book = Book ()
book.inter_data()
book.show_data()
        