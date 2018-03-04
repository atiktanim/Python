class Calculator:
    def addition(self,a,b):
        return a+b
    def subtraction(self,a,b):
        return a-b
    def multipliication(self,a,b):
        return a*b
    def division(self,a,b):
        try:
            return a/b
        except ZeroDivisionError:
            return 'Not Possible to devide by zero'

'''
my_calculator=Calculator()
temp=my_calculator.addition(12,78)
print(temp)

temp=my_calculator.division(43,0)
print(temp)

'''
class SuperCalculator(Calculator):
    def square(self,a):
        return a*a
    def cube(self,a):
        return a*a*a
my_calculator=SuperCalculator()
temp=my_calculator.subtraction(100,500)
print(temp)
