a,b=map(int,input().split('x'))
s=int(input())
if (s%a==0 or s%b==0) and s<=(a+b):
    print('успешно')
else:
    print('неосуществимо')
