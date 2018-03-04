my_file=open('Test.txt','r')
content=my_file.read()
print(content)
my_file.close()
my_file=open('Test.txt','w')
my_file.write('I am Tanim.')
my_file.close()


my_file=open('Test.txt','a')
my_file.write('I am from Chandpur')
my_file.close()

my_file=open('Test.txt','r')
content=my_file.read(5)
print(content)
content=my_file.read()
print(content)
position=my_file.tell()
print(position)
my_file.seek(0,0)
content=my_file.read()
print(content)
my_file.close()

with open('Test.txt','r') as my_file:
    content=my_file.read()
    print(content)
