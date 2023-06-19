class Person:
    def __init__(self,id,name,birthday,address,height,weight):
        self.id =id
        self.name=name
        self.birthday = birthday
        self.address = address
        self.height = height
        self.weight = weight
class Student(Person):
    def __init__(self,student_code,school,start_year,CPA):
        super.__init__()
        self.student_code=student_code
        self.school= school
        self.start_year=start_year
        self.CPA= CPA
class Manage:
    def __init__(self):
        self.students=[]
class Check(Student):
    def __init__(self):
        super().__init__()
    



