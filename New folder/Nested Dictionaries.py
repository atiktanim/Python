Guests={'Tanim':{'apples':5,'Banana':12},
        'Bob':{'Lichi':10,'Orange':100},
        'Jacob':{'Guazava':1000,'apples':20}


        }
def totalBrought(guests,item):
    numBrought=0
    for k,v in Guests.items():
        numBrought=numBrought+v.get(item,0)
    return numBrought
print('apples'+str(totalBrought(Guests,'apples')))

for v in Guests.keys():
        print(v)

