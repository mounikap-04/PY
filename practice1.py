class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        if b == 0:
            return 0
        return a/b
cal=Calculator()
print(cal.add(1,2))
print(cal.sub(1,2))
print(cal.mul(1,2))
print(cal.div(1,2))




