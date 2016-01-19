#! python3
# strongPW.py - tells you if your password is strong

import re

while True:
    print('Please type your password. Blank entry to quit')
    pw=str(input())
    if pw == '':
        break
    lntest = re.compile(r'\w{8,}')
    lntest2 = lntest.search(pw)
    if lntest2 == None:
        print("Your Password is too short")
        continue
    lowtest = re.compile(r'[a-z]')
    lowtest2 = lowtest.search(pw)
    if lowtest2 == None:
        print("Your Password doesnt contain a lowercase letter")
        continue
    hitest = re.compile(r'[A-Z]')
    hitest2 = hitest.search(pw)
    if hitest2 == None:
        print("Your Password doesnt contain an uppercase letter")
        continue
    numtest = re.compile(r'[0-9]')
    numtest2 = numtest.search(pw)
    if numtest2 == None:
        print("Your Password doesnt contain a number")
        continue
    print('The password ' + lntest2.group() + ' is strong' )
    
