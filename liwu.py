from turtle import *  # 导入模块中的全部方法
import turtle  # 导入今天我们要用的画图工具turtle模块
import turtle as t
import random as r  # 导入随机数模块


n = 100
m = 20

speed("fastest")  # 画笔速度
t.bgcolor("black")  # 背景色
left(90)
forward(3 * n)

color("red", "yellow")  # 圣诞树顶五角星的颜色外-red 内-yellow
begin_fill()  # 填充颜色
left(126)
for i in range(5):  # 画五角星
    forward(200 / 5)
    right(144)  # 五角星的内角
    forward(200 / 5)
    left(72)  # 转换角度
end_fill()
right(126)


def drawLight():
    '''定义画彩灯的方法'''
    if r.randint(0, 30) == 0:  # randint：随机生成一整数
        color('red')  # 第一种彩灯气球颜色
        circle(6)  # 彩灯大小
    elif r.randint(0, 30) == 1:
        color('orange')  # 第二种彩灯气球颜色
        circle(3)
    elif r.randint(0, 50) == 1:
        color('yellow')  # 第三种彩灯五角星颜色
        circle(1)
        for i in range(5):  # 画五角星彩灯
            forward(m / 5)
            right(144)
            forward(m / 5)
            left(72)
    else:
        color('dark green')  # 其余的随机数情况下画绿色树枝


t.pensize(10)
t.pencolor("brown")
backward(n * 5)
forward(10)


def drawSocks():
    '''画袜子'''
    penup()
    goto(-20, 80)
    pencolor("white")
    pendown()
    begin_fill()
    fillcolor("white")
    fd(25)
    circle(4, 180)
    fd(25)
    circle(4, 180)
    end_fill()
    penup()
    goto(-15, 80)
    pendown()
    begin_fill()
    fillcolor("red")
    seth(-120)
    fd(20)
    seth(150)
    fd(5)
    circle(7, 180)
    fd(15)
    circle(5, 90)
    fd(30)
    seth(160)
    fd(18)
    end_fill()
    penup()
    seth(0)
    goto(70, -240)


def tree(d, s):  # 定义画树方法
    if d <= 0:
        return
    t.pensize(4)
    forward(s)
    tree(d - 1, s * 0.8)
    right(120)
    tree(d - 3, s * 0.5)
    right(120)
    tree(d - 3, s * 0.5)
    right(120)
    backward(s)


color('dark green')  # 定义全局树枝颜色
tree(12, n)  # 调用画树方法
t.pensize(30)
backward(n / 1.1)

t.pensize(3)
# 循环画树下的小装饰
for i in range(200):
    a = 400 - 800 * r.random()
    b = 10 - 30 * r.random()
    up()
    forward(b)
    left(90)
    forward(a)
    down()
    if r.randint(0, 1) == 0:  # 随机生成整数用于随机生成小装饰
        color('red')  # 1.小圈圈
    elif r.randint(0, 1) == 0:
        color('yellow')  # 2.五角星
        for i in range(5):
            forward(m / 5)
            right(144)
            forward(m / 5)
            left(72)
    else:
        color('wheat')  # 3.小圈圈
    circle(2)

    up()
    backward(a)
    right(90)
    backward(b)

t.color("dark red")  # 定义字体颜色
t.write("Merry Christmas", align="center", font=("Comic Sans MS", 35, "bold"))  # 定义文字版式、位置、大小、颜色


def drawsnow():
    '''定义画雪花方法'''
    t.ht()  # 隐藏笔头-hideturtle缩写——ht
    t.pensize(2)
    for i in range(200):  # 雪花个数
        t.pencolor("white")  # 白色雪花
        t.pu()  # 提笔penup
        t.setx(r.randint(-340, 350))  # 定义x，y坐标，表示雪花飘落的范围
        t.sety(r.randint(-150, 350))
        t.pd()  # 落笔pendown
        dens = 6  # 雪花瓣数设为6
        snowsize = r.randint(1, 10)
        for j in range(dens):  # 画雪花
            t.fd(int(snowsize))  # 画线
            t.backward(int(snowsize))
            t.right(int(360 / dens))  # 转动角度


drawsnow()
turtle.done()

