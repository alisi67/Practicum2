a=(input())
if len(a)==4:
    a=int(a)
    e=a%10
    d=a//10%10
    s=a//100%10
    t=a//1000
    if e!=d and e!=s and e!=t and d!=s and d!=t and t!=s:
        if a<1900 or a>2050:
            print('OK')
        else:
            print('ERROR')
    else:
        print('ERROR')
else:
    print('ERROR')