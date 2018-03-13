'''

helloFile=open("Love.txt")
#helloContent=helloFile.read()
print(helloFile.readlines())
helloFile.close()

helloFile=open('Love.txt','a')
helloFile.write("\nWhat's your name?")
helloFile.close()
helloFile=open('Love.txt')
content=helloFile.read()
helloFile.close()
print(content)

newFile=open("Boss.txt",'w')
newFile.write("I am new file,who are you?")
newFile.close()
newFile=open('Boss.txt')
content=newFile.read()
newFile.close()
print(content)

'''

'''
import shelve
shelfFile=shelve.open('mydata')
cats=['Zophie','Pooka','Simon']
shelfFile['cats']=cats
#shelfFile.close()
print(type(shelfFile))
print(shelfFile['cats'])
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()

'''

'''
import pprint
cats=[{'name':'Zophie','desc':'chubby'},{'name':'Pooka','desc':'fluffy'}]
print(pprint.pformat(cats))
fileobj=open('myCats.py','w')
fileobj.write('cats = '+pprint.pformat(cats)+'\n')
fileobj.close()
fileobj=open('myCats.py','r')
content=fileobj.read()
print(content)
fileobj.close()
'''
import myCats
print(myCats.cats)



























