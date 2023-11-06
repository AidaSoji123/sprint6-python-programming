class Employees :
    def __init__(self) :
        print('parent class') 
    def display_details(self):
        print('Welcome to the Organization')
    def homepage(self) :
        print('Welcome')
    
class Accountant(Employees):   # child class
    def __init__(self):
        super().__init__()
        print('The child class')
    def accountant_Profile(self) :
        print('Welcome to accounts department')
    def homepage(self):
        print('Welcome to accountant homepage')
        
        
class Head(Accountant) :
    def __init__(self):
        super().__init__()
        print('Accounts head')
    

accountant1 = Accountant()
accountant1.display_details()
accountant1.accountant_Profile()
accountant1.homepage()

head1 = Head()    # multilevel inheritance





       
   
       
 