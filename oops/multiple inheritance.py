class Employee_Info :
    def __init__(self,name,emp_id) :
        self.name = name
        self.emp_id = emp_id
    def display_info(self):
        print(f'employee id: {self.emp_id},name : {self.name}')

class Employee_Benefits :
    def __init__(self,insurance,retairment_plan) :
        self.insurane = insurance
        self.retairment_plan = retairment_plan
    def display_benefits(self):
        print(f'insurance: {self.insurane},retairment plan : {self.retairment_plan}')
        
class Employee(Employee_Info,Employee_Benefits):
    def __init__(self, name, emp_id,insurance,retairment_plan):
        Employee_Info.__init__(self,name, emp_id)
        Employee_Benefits.__init__(self,insurance,retairment_plan)
        
employee1 = Employee("Aida",3486,"true","101(A)")
employee1.display_benefits()
employee1.display_info()
        
        