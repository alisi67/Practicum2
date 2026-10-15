a=int(input())
if 0<a<11:
    print(a-1)
elif 10<a<100:
    if (a-11)%2==0:
        nomer=(a-11)//2
        number=(nomer+10)//10
        print(number)
    elif (a-11)%2>0:
        nomer=(a-11)//2
        number=(nomer+10)%10
        print(number)
elif 99<a<191:
    if (a-11)%2==0:
        nomer=(a-11)//2
        number=(nomer+10)//100
        print(number)
    elif (a-11)%2>0:
        nomer=(a-11)//2
        number=(nomer+10)%10
        print(number)
elif 190<a<201:
    if (a-191)%3==0:
        nomer=(a-191)//3
        number=(nomer+100)//100
        print(number)
    elif (a-191)%3==2:
        nomer=(a-191)//3
        number=(nomer+100)//10%10
        print(number)
    elif (a-191)%3==3:
        nomer=(a-191)//3
        number=(nomer+100)%10
        print(number)
