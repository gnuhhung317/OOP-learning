import time
import csv
from random import randint
class Book:
    #initial book object
    def __init__(self,title,author,ibsn,quantity,checkoutbook):
        self.title =title
        self.author = author
        self.ibsn = ibsn
        self.quantity=int(quantity)
        self.checkoutbook=int(checkoutbook)
    #check the information of the book:
    def infor(self):
        print("Tựa đề sách là",self.title,"của",self.author,"với số ibs là",self.ibsn)
    #check if the information is available
    def is_available(self):
        if self.quantity-self.checkoutbook>0:
            print(f"{self.title} có sẵn {self.quantity-self.checkoutbook}!")
        else:
            print(f"{self.title} không có sẵn!")
    #permit user checkout book
    def check_out(self,history):
        if int(self.quantity)-self.checkoutbook>0:
            print(f"{self.title} của bạn đây!")
            self.checkoutbook+=1
            print("Lịch sử mượn trả sẽ được cập nhật sau phiên làm việc")
            history.append(f"{time.ctime(time.time())} đã mượn {book.title}\n") #lưu lịch sử mượn vào list để thêm vào lưu vào csdl sau phiên làm việc
        else:
            print(f"{self.title} đã bị mượn hết!")
    #permit user return book
    def return_book(self,history):
        if self.checkoutbook>0:
            print(f"{self.title} đã được trả!")
            self.checkoutbook-=1
            print("lịch sử mượn trả sẽ được cập nhật sau phiên làm việc")
            history.append(f"{time.ctime(time.time())} đã trả {book.title}")
        else:
            print(f"{self.title} chưa được mượn!")
class library:
    #initial library
    def __init__(self):
        self.books=[]
    #add book to lib
    def add_book(self,book):
        self.books.append(book)
    #remove book from lib
    def remove_book(self,book):
        print("Cần quyền quản lý, mời nhập vào mã PIN: ")
        n=input()
        if n=="hungdeptraihaha":
            self.books.remove(book)
        else:
            print("Mã pin sai, dừng hoạt động.")
    #find book from lib (find book by title)
    def search_book(self,keyword=str):
        matched_book = [book for book in self.books if keyword.lower() in book.title.lower()]
        if len(matched_book)==0:
            print("Không tìm thấy sách.")
        else:
            print("Tìm được:")
            i=1
            for book in matched_book:
                print(f"{i}. {book.title} của {book.author} với số ibs là {book.ibsn}: {int(book.quantity)-book.checkoutbook} quyển")
                i+=1
        return matched_book
    #find book from lib(find book by author)
    def search_book1(self,keyword=str):
        matched_book = [book for book in self.books if keyword.lower() in book.author.lower()]
        if len(matched_book)==0:
            print("Không tìm thấy sách.")
        else:
            print("Tìm được:")
            i=1
            for book in matched_book:
                print(f"{i}. {book.title} của {book.author} với số ibs là {book.ibsn}: {int(book.quantity)-book.checkoutbook} quyển")
                i+=1
        return matched_book
    #show all book
    def display_book(self):
        i=1
        for book in self.books:
            print(f"{i}. {book.title} của {book.author}: {book.quantity} quyển")
            i+=1
    #show all available book
    def display_available_book(self):
        available_book=[book for book in self.books if book.quantity-book.checkoutbook>0]
        if len(available_book)==0:
            print("Không có sách nào có sẵn!")
        else:
            i=1
            for book in available_book:
                print(f"{i}. {book.title} của {book.author}: {book.quantity} quyển")
                i += 1
#make name book in good form
def nice(book_name):
    return " ".join(book_name.split())


Mylib=library()
with open('books.txt') as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) == 5:
            book = Book(row[0].strip(), row[1].strip(), row[2].strip(), row[3].strip(),row[4].strip())
            Mylib.add_book(book)
        elif len(row)>5:
            for i in range(1,len(row)-5):
                row[0]= row[0]+row[i]
            book = Book(row[0].strip(),row[-4].strip(),row[-3].strip(), row[-2].strip(),row[-1].strip())
            Mylib.add_book(book)
print("Chào mừng đến với thư viện của Đức Hùng!")
time.sleep(1)
print(f"Hiện tại bên mình đang có {len(Mylib.books)} đầu sách.")
time.sleep(1)
history=[]
while True:
    print("Bạn muốn làm gì nào?")
    time.sleep(1)
    print("1. tìm thông tin sách")
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

    n=int(input("Nhập vào lựa chọn của bạn(1-11): "))
    dem=1
    while n<1 or n>11:
        n = int(input(f"Lựa chọn không hợp lệ, mời nhập lại({dem}/5): "))
        dem+=1
        if dem==6:
            break
    if n==1:
        #find the book infor
        print("Nhập 1 để tìm theo tiêu đề sách, 2 để tìm theo tên tác giả: ")
        a=int(input())
        for i in range(1,6):
            if a!="1" and a!="2":
                a=input("Đầu vào không hợp lệ, mời nhập lại")
            else:
                break
        if a==1:
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
        if a==2:
            book_author=input("Nhập vào tên tác giả: ")
            book_author=nice(book_author)
            dem=1
            for book in Mylib.books:
                if book_author.lower()== book.author.lower():
                    book.infor()
                    dem=0
            if dem>0:
                print("Không có tác giả nào tên như thế á!")
    #check_available
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
    #check out book
    if n==3:
        book_name = input("Nhập vào tên sách: ")
        book_name = nice(book_name)
        dem = 1
        for book in Mylib.books:
            if book_name.lower() == book.title.lower():
                book.check_out(history)
                dem=0
                break
        if dem == 1:
            print("Không có sách với tiêu đề như vây.")
            print("Tìm kiếm sách có khả năng..")
            Mylib.search_book(book_name)
    #return book
    if n==4:
        book_name = input("Nhập vào tên sách: ")
        book_name = nice(book_name)
        dem = 1
        for book in Mylib.books:
            if book_name.lower() == book.title.lower():
                book.return_book(history)
                dem=0
        if dem == 1:
            print("Không có sách với tiêu đề như vây.")
            print("Tìm kiếm sách có khả năng..")
            Mylib.search_book(book_name)
    #add book
    if n==5:
        book = Book(input("Name: ").title(), input("Author: ").title(), input("ibs number: ").title())
        if book not in Mylib.books:
            Mylib.add_book(book)
            with open("books.txt", 'a') as f:
                f.write(f"\n{book.title}, {book.author}, {book.ibsn}, {book.quantity}, {book.checkoutbook}")
            print(f"Đã thêm sách {book.title} của {book.author} có số ibs là {book.ibsn}: {book.quantity}")
        else:
            print(f"Sách {book.title} của {book.author} đã có trong thư viện.")
        time.sleep(3)
    #delete book
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
    #seach book
    if n==7:
        a=input("Nhập 1 để tìm sách theo tên,2 để tìm sách theo tác giả: ")
        if a=="1":
            book_name=input("Nhập vào tên sách: ")
            Mylib.search_book(book_name)
        elif a=="2":
            book_author=input("Nhập vào tên tác giả: ")
            Mylib.search_book1(book_author)
        else:
            print("Nhập vào không hợp lệ, dừng tiến trình.")
    #show all books
    if n==8:
        Mylib.display_book()
        time.sleep(5)
    #show available books
    if n==9:
        Mylib.display_available_book()
        time.sleep(5)
    #show  checkouted history
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
    #stop using service
    if n==11:
        break
#save the changes
with open('books.txt', 'w') as file:
    for book in Mylib.books:
        file.write(f"{book.title}, {book.author}, {book.ibsn}, {book.quantity}, {book.checkoutbook}\n")
with open("checkout_history.txt","a",encoding="utf-8") as f:
    for i in history:
        f.write(i+"\n")
print("Cảm ơn đã sử dụng dịch vụ!")


