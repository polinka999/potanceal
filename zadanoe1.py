f=open('students.csv',encoding='utf8')
a= f.readlines()
f.close()
shaka= a.pop(0)
for i in range(len(a)):
    a[i]=a[i].strip().split(',')
    if a[i][-1]=='None':
        print(a[i])
for i in range(len(a)):
    if 'Хадаров Владимир' in a[i][1]:
        print(f'Ты получил: {a[i][-1]}, за проект: {a[i][2]}')

d={}
for x in a:
    clas=x[3]
    score=x[-1]
    if score!='None':
        if clas not in d:
            d[clas]=[int(score)]
        else:
            d[clas]+=[int(score)]
print(d)
for clas in d:
    d[clas]=round(sum(d[clas])/len(d[clas]),3)
for i in range(len(a)):
    if a[i][-1] == 'None':
        a[i][-1] = str(d[a[i][3]])
f=open('student_new.csv','w', encoding='utf8')
f.write(shaka)
for x in a:
    f.write(','.join(x)+'\n')
f.close()