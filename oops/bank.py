class Bank_Account:
    count=0
    def __init__(self,name,account_number,branch,ifsc_code,atm_pin,email,phone_number):
        self.name=name
        self.account_number=account_number
        self.branch=branch
        self.ifsc_code=ifsc_code
        self.atm_pin=atm_pin
        self.email=email
        self.phone_number=phone_number
        Bank_Account.count=Bank_Account.count+1
        
    def display_Bank_Account(self):
        print('name: ',self.name)
        print('account_number: ',self.account_number)
        print('branch: ',self.branch)
        print('ifsc_code: ',self.ifsc_code)
        print('ATM_PIN: ',self.atm_pin)
        print('email: ',self.email)
        print('phone_number: ',self.phone_number)
        
    def Bank_Account_count(self):
        print('Total number of accounts: %d' %Bank_Account.count)
        
Bank_Account1=Bank_Account("aida",55655677890,'edathanattukara' ,'sbin0008610',6754488,'aidasoji1223@gmail.com',78964533560)
Bank_Account1.display_Bank_Account()
Bank_Account1.Bank_Account_count()

        
  
        
        
   