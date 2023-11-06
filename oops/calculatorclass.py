class Calculator:
    def add(self,num1,num2):
        return num1 + num2
    def substract(self,num1,num2):
        return num1 - num2
    def multiply(self,num1,num2):
        return num1 * num2
    def division(self,num1,num2):
        if num2 != 0 :
            return num1 / num2
        else :
            return ('cannot divisible by zero.') 
        
calculator1 = Calculator()
result = calculator1.add(232,3)

print("the addition value of 232 & 3 is :",result)

result = calculator1.substract(232,3)

print("the substraction value of 232 & 3 is :",result)

result = calculator1.multiply(232,3)

print("the multiplication value of 232 & 3 is :",result)

result = calculator1.division(232,0)

print("the division value of 232 & 0 is :",result)
            