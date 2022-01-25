import requests
from bs4 import BeautifulSoup
import turtle

res = requests.get('https://weather.yahoo.co.jp/weather/jp/47/9110.html')
res.encoding = res.apparent_encoding
soup = BeautifulSoup(res.text,'html.parser')
temp_str = soup.select('.high em')
print(temp_str[0].text)
temp = int(temp_str[0].text)
t = turtle.Turtle()
t.shape('turtle')
t.pensize(20)
t.speed(2)
t.penup()

def zero(t,x_offset):
    t.setposition(-50+x_offset, 100)
    t.right(90)
    t.pendown()
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(100)

def one(t,x_offset):
    t.setposition(50+x_offset, 100)
    t.right(90)
    t.pendown()
    t.forward(200)

def two(t,x_offset):
    t.setposition(-50+x_offset, 100)
    t.pendown()
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)

def three(t,x_offset):
    t.setposition(-50+x_offset, 100)
    t.pendown()
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.setposition(50+x_offset, 0)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(100)

def four(t,x_offset):
    t.setposition(-50+x_offset, 100)
    t.right(90)
    t.pendown()
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.penup()
    t.setposition(50+x_offset, 100)
    t.right(90)
    t.pendown()
    t.forward(200)

def five(t,x_offset):
    t.setposition(50+x_offset, 100)
    t.left(180)
    t.pendown()
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)

def six(t,x_offset):
    t.setposition(50+x_offset, 100)
    t.left(180)
    t.pendown()
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)

def seven(t,x_offset):
    t.setposition(-50+x_offset, 100)
    t.pendown()
    t.forward(100)
    t.right(90)
    t.forward(200)

def eight(t,x_offset):
    t.setposition(-50+x_offset, 100)
    t.right(90)
    t.pendown()
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.setposition(-50+x_offset, 0)
    t.left(180)
    t.forward(100)

def nine(t,x_offset):
    t.setposition(50+x_offset, 100)
    t.left(180)
    t.pendown()
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.penup()
    t.setposition(50+x_offset, 100)
    t.right(90)
    t.pendown()
    t.forward(200)


selector = {0:zero,1:one,2:two,3:three,4:four,5:five,6:six,7:seven,8:eight,9:nine}

tens_place_num = temp // 10
onec_place_num = temp % 10

t.setposition(0, 150)
t.write('今日の那覇の最高気温（℃）は',align="center",font=("Sans",25,"bold"))
t.penup()

if tens_place_num > 0:
    x_offset = -100
    selector[tens_place_num](t,x_offset)
    t.penup()
    x_offset = 100
    selector[onec_place_num](t,x_offset)
else:
    selector[onec_place_num](t,x_offset=0)

turtle.mainloop()
