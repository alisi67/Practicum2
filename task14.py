q=int(input())
if q%29==0:
    w=q//29
    if w<17:
        print(w,'кнатов')
    elif w>=17:
        if w%17==0:
            print(w//17,'галлеонов')
        else:
            g=w//17
            w=w-g*17
            print(g,'галлеонов')
            print(w,'сиклей')
elif q%29>0:
    w=int(q/29)
    q=q-w*29
    if w<17:
        print(w,'сиклей')
        print(q, 'кнатов')
    elif w>=17:
        if w%17==0:
            print(w//17,'галлеонов')
            print(q, 'кнатов')
        else:
            g=w//17
            w=w-g*17
            print(g,'галлеонов')
            print(w,'сиклей')
            print(q, 'кнатов')
elif q%29<0:
    print(q, 'кнатов')



