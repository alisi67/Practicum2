a,b=input().split('-')
if a[0]=='a':
    a1=1
    a2=a[1]
elif a[0]=='b':
    a1=2
    a2=a[1]
elif a[0]=='c':
    a1=3
    a2=a[1]
elif a[0]=='d':
    a1=4
    a2=a[1]
elif a[0]=='e':
    a1=5
    a2=a[1]
elif a[0]=='f':
    a1=6
    a2=a[1]
elif a[0]=='g':
    a1=7
    a2=a[1]
elif a[0]=='h':
    a1=8
    a2=a[1]
if b[0]=='a':
    b1=1
    b2=b[1]
elif b[0]=='b':
    b1=2
    b2=b[1]
elif b[0]=='c':
    b1=3
    b2=b[1]
elif b[0]=='d':
    b1=4
    b2=b[1]
elif b[0]=='e':
    b1=5
    b2=b[1]
elif b[0]=='f':
    b1=6
    b2=b[1]
elif b[0]=='g':
    b1=7
    b2=b[1]
elif b[0]=='h':
    b1=8
    b2=b[1]
if (b1-a1)*(int(b2)-int(a2))==2:
    print('верно')
else:
    print('ошибка')