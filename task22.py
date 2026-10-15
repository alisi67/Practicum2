a,b,c=map(int,input().split())
if a%b>0:
    poezdokful=a//b
    poezdokostat=0
else:
    poezdokful=a//b
    poezdokostat=a-poezdokful
time=poezdokostat*2*c + poezdokful*2*c
print(time)