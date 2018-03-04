
def add(*args):
	print(type(args))
	tmp=0
	for number in args:
		tmp=tmp+number
	return tmp
def factorial(number):
    if number==0:
        return 1
    else:
        return number*factorial(number-1)
print("Plese enter the number")
number=int(input())
print(factorial(number))
