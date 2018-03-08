PASSWORDS={'email':'atiuhwyvbfwyd',
            'blog':'whhfgfwiuy',
           'luggage':'12345'
           }
import sys,pyperclip

if len(sys.argv)<2:
    print('Usage : py pw.py [account] - copy account password')
    sys.exit()

accountsys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for '+ account +' copied to clipboard')
else:
    print('There are no account named '+ account)
