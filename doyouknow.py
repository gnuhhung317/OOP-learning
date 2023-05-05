import time
class Book:
    def __init__(self,title,author,ibsn):
        self.title =title
        self.author = author
        self.ibsn = ibsn
        self.checkout=False
    def infor(self):
        print("Tựa đề sách là",self.title,"của",self.author,"với số ibs là",self.ibsn)
    def is_available(self):
        if self.checkout:
            print(f"{self.title} có sẵn!")
        else:
            print(f"{self.title} không có sẵn!")
    def check_out(self):
        if not self.checkout:
            print(f"{self.title} của bạn đây!")
            self.checkout=True
        else:
            print(f"{self.title} đã bị mượn!")
    def return_book(self):
        if self.checkout:
            print(f"{self.title} đã được trả!")
            self.checkout= False
        else:
            print(f"{self.title} chưa được mượn!")
class library:
    def __init__(self):
        self.books=[]
    def add_book(self,book):

        self.books.append(book)
    def remove_book(self,book):
        self.books.remove(book)
    def search_book(self,keyword=str):
        matched_book = [book for book in self.books if keyword.lower() in book.title.lower()]
        if len(matched_book)==0:
            print("Không tìm thấy sách.")
        else:
            print("Tìm được:")
            i=1
            for book in matched_book:
                print(f"{i}. {book.title} của {book.author} với số ibs là {book.ibsn}")
                i+=1
        return matched_book

    def display_book(self):
        i=1
        for book in self.books:
            print(f"{i}. {book.title} by {book.author}")
            i+=1
    def display_available_book(self):
        available_book=[book for book in self.books if book.checkout==False]
        if len(available_book)==0:
            print("Không có sách nào có sẵn!")
        else:
            i=1
            for book in available_book:
                print(f"{i}. {book.title} của {book.author}")
                i += 1

    def working(self, classname, func):
        book_name = input("Nhập vào tên sách: ")
        book_name = nice(book_name)
        dem = 1
        for book in classname.books:
            if book_name.lower() == book.title.lower():
                book.func()
                dem = 0
        if dem == 1:
            print("Không có sách với tiêu đề như vây.")
            print("Tìm kiếm sách có khả năng...")
            classname.search_book(book_name)



def nice(book_name):
    return " ".join(book_name.split())


Mylib=library()
book1 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")
book2 = Book("1984", "George Orwell", "9780451524935")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
book4 = Book("One Hundred Years of Solitude", "Gabriel Garcia Marquez", "9780060883287")
book5 = Book("Moby-Dick", "Herman Melville", "9780142437247")
book6 = Book("The Catcher in the Rye", "J.D. Salinger", "9780316769488")
book7 = Book("The Adventures of Huckleberry Finn", "Mark Twain", "9780486280615")
book8 = Book("Pride and Prejudice", "Jane Austen", "9780141439518")
book9 = Book("Brave New World", "Aldous Huxley", "9780060850524")
book10 = Book("Animal Farm", "George Orwell", "9780141036137")
book11 = Book("The Lord of the Rings", "J.R.R. Tolkien", "9780544003415")
book12 = Book("The Hobbit", "J.R.R. Tolkien", "9780547928227")
book13 = Book("The Chronicles of Narnia", "C.S. Lewis", "9780007100221")
book14 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "9780345391803")
book15 = Book("A Game of Thrones", "George R.R. Martin", "9780553573404")
book16 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "9781408855652")
book17 = Book("Gone with the Wind", "Margaret Mitchell", "9781451635621")
book18 = Book("The Picture of Dorian Gray", "Oscar Wilde", "9780141442464")
book19 = Book("Frankenstein", "Mary Shelley", "9780486282114")
book20 = Book("The Count of Monte Cristo", "Alexandre Dumas", "9780140449266")
books=[book1,book2,book3,book4,book5,book6,book7,book8,book9,book10,book11,book13,book13,book14,book15,book16,book17,book18,book19,book20]
for book in books:
    Mylib.add_book(book)
print("Chào mừng đến với thư viện của Đức Hùng!")
time.sleep(1)
print(f"Hiện tại bên mình đang có {len(Mylib.books)} quyển sách.")
time.sleep(1)
while True:
    print("Bạn muốn làm gì nào?")
    time.sleep(1)
    print("1. tìm thông tin sách xác định")
    time.sleep(0.1)
    print("2. xem sách có sẵn hãy không")
    time.sleep(0.1)
    print("3. mượn sách")
    time.sleep(0.1)
    print("4. trả sách")
    time.sleep(0.1)
    print("5. thêm sách")
    time.sleep(0.1)
    print("6. Xóa sách")
    time.sleep(0.1)
    print("7. tìm sách")
    time.sleep(0.1)
    print("8. hiển thị toàn bộ sách")
    time.sleep(0.1)
    print("9. hiển thị sách khả dụng")
    time.sleep(0.1)
    print("10. thoát ra")
    time.sleep(0.1)
    n=int(input("Nhập vào lựa chọn của bạn(1-10): "))
    dem=1
    while n<1 or n>10:
        n = int(input(f"Lựa chọn không hợp lệ, mời nhập lại({dem}/5): "))
        dem+=1
        if dem==6:
            break
    if n==1:
        """find the in4 of book"""
        book_name = input("Nhập vào tên sách: ")
        book_name = nice(book_name)
        dem = 1
        for book in Mylib.books:
            if book_name.lower() == book.title.lower():
                book.infor()
                dem = 0
        if dem == 1:
            print("Không có sách với tiêu đề như vây.")
            print("Tìm kiếm sách có khả năng..")
            Mylib.search_book(book_name)

    if n==2:
        book_name = input("Nhập vào tên sách: ")
        book_name = nice(book_name)
        dem = 1
        for book in Mylib.books:
            if book_name.lower() == book.title.lower():
                book.is_available()
                dem = 0
        if dem == 1:
            print("Không có sách với tiêu đề như vây.")
            print("Tìm kiếm sách có khả năng..")
            Mylib.search_book(book_name)

    if n==3:
        book_name = input("Nhập vào tên sách: ")
        book_name = nice(book_name)
        dem = 1
        for book in Mylib.books:
            if book_name.lower() == book.title.lower():
                book.check_out()
                dem = 0
        if dem == 1:
            print("Không có sách với tiêu đề như vây.")
            print("Tìm kiếm sách có khả năng..")
            Mylib.search_book(book_name)
    if n==4:
        book_name = input("Nhập vào tên sách: ")
        book_name = nice(book_name)
        dem = 1
        for book in Mylib.books:
            if book_name.lower() == book.title.lower():
                book.return_book()
                dem = 0
        if dem == 1:
            print("Không có sách với tiêu đề như vây.")
            print("Tìm kiếm sách có khả năng..")
            Mylib.search_book(book_name)

    if n==5:
        book = Book(input("Name: "), input("Author: "), input("ibs number: "))
        Mylib.add_book(book)
        print(f"Đã thêm sách {book.name} của {book.author} có số ibs là {book.ibsn}")
        print("Nhập 1 để tiếp tục sử dụng, nhập phím khác để dừng lại")

    if n==6:
        book_name = input("Nhập vào tên sách: ")
        book_name = nice(book_name)
        dem = 1
        for book in Mylib.books:
            if book_name.lower() == book.title.lower():
                Mylib.remove_book(book)
                dem = 0
        if dem == 1:
            print("Không có sách với tiêu đề như vây.")
            print("Tìm kiếm sách có khả năng..")
            Mylib.search_book(book_name)

    if n==7:
        book_name = input("Nhập vào tên sách: ")
        book_name = nice(book_name)
        Mylib.search_book(book_name)
        time.sleep(10)
    if n==8:
        Mylib.display_book()
        time.sleep(5)

    if n==9:
        Mylib.display_available_book()
        time.sleep(5)
    if n==10:
        break
print("Cảm ơn đã sử dụng dịch vụ!")


