import time
import csv
from random import randint
class Book:
    def __init__(self,title,author,ibsn,quantity):
        self.title =title
        self.author = author
        self.ibsn = ibsn
        self.quantity=quantity
        self.checkoutbook=0
    def infor(self):
        print("Tựa đề sách là",self.title,"của",self.author,"với số ibs là",self.ibsn)
    def is_available(self):
        if self.quantity-self.checkoutbookk>0:
            print(f"{self.title} có sẵn {self.quantity-self.checkoutbook}!")
        else:
            print(f"{self.title} không có sẵn!")
    def check_out(self):
        if self.quantity-self.checkoutbook>0:
            print(f"{self.title} của bạn đây!")
            self.checkoutbook+=1
        else:
            print(f"{self.title} đã bị mượn hết!")
    def return_book(self):
        if self.checkoutbook>0:
            print(f"{self.title} đã được trả!")
            self.checkoutbook-=1
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
                print(f"{i}. {book.title} của {book.author} với số ibs là {book.ibsn}: {book.quantity} quyển")
                i+=1
        return matched_book

    def display_book(self):
        i=1
        for book in self.books:
            print(f"{i}. {book.title} của {book.author}: {book.quantity} quyển")
            i+=1
    def display_available_book(self):
        available_book=[book for book in self.books if book.quantity-book.checkoutbook>0]
        if len(available_book)==0:
            print("Không có sách nào có sẵn!")
        else:
            i=1
            for book in available_book:
                print(f"{i}. {book.title} của {book.author}: {book.quantity} quyển")
                i += 1
def nice(book_name):
    return " ".join(book_name.split())


Mylib=library()
with open('books.txt',encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) == 3:
            book = Book(row[0], row[1], row[2], randint(1,14))
            Mylib.add_book(book)
        elif len(row)>3:
            for i in range(1,len(row)-3):
                row[0]= row[0]+row[i]
            book = Book(row[0],row[-3], row[-2],randint(1,14))
            Mylib.add_book(book)

print("Chào mừng đến với thư viện của Đức Hùng!")
time.sleep(1)
print(f"Hiện tại bên mình đang có {len(Mylib.books)} đầu sách.")
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
    print("10. lịch sử mượn trả")
    time.sleep(0.1)
    print("11. thoát ra")

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
                f=open("checkout_history.txt",'a',encoding="utf-8")
                f.write(f"Đã mượn {book.title}\n")
                f.close()
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
                f.open("checkout_history.txt",'a',encoding="utf-8")
                f.write(f"Đã trả {book.title}")
                f.close()
                dem = 0
        if dem == 1:
            print("Không có sách với tiêu đề như vây.")
            print("Tìm kiếm sách có khả năng..")
            Mylib.search_book(book_name)

    if n==5:
        book = Book(input("Name: ").title(), input("Author: ").title(), input("ibs number: ").title())
        if book not in Mylib.books:
            Mylib.add_book(book)
            with open("books.txt", 'a', encoding="utf-8") as f:
                f.write(f"\n{book.title}, {book.author}, {book.ibsn}")
            print(f"Đã thêm sách {book.title} của {book.author} có số ibs là {book.ibsn}")
        else:
            print(f"Sách {book.title} của {book.author} đã có trong thư viện.")
        time.sleep(3)

    if n==6:
        book_name = input("Nhập vào tên sách: ")
        book_name = nice(book_name)
        dem = 1
        for book in Mylib.books:
            if book_name.lower() == book.title.lower():
                Mylib.remove_book(book)
                dem = 0
                print(f"Đã xóa sách {book.title}")
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
            f=open("checkout_history.txt",'r',encoding="utf-8")
            file=f.read()
            file=file.split("\n")
            dem=0
            for i in file:
                i=i.strip()
                if len(i)>0:
                    print(i)
                    dem+=1
            if dem==0:
                print("Lịch sử trống")

    if n==11:
        break
print("Cảm ơn đã sử dụng dịch vụ!")


