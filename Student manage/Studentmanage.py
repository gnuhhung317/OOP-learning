from manage import *
manage=StudentManagement()
print("Hệ thống quản lí sinh viên....")
print(f"Hiện tại có {len(manage.StudentList)} sinh viên")
while True:
    print("1.Xem thông tin toàn bộ sinh viên\n2.Xóa sinh viên theo tên\n3.Xóa sinh viên theo số thứ tự\n4.Xem điểm trung bình của sinh viên\n5.Sắp xếp theo tuổi\n6.Sắp xếp theo tên\n7.Thay đổi thông tin sinh viên\n8.Thêm sinh viên\n9.Thoát")
    choice=input("Mời lựa chọn: ")
    if choice =="1":
        manage.ShowAll()
    elif choice =="2":
        name=input()
        manage.DeleteStudentbyName(name)
    elif choice =="3":
        serial=input()
        if serial.isdigit():
            manage.DeleteStudentbyserial(int(serial))
        else:
            print("Serial invalid")
    elif choice =="4":
        manage.AverageGpa()
    elif choice =="5":
        manage.SortAge()
    elif choice=="6":
        manage.SortName()
    elif choice=="7":
        manage.ChangeInfobySerial()
    elif choice == "8":
        
        name=input("Mời nhập vào tên: ")
        age=input("Mời nhập vào tuổi: ")
        gpa=input("Mời nhập vào gpa: ")
        while not age.isdigit():
            age=input("Mời nhập lại tuổi: ")
        while len(gpa)>4 or not gpa[0].isdigit() or not gpa[-1].isdigit() or gpa[1]!=".":
            gpa=input("Mời nhập lại gpa: ")
        stu=Student(name,age,gpa)
        if stu not in manage.StudentList:
            manage.AddStudent(stu)
        
        
    elif choice == "9":
        with open("student.txt","w") as file:
            for stu in manage.StudentList:
                file.write(f"{stu.name}, {stu.age}, {stu.gpa}\n")
        break
    else:
        print("Invalid entry")
    if not Continue():
        with open("student.txt","w") as file:
            for stu in manage.StudentList:
                file.write(f"{stu.name}, {stu.age}, {stu.gpa}\n")
        break
manage.SaveData()