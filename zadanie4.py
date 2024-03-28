from random import choice
def login(x):
    f,i,o=x[1].split()
    lg=f'{f}_{i[0]}{o[0]}'
    return lg

def password():
    a1='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    a2='abcdefghijklmnopqrstuvwxyz'
    c='0123456789'
    p=choice(a1)+choice(a2)+choice(c)+choice(a1)+choice(a2)+choice(a1)+choice(c)+choice(a2)
    return p

a=open('students.csv', encoding='utf8').readlines()
shapka=a.pop(0)

for i in range(len(a)):
    a[i]=a[i].strip().split(',')
    a[i]+=[login(a[i]),password()]
    print(a[i], login(a[i]), password())
f=open('students_password.csv','w',encoding='utf8')
f.write(shapka)
for x in a:
    f.write(','.join(x)+'\n')
f.close()