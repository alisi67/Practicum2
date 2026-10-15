a=input()
b=a[1]
a=a[0]
if a in 'aceg' and b in '1357':
    print('чёрное')
elif a in 'bdfh' and b in '2468':
    print('чёрное')
else:
    print('белое')