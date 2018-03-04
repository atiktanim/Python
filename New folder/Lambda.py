sum=lambda a,b:a+b
print(sum(10,20))
print((lambda a,b:a+b)(10,20))
my_list=[2,3,4,5,6,7]
def square(x):
    return x*x
new_list=map(square,my_list)
print(new_list)
print(list(new_list))

my_list=[2,3,4,5,6,7]
def is_even(x):
    if(x%2)==0:
        return True
    else:
        return False
new_list=filter(is_even,my_list)
print(new_list)
print(list(new_list))

