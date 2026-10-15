xc=int(input('xc = '))
yc=int(input('yc = '))
r=int(input('r = '))
x=int(input('x = '))
y=int(input('y = '))
from turtle import *
reset()
up()
goto(0,0)
goto(xc,yc-r)
down()
circle(r)
up()
goto(0,0)
goto(x,y)
dot(3)
ty=(x-xc)**2 + (y-yc)**2
if ty< r**2:
    write('точка в окружности')
elif ty==r**2:
    write ('точка лежит на окружности')
else:
    write('точка вне окружности')
done()