import hashlib
import time
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
    def check_out(self,history,username,book):
        if int(self.quantity)-self.checkoutbook>0:
            print(f"{self.title} của bạn đây!")
            self.checkoutbook+=1 #tăng số sách self bị mượn thêm 1
            print("Lịch sử mượn trả sẽ được cập nhật sau phiên làm việc")
            history.append(f"{time.ctime(time.time())} {username} đã mượn {book.title}") #lưu lịch sử mượn vào list để thêm vào lưu vào csdl sau phiên làm việc
        else:
            print(f"{self.title} đã bị mượn hết!")
    #permit user return book
    def return_book(self,history,username,book):
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
    def login(self,username,password,user_data,admin_data):
        if username in user_data and user_data[username]==get_sha256_hash(password): #kiểm tra mật khẩu sau khi hash có giống trong từ điển dữ liệu người dúng không
            print("Người dùng đăng nhập thành công")

            return True

        elif username in admin_data and admin_data[username]==get_sha256_hash(password):
            print("Quản trị viên đăng nhập thành công")

            return True

        return False
    def display_menu(self,is_admin):

        options = [
            "1. Tìm thông tin sách",
            "2. Xem sách có sẵn hay không",
            "3. Mượn sách",
            "4. Trả sách",
            "5. Tìm sách",
            "6. Hiển thị toàn bộ sách",
            "7. Hiển thị sách khả dụng",
            "8. Lịch sử mượn trả",
            "9. Thêm sách",
            "10. Xóa sách",
            "Nhập bất kì để thoát ra"
        ]
        for option in options:
            if option[0]=="9" or option[0:2]=="10":
                if is_admin:
                    print(option)
                else:
                    continue
            else:
                print(option)
            time.sleep(0.2)

    #add book to lib
    def add_book(self,book):
        self.books.append(book)
    #remove book from lib
    def remove_book(self,book):
        self.books.remove(book)
        print(f"Đã xóa sách {book.title}")
    #find book from lib (find book by title)
    def search_book_by_title(self,keyword=str):
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
    def search_book_by_author(self,keyword=str):
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


def nice(book_name):
    return " ".join(book_name.split())

#hash the password
def get_sha256_hash(data):
    hash_object = hashlib.sha256(data.encode())
    return hash_object.hexdigest()