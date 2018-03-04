from operator import attrgetter
class User:
    def __init__(self,x,y):
        self.name=x
        self.user_id=y

    def __repr__(self):
        return self.name+" : "+str(self.user_id)
users=[

    User('Kamrul',22),
    User('Tanim',21),
    User('Minar',23),
    User('Jahid',23),
    User('Kamal',30),
    User('Mimi',50)
]

for user in users:
    print(user)

print('_________________________________________________________')

for user in sorted(users,key=attrgetter('user_id')):
    print(user)