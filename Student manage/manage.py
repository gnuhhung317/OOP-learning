class Student:
    def __init__(self,name,age,gpa):
        self.name=name
        self.age=age
        self.gpa=gpa
    def showinfo(self):
        return f"{self.name}, {self.age} years old, GPA {self.gpa}"
    def changeinfo(self):
        options=input("Choose the attibute you want to change:\n1.Name\n2.age\n3.gpa\n")
        if options=="1" :
            print("Enter the new name of",self.showinfo())
            self.name=input()
        if options=="2":
            print("Enter the new age of",self.showinfo())
            self.age=input()
        if options=="3":
            print("Enter the new GPA",self.showinfo())
            self.gpa==input()
class StudentManagement:
    def __init__(self):
        self.StudentList=[]
        with open("student.txt","r",encoding="utf-8") as file:
            data=file.read()
            data=data.split("\n")
            
            for i in range(len(data)):
                if data[i]=="":
                    continue
                data[i]=data[i].split(", ")
                student=Student(data[i][0],data[i][1],data[i][2])
                self.StudentList.append(student)
    def DeleteStudentbyserial(self,serial):
        if serial>len(self.StudentList):
            print(f"Can't find this serial {serial}")
            return 0
        print(f"Removed {self.StudentList[serial].showinfo()}")
        self.StudentList.pop(serial-1)
        
    def DeleteStudentbyName(self,name=str):
        check=True
        for Student in self.StudentList:
            if Student.name.lower()==name.lower():
                self.StudentList.remove(Student)
                print(f"{self.StudentList.index(Student)+1}",Student.showinfo())
                
                check=False
        if check:
            print(f"Can't find {name}")
    def AddStudent(self,student):
        self.StudentList.append(student)
        print(f"Added",student.showinfo())
    def ShowAll(self):
        print("Student list:")
        for index in range(len(self.StudentList)):
            print(f"{index+1}:",self.StudentList[index].showinfo())
    def AverageGpa(self):
        AGpa=sum(float(student.gpa) for student in self.StudentList)/len(self.StudentList)
        print("Average GPA of Student is",AGpa)
    def SortAge(self):
        SortAgeList=sorted(self.StudentList,key=lambda student:student.age)
        print("Sorted student list:")
        for index in range(len(self.StudentList)):
            print(f"{index+1}:",SortAgeList[index].showinfo())
    def SortName(self):
        SortNameList=sorted(self.StudentList,key=lambda student : student.age)
        print("Sorted student list:")
        for index in range(len(self.StudentList)):
            print(f"{index+1}:",SortNameList[index].showinfo())
    def SaveData(self):
        with open("student.txt","w",encoding="utf-8") as data:
            for student in self.StudentList:
                data.write(f"\n{student.name}, {student.age}, {student.gpa}")
    def ChangeInfobySerial(self):
        serial = input("Enter serial:")
        if not serial.isdigit():
            print("Invalid serial!")
            return 0
        self.StudentList[int(serial)-1].changeinfo()
def Continue():
    n=input("Do u wanna continue (y/n)?")
    if n=="y":
        return True
    else:
        return False