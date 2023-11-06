for i in range(1,6):
    for j in range(i):
        print('*',end="")
    print("\n")
    
    
star=[5,4,3,2,1]
for i in star:
    for j in range(i):
        print("*",end="")
    print('\n')


n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print('\n')
  
    