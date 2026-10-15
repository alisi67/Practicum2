a,b=map(int,input().split('x'))
q,w,e=map(int,input().split('x'))
if (a>=q and b>=e) or (a>=w and b>=q) or (a>=q and b>=w) or (a>=w and b>=e) or (a>=e and b>=q) or (a>=e and b>=w):
    print('да')
else:
    print('нет')