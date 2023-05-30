
import os
from classlib import *
#make name book in good form


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
                book.check_out(history,username,book)
            elif a==4:
                book.return_book(history,username,book)
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

"""các biến chính:
histo: danh sách chứa lịch sử mượn trả các phiên làm việc chứa
history: danh sách chưa lịch sử mượn trả phiên làm việc hiện tại
user_data: từ điển chứa từ khóa là username với định nghĩa là password sau khi hash
admin_data: Tương tự user_data nhưng của admin
admin và user khởi tạo và gán giá trị True khi đăng nhập bằng phương thức của 2 class"""
while count<6:
    username=input("username: ")
    password=input("password: ")
    mylog=Mylib.login(username,password,user_data,admin_data)
    if username in user_data:
        if  mylog == False:
            continue
        os.system('cls')
        break
    elif username in admin_data:
        if mylog ==False:#kiểm tra đăng nhập thành công không
            continue
        admin=True
        os.system('cls')
        break
    else:
        print(f"Tài khoản hoặc mật khẩu không chính xác({count}/5)")
        count+=1
        os.system('cls')
#nhập vào lựa chọn
while True:
    Mylib.display_menu(admin)
    n=input("Nhập vào lựa chọn của bạn: ")
    os.system('cls')
    if n.isdigit():
        n=int(n)
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
    if n==9:
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
    if n==10:
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
    if n==5:
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
    if n==6:
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
    if n==7:
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
    if n==8:
        dem=0
        for i in histo:
            i=i.strip()
            if len(i)>0:
                print(i)
                dem+=1
        if dem==9:
            print("Lịch sử trống")
        # về menu chính hoặc dừng sử dụng
        check = input("Nhập 1 để tiếp tục sử dụng, nhập bất kì để thoát: ")
        os.system('cls')
        if check == "1":
            continue
        else:
            break
    #stop using service
    else:
        break
print("Cảm ơn đã sử dụng dịch vụ!")
#save the changes
with open('books.txt', 'w') as file:
    for book in Mylib.books:
        file.write(f"{book.title}, {book.author}, {book.ibsn}, {book.quantity}, {book.checkoutbook}\n") #ghi lại dữ liệu hiện tại của Mylib
with open("checkout_history.txt","a",encoding="utf-8") as f:
    for i in history:
        f.write(i+"\n") #ghi tiếp lịch sử mượn trả phiên làm việc



