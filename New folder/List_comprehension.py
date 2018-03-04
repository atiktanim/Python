'''

my_list=[i**2 for i in range(20) if i%2==0]
print(my_list)
a_list=['Matin','Khan','a','b','c']
my_set={i for i in a_list if len(i)>1}
print(my_set)
new_list=['Name','Country','Career']
new_list1=['Tanim','Bangladesh','Teletalk']
my_dic={i:j for i,j in zip(new_list,new_list1)}
print(my_dic)

'''


'''
a=[i for i in range(11)]
print(a)
b=[i for i in range(11,25)]
c=zip(a,b)
print(c)
print(list(c))
'''

'''
my_dic={'Career':'Teletalk','Country':'Bangladesh','Name':'Tanim'}
print(my_dic)
new_dic={key:value for value,key in my_dic.items()}
print(new_dic)
'''

def add(a,b,c):
    return a+b+c
c=add(1,2,3)
print(c)
