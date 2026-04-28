class shope:
    def __init__(self,book,book_company,price):
        self.book = book
        self.book_company = book_company
        self.price = price


book = input("Book's name : ")
book_company = input ("Book's company name : ")
price = int(input("Enter minimum price : "))

Book =shope(book,book_company,price)

print(f"Book name is {Book.book} \nThis company name is {Book.book_company} \nThis price is {Book.price}")