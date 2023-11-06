class Student:
    def __init__(self,name,age) :
        self.name = name
        self.age = age
    
    def displayDetails(self):
        print(f"name : {self.name}, Age : {self.age}")
    def study(self):
        print(f'{self.name} is studying ')
        
class UgStudent(Student):
    def study(self):
        print(f'{self.name} is studying hard for exams')
        
        
student1 = Student('Suma',30)
student2 = UgStudent('Reema',28)
print('Profile of student1') 
student1.displayDetails()
student1.study()
print('--------------------------------')
print('Profile of student2:')       
student2.displayDetails()
student2.study()