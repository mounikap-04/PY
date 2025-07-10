class Calculator:
    def add(self,a,b):
        return a+b       #used to add two numbers
    def sub(self,a,b):
        return a-b        #used to subtract two numbers
    def mul(self,a,b):
        return a*b       #used to multiply two numbers
    def div(self,a,b):
        if b == 0:
            return 0
        return a/b
cal=Calculator()
print("addition(1,2):",cal.add(1,2))
print("subtraction(1,2):",cal.sub(1,2))
print("multiply(1,2):",cal.mul(1,2))
print("division(1,2):",cal.div(1,2))





