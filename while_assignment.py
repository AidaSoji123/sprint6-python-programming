bill1=[]
total=0
while True:
    item=int(input('Enter the value of the item:'))
    bill1.append(item)
    choice=input('Do you have more values to add?? press  y/n ')
    if choice.casefold()=='n':
        for i in bill1:
            total=total+i
        print('total: ',total)
    if total>2000:
        if total<5000:                               
            total=total-(total*12)/100
            print('total amount payable',total)
    if total>5000:
        if total<10000:
            total=total-(total*18)/100
            print('total amount payable',total)
    if total>10000:
        total=total-(total*25)/100
        print('total amount payable',total)
                
            
            
       
            