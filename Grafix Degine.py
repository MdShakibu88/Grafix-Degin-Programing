from turtle import  * 
from colorsys import * 
bgcolor("black")
title("Shakibul Programmer")
width(2)
speed(0)
n = 100
for i in range(n): 
    c = hsv_to_rgb(i/6,i/n,1)
    fillcolor(c)
    begin_fill()
    rt(85)
    circle(i*1.2,85)
    end_fill()
    rt(59)
ht()
done()