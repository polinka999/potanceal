f=open('students.csv',encoding='utf8')
a= f.readlines()
f.close()
shaka= a.pop(0)
for i in range(len(a)):
    a[i]=a[i].strip().split(',')
    if a[i][-1]=='None':
        a[i][-1]==0
    else:
        a[i][-1]==int(a[i][-1])

for n in range(1,len(a)):
    v=a[n][-1]
    i=a[n]
    j=n-1
    while a[j][-1]<v and j>0:
        a[j+1]=a[j]
        j-=1
    a[j+1]=i
k=0
print('10 class:')
for x in a:
    clas = x[3]
    if '10' in clas:
        k+=1
        f,i,o=x[1].split()
        name=f'{i[0]}.{f}'
        print(f'{k} место: {name}')
    if k==3:
        break