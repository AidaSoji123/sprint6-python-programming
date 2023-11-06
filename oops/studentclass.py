class Students:
    def __init__(self,name,age,mark):
        self.name = name
        self.age = age
        self.mark = mark
        
    def getGrade(self):
        if self.mark >= 90:
           return "A"
        elif self.mark >= 80:
            return "B"
        elif self.mark >= 70:
            return "C"
        elif self.mark >=60:
            return "D"
        else:
            return "F"
        
student = [
    Students("Aida",28,70),
    Students("Aiby",23,89),
    Students("Aneena",21,98),
    Students('Adona',16,56)
]

for x in student:
    print(f'name : {x.name},Age : {x.age}, mark : {x.mark}, Grade : {x.getGrade()} ')
        
       
        