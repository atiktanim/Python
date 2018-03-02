#matching rejex knowing pattern contains match objects


import re


'''
phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=phoneNumRegex.search('My contact number is 415-555-42424')
print('Phone Number found '+mo.group())
'''

#Grouping with parenthesis
'''

phoneNumRegex=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo=phoneNumRegex.search('My contact number is 415-555-42424')
print(mo.group(1))
print(mo.group(0))
print(mo.groups())#retriives all the group at once

'''
#Matching Multiple group with pipe

'''
heroRegex=re.compile(r'Batman|Tina Fey')
mo1=heroRegex.search('Batman and Tina Fey.')
print(mo1.group())#The first matching occurences will be returned

'''

#Optional matching with the question mark
'''
batRegex=re.compile(r'Bat(wo)?man')
mo1=batRegex.search('The adventure of Batman')
print(mo1.group())
mo2=batRegex.search('The adventure of Batwoman')
print(mo2.group())


phoneRegex=re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1=phoneRegex.search('My phone number is 415-555-4242')
print(mo1.group())
mo2=phoneRegex.search('My phone number is 555-4242')
print(mo2.group())
'''

#Matching zero or more with the star

'''
batRegex=re.compile(r'Bat(wo)*man')
mo1=batRegex.search('The adventure of Batman')
print(mo1.group())
mo2=batRegex.search('The adventure of Batwoman')
print(mo2.group())
mo3=batRegex.search('The adventure of Batwowoman')
print(mo3.group())

'''

#Matching specific repittions with curely Brackets

'''
haRegex=re.compile(r'(ha){3}')#will match 3 ha sequentially
mo1=haRegex.search('hahahahahaha')
print(mo1.group())
mo2=haRegex.search('ha')
print(mo2==None)
'''

#Greedy and NoneGreedy Matching

'''
GreedyhaRegex=re.compile(r'(ha){3,5}')
mo1=GreedyhaRegex.search('hahahahahaha')#will search maximum match of ha
print(mo1.group())


NonGreedyhaRegex=re.compile(r'(ha){3,5}?')
mo2=NonGreedyhaRegex.search('hahahahahaha')#will search minimum match of ha
print(mo2.group())

'''

#Findall Method

'''
phoneregex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=phoneregex.findall('My phone num is 015-212-33718.Or 018-577-59319')
print(mo)

'''
#Charachter class

'''
xmasRegex=re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers,11 pipers,10 lords,9 ladies,8 maids'))

'''
#Making your own charachter classes

'''
vowelRegex=re.compile(r'[aeiouAEIOU]')#Matches what you put on curely Bracket
print(vowelRegex.findall("She is very sexy,whatever i don't like her"))

consonentRegex=re.compile(r'[^aeiouAEIOU]')#Matches all except vowel.Caret("^") is doing it
print(consonentRegex.findall("She is very sexy,whatever i don't like her"))
'''

#There are caret and dollar charachter in automate the booring stuff

#The Wildcart chararchter

'''
atRegex=re.compile(r'.at')
print(atRegex.findall('The cat in the h.at sat on the flat mat'))
'''

#Matching everything with dot star

'''
nameRegex=re.compile(r'First Name: (.*) Last Name : (.*)')
mo=nameRegex.search('First Name: Md. Atikur Rahman Last Name : Tanim')
print(mo.group(1))

nongreedyRegex=re.compile(r'<.*?>')#Matches in greedy approach
mo=nongreedyRegex.search('<To serve man> for dinner>')
print(mo.group())

greedyRegex=re.compile(r'<.*>')#Matches in non greedy approach
mo=greedyRegex.search('<To serve man> for dinner>')
print(mo.group())

'''

#Matching new lines withg dot character
'''
noNewLineRegex=re.compile('.*')#Matches to new Line
mo=noNewLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law')
print(mo.group())

NewLineRegex=re.compile('.*',re.DOTALL)
mo=NewLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law')
print(mo.group())
'''

#Case Insensitive Matching

robocop=re.compile(r'robocop',re.I)
mo=robocop.search('Robocope is a part of machinee')
print(mo.group())






























