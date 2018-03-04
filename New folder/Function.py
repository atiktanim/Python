'''
def add(**args):
    print(type(args))
    tmp=0
    for value in args:
        tmp=tmp+args[value]
    return tmp
temp=add(a=1,b=2,c=3,d=4)
print(temp)


def factorial(n):
    temp=n
    while n>1:
        n-=1
        temp=temp*n
    return temp
print('Enter value for factorial')
num=int(input())
if num==0:
    print(1)
else:
    print(factorial(num))

def factorial1(n):
    if n==0:
       return 1
    else:
        return  factorial1(n-1)*n
print('Enter the input')
number=int(input())
print(factorial1(number))

sum=lambda a,b:a+b
print(sum(10,20))
        
'''
'''
def my_function(func,arg1,arg2):
    return func(arg1,arg2)
print(my_function(lambda a,b:a+b,10,20))

my_list=[2,3,4,6,7,9]
def square(x):
    return x*x
new_list=map(square,my_list)
print(new_list)
print(list(new_list))
'''
a,b=map(int,input().split())
#print(a)
print(b+a)






















    
