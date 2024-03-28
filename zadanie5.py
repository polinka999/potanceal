a=open('students.csv', encoding='utf8').readlines()
shapka=a.pop(0)

def hash(s):
    p=67
    m=10**9+9
    h=0
    for i in range(len(s)):
        h+=A.index(s[i])*p**i
    h=h%m
    return h
A='*АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя '
for i in range(len(a)):
    a[i]=a[i].strip().split(',')
    a[i][0]=str(hash(a[i][1]))
    print(a[i])
f=open('students_with_hash.csv','w',encoding='utf8')
f.write(shapka)
for x in a:
    f.write(','.join(x)+'\n')
f.close()