'''
n=1
temp=0
while n<=100:
    temp=temp+n
    n=n+1
print(temp)
a=['Onion','Potato','Ginger','Cucumber']
print(type(a))
for item in a:
    print(item)
a={'Name':'Md. Atikur Rahman','Nickname':'Tanim','Email:':'Atik.tanim14@gmail.com','Phone':'01521233718'}
print(a)
print(type(a))
for item in a:
    print(item)
for item in a:
    print(item,a[item])

for number in range(1,11):
        if number==5:
            continue
        print(number)
print('Enter the value')
number=int(input())
count=1

while count<=10:
    print(number,'X',count,'=',number*count)
    count=count+1
print('Enter the input')
word=input()
word=word.casefold()
reversed_word=word[::-1]
if word==reversed_word:
    print('Great!,its a peliindrome')
else:
    print('Lol!,its not a pelindrome')
'''

my_list=[1,3,5,7,11,13,15,17,20,26,31,44,54,56,65,77,94,100]
print('Input the number')

number=int(input())
first=0
last=len(my_list)-1
print(last)
found=False
cycle=0
while first<=last and not found:
    midpoint=(first+last)//2
    if my_list[midpoint]==number:
        found==True
        cycle=cycle+1
        break
    elif number<my_list[midpoint]:
        last=midpoint-1
    else:
        first=midpoint+1
    cycle=cycle+1

print('Found after',cycle,'cycle')
    
