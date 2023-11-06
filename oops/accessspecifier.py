class Bank_Account:
    count=0
    def __init__(self,name,account_number,branch,ifsc_code,atm_pin,email,phone_number):
        self.name=name
        self.account_number=account_number
        self.branch=branch
        self.ifsc_code =ifsc_code
        self.__atm_pin = atm_pin    # private variable
        self.email=email
        self.phone_number=phone_number
        Bank_Account.count=Bank_Account.count+1
        
    def display_Bank_Account(self):
        print('name: ',self.name)
        print('account_number: ',self.account_number)
        print('branch: ',self.branch)
        print('ifsc_code: ',self.ifsc_code)
        print('ATM_PIN: ',self.__atm_pin)
        print('email: ',self.email)
        print('phone_number: ',self.phone_number)
        
    def Bank_Account_count(self):
        print('Total number of accounts: %d' %Bank_Account.count)
    
    def get_atm_pin(self):
        return self.__atm_pin
    
    def set_atm_pin(self,atm_pin):
        self.__atm_pin = atm_pin
        
Bank_Account1=Bank_Account("aida",55655677890,'edathanattukara' ,'sbin0008610',4488,'aidasoji1223@gmail.com',78964533560)
# Bank_Account1.display_Bank_Account()
# Bank_Account1.Bank_Account_count()
Bank_Account1.name = 'Aneena'
# Bank_Account1.display_Bank_Account()
        
# Bank_Account1.__atm_pin = 1122  
# Bank_Account1.display_Bank_Account()      
        
print(Bank_Account1._Bank_Account__atm_pin)  # name mangling method: no modification possible only accessing
print(Bank_Account1.name)
# print(Bank_Account1.__atm_pin)  # will not access using the dot operator bzs it is a private variable , modify using getter and setter
bank_account2 = Bank_Account("Aiby",33244556771,'kodanchery','fdrl00097',4445,"aiby2002@gmail.com",9556743211) 
print('display details of customer2')  
bank_account2.display_Bank_Account()
print('update atm pin ############################')
print(bank_account2.get_atm_pin())
print('new atm pin:################################## ')
bank_account2.set_atm_pin(7888)
print('updated details of customer2:################')
bank_account2.display_Bank_Account()
   