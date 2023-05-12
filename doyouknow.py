import time
import hashlib
import os

class Book:
    #initial book object
    def __init__(self,title,author,ibsn,quantity,checkoutbook):
        self.title =title
        self.author = author
        self.ibsn = ibsn
        self.quantity=int(quantity) #số lượng sách
        self.checkoutbook=int(checkoutbook) #số lượng sách đã bị mượn
    #check the information of the book:
    def infor(self):
        print("Tựa đề sách là",self.title,"của",self.author,"với số ibs là",self.ibsn)
    #check if the information is available
    def is_available(self):
        if self.quantity-self.checkoutbook>0: #kiểm tra số sách hiện tại
            print(f"{self.title} có sẵn {self.quantity-self.checkoutbook}!")
        else:
            print(f"{self.title} không có sẵn!")
    #permit user checkout book
    def check_out(self,history):
        if int(self.quantity)-self.checkoutbook>0:
            print(f"{self.title} của bạn đây!")
            self.checkoutbook+=1 #tăng số sách self bị mượn thêm 1
            print("Lịch sử mượn trả sẽ được cập nhật sau phiên làm việc")
            history.append(f"{time.ctime(time.time())} {username} đã mượn {book.title}") #lưu lịch sử mượn vào list để thêm vào lưu vào csdl sau phiên làm việc
        else:
            print(f"{self.title} đã bị mượn hết!")
    #permit user return book
    def return_book(self,history):
        if self.checkoutbook>0:
            print(f"{self.title} đã được trả!")
            self.checkoutbook-=1 #giảm số sách self bị giảm thêm 1#
            print("lịch sử mượn trả sẽ được cập nhật sau phiên làm việc")
            history.append(f"{time.ctime(time.time())} {username} đã trả {book.title}") #lưu lịch sử mượn vào list để thêm vào lưu vào csdl sau phiên làm việc
        else:
            print(f"{self.title} chưa được mượn cuốn nào cả!")
class library:
    #initial library
    def __init__(self):
        self.books=[]
    #add book to lib
    def add_book(self,book):
        self.books.append(book)
    #remove book from lib
    def remove_book(self,book):
        self.books.remove(book)
        print(f"Đã xóa sách {book.title}")
    #find book from lib (find book by title)
    def search_book(self,keyword=str):
        matched_book = [book for book in self.books if keyword.lower() in book.title.lower()]
        if not matched_book:
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
            print("Không tìm thấy tác giả.")
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
        available_book=[book for book in self.books if book.quantity-book.checkoutbook>0] #tạo danh sách sách có số quyển sách hiện có lớn hơn 0
        if len(available_book)==0:
            print("Không có sách nào có sẵn!")
        else:
            i=1
            for book in available_book:
                print(f"{i}. {book.title} của {book.author}: {book.quantity} quyển")
                i += 1
#class Login to login

class Login:
    def __init__(self,username,password): #khởi tạo class Login với 2 biến username và password
        self.username=username
        self.password=password
class userlogin(Login): #Tạo class login cho người dùng
    def __init__(self,username,password,user_data):
        super().__init__(username,password) #truyển vào từ class Login
        self.user_data=user_data #truyền dict dữ liệu người dùng gồm tài khoản và chuỗi hash mật khẩu
    def login(self):
        if self.user_data[self.username]==get_sha256_hash(self.password): #kiểm tra mật khẩu sau khi hash có giống trong từ điển dữ liệu người dúng không
            print("Người dùng đăng nhập thành công")
            return True
        print("Tài khoản hoặc mật khẩu không chính xác!")
        return False
class adminlogin(Login):
    def __init__(self,username,password,admin_data):
        super().__init__(username,password)
        self.admin_data=admin_data
    def login(self):
        if self.admin_data[self.username]==get_sha256_hash(self.password):
            print("Quản trị viên đăng nhập thành công")
            return True
        print("Tài khoản hoặc mật khẩu không chính xác!")
        return False
#make name book in good form
def nice(book_name):
    return " ".join(book_name.split())

#hash the password
def get_sha256_hash(data):
    hash_object = hashlib.sha256(data.encode())
    return hash_object.hexdigest()

def working(book_name,a):
    book_name = nice(book_name)
    dem = 1
    for book in Mylib.books:
        if book_name.lower() == book.title.lower():
            if a==2:
                book.is_available()
            elif a==1:
                book.infor()
            elif a==3:
                book.check_out(history)
            elif a==4:
                book.return_book(history)
            elif a==6:
                Mylib.remove_book(book)
            dem = 0
    if dem == 1:
        print("Không có sách với tiêu đề như vây.")
        print("Tìm kiếm sách có khả năng..")
        Mylib.search_book(book_name)

Mylib=library()
#tạo một từ điển chứa tài khoản và mật khẩu (sau khi đã hash) của người dùng từ file user.txt
with open("user.txt","r") as f:
    data=f.read()
data=data.split("\n")
for i in range(len(data)):
    data[i]=data[i].split(", ")
user_data={username: password for [username,password] in data }
#tạo một từ điển chứa tài khoản và mật khẩu(sau khi đã hash của người dùng từ file admin.txt
with open("admin.txt","r") as f:
    data=f.read()
    data=data.split("\n")
    for i in range(len(data)):
        data[i]=data[i].split(", ")
    admin_data={admin: password for [admin,password] in data }
#tạo một danh sách các đối tượng sách, sau đó thêm sách vào đối tượng Mylib
with open('books.txt','r',encoding="utf-8") as file:
    file=file.read()
    file=file.split("\n")
    for i in range(len(file)):
        file[i]=file[i].split(", ")
    for row in file:
        if len(row) == 5:
            book = Book(row[0].strip(), row[1].strip(), row[2].strip(), row[3].strip(),row[4].strip())
            Mylib.add_book(book)
        elif len(row)>5:    #chia 2 trường hợp vì tiêu đề sách có thể chứa dấu phẩy
            for i in range(1,len(row)-5):
                row[0]= row[0]+row[i]
            book = Book(row[0].strip(),row[-4].strip(),row[-3].strip(), row[-2].strip(),row[-1].strip())
            Mylib.add_book(book)
#mở lịch sử đến phiên làm việc lần trước
f=open("checkout_history.txt",'r',encoding="utf-8")
histo=f.read()
histo=histo.split("\n")
# tạo danh sách rỗng lưu lại lịch sử mượn trả từng tiến trình để ghi vào checkout_history
history=[]
print("Chào mừng đến với thư viện của Đức Hùng!")
time.sleep(1)
print(f"Hiện tại bên mình đang có {len(Mylib.books)} đầu sách.")
time.sleep(1)
#Đăng nhập hệ thống
print("Mời đăng nhập. ")
count=1
admin=False
user=False
"""các biến chính:
histo: danh sách chứa lịch sử mượn trả các phiên làm việc chứa
history: danh sách chưa lịch sử mượn trả phiên làm việc hiện tại
user_data: từ điển chứa từ khóa là username với định nghĩa là password sau khi hash
admin_data: Tương tự user_data nhưng của admin
admin và user khởi tạo và gán giá trị True khi đăng nhập bằng phương thức của 2 class"""
while count<6:
    username=input("username: ")
    password=input("password: ")
    userlog=userlogin(username,password,user_data)
    adminlog=adminlogin(username,password,admin_data)
    if username in user_data:
        if userlog.login()==False:
            continue
        user=True
        os.system('cls')
        break
    elif username in admin_data:
        if adminlog.login()==False:#kiểm tra đăng nhập thành công không
            continue
        admin=True
        os.system('cls')
        break
    else:
        print(f"Tài khoản hoặc mật khẩu không chính xác({count}/5)")
        count+=1
        os.system('cls')
#nhập vào lựa chọn
while count<6:## bỏ qua các chức năng khi đăng nhập 5 lần
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
        os.system('cls')
        if dem==6:
            break
    if n==1:
        #find the book infor
        print("Nhập 1 để tìm theo tiêu đề sách, 2 để tìm theo tên tác giả: ")
        a=input()
        for i in range(1,6):
            if a!="1" and a!="2":
                a=input("Đầu vào không hợp lệ, mời nhập lại")
            else:
                break
        os.system('cls')

        if a=="1":
            book_name = input("Nhập vào tên sách: ")
            working(book_name,n)

        if a=="2":
            book_author=input("Nhập vào tên tác giả: ")
            book_author=nice(book_author)
            dem=1
            for book in Mylib.books:
                if book_author.lower()== book.author.lower():
                    book.infor()
                    dem=0
            if dem == 1:
                print("Không tìm thấy sách của tác giả như vây.")
                print("Tìm kiếm tên tác giả có khả năng..")
                Mylib.search_book1(book_author)

        #về menu chính hoặc dừng sử dụng
        check= input("Nhập 1 để tiếp tục sử dụng, nhập bất kì để thoát: ")
        if check == "1":
            os.system('cls')
            continue
        else:
           break
    #check_available

    if n==2:
        book_name = input("Nhập vào tên sách: ")
        working(book_name,n)
        # về menu chính hoặc dừng sử dụng
        check = input("Nhập 1 để tiếp tục sử dụng, nhập bất kì để thoát: ")
        if check == "1":
            os.system('cls')
            continue
        else:
            os.system('cls')
            break
    #check out book
    if n==3:
        book_name = input("Nhập vào tên sách: ")
        working(book_name,3)
        # về menu chính hoặc dừng sử dụng
        check = input("Nhập 1 để tiếp tục sử dụng, nhập bất kì để thoát: ")
        if check == "1":
            os.system('cls')
            continue
        else:
            os.system('cls')
            break
    #return book
    if n==4:
        book_name = input("Nhập vào tên sách: ")
        working(book_name,n)
        # về menu chính hoặc dừng sử dụng
        check = input("Nhập 1 để tiếp tục sử dụng, nhập bất kì để thoát: ")
        os.system('cls')
        if check == "1":
            continue
        else:
            break

    #add book
    if n==5:
        if admin:
            book = Book(input("Name: ").title(), input("Author: ").title(), input("ibs number: ").title(),input("quantity: ".title()),input("checkoutnumber: ").title())
            if book not in Mylib.books:
                Mylib.add_book(book)
                print(f"Đã thêm sách {book.title} của {book.author} có số ibs là {book.ibsn}: {book.quantity}")
            else:
                print(f"Sách {book.title} của {book.author} đã có trong thư viện.")

        else:
            print("Cần quyền quản trị viên để thêm sách")
        # về menu chính hoặc dừng sử dụng
        check = input("Nhập 1 để tiếp tục sử dụng, nhập bất kì để thoát: ")
        os.system('cls')
        if check == "1":
            continue
        else:
            break
    #delete book
    if n==6:
        if admin:
            book_name = input("Nhập vào tên sách: ")
            working(book_name,n)

        else:
            print("Cần quyền quản trị viên")
        # về menu chính hoặc dừng sử dụng
        check = input("Nhập 1 để tiếp tục sử dụng, nhập bất kì để thoát: ")
        os.system('cls')
        if check == "1":
            continue
        else:
            break
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
            print("Nhập vào không hợp lệ, về menu chính.")
        # về menu chính hoặc dừng sử dụng
        check = input("Nhập 1 để tiếp tục sử dụng, nhập bất kì để thoát: ")
        os.system('cls')
        if check == "1":
            continue
        else:
            break

    #show all books
    if n==8:
        print("Danh sách sách trong thư viện là: ")
        Mylib.display_book()
        # về menu chính hoặc dừng sử dụng
        check = input("Nhập 1 để tiếp tục sử dụng, nhập bất kì để thoát: ")
        os.system('cls')
        if check == "1":
            continue
        else:
            break
    #show available books
    if n==9:
        print("Danh sách sách có sẵn là: ")
        Mylib.display_available_book()
        # về menu chính hoặc dừng sử dụng
        check = input("Nhập 1 để tiếp tục sử dụng, nhập bất kì để thoát: ")
        os.system('cls')
        if check == "1":
            continue
        else:
            break
    #show checkouted history
    if n==10:
        dem=0
        for i in histo:
            i=i.strip()
            if len(i)>0:
                print(i)
                dem+=1
        if dem==0:
            print("Lịch sử trống")
        # về menu chính hoặc dừng sử dụng
        check = input("Nhập 1 để tiếp tục sử dụng, nhập bất kì để thoát: ")
        os.system('cls')
        if check == "1":
            continue
        else:
            break
    #stop using service
    if n==11:
        break
print("Cảm ơn đã sử dụng dịch vụ!")
#save the changes
with open('books.txt', 'w') as file:
    for book in Mylib.books:
        file.write(f"{book.title}, {book.author}, {book.ibsn}, {book.quantity}, {book.checkoutbook}\n") #ghi lại dữ liệu hiện tại của Mylib
with open("checkout_history.txt","a",encoding="utf-8") as f:
    for i in history:
        f.write(i+"\n") #ghi tiếp lịch sử mượn trả phiên làm việc



