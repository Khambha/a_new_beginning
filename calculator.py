import math

class Calculator:

    def __init__(self,a,b) :
        print("Welcome to calculator")
        self.a=a
        self.b=b

    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        try:
          return self.a/self.b
        except ZeroDivisionError:
            print("Division cannot be done by zero")  
    def sqrt(self):
        return math.sqrt(self.a)

a=int(input("Enter a value for calculation"))      
b=int(input("Enter another value for calculation")) 
cl=Calculator(a,b)             
print(cl.add())
print(cl.sub())
print(cl.mul())
print(cl.div())
print(cl.sqrt())

        
        

  


