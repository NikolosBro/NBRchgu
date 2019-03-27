import re
x=str(input('Введите чилсо на примере (-87.21E-5)'))
z=re.compile(r'(^[-+][0-9]+[.][0-9]+[E][-+][0-9]+$)')
z1=z.search(x)
if z1==None:
    print('False')
elif x==z1.group():
    print('true')
else:
    print('False')
    111
