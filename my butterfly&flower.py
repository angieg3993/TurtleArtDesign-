import turtle
x=turtle.Turtle()
turtle.colormode(255)
x.left(90)
x.speed(111)
turtle.bgcolor(0,0,0)
#the first middle swirl
x.pencolor("pink")
for times in range(10):
    
    x.width(9)
    x.forward(20)
    x.left(times+3)
    
x.left(30)
x.forward(7)
x.begin_fill()
x.circle(5)
x.end_fill()

x.penup()
x.goto(0,-5)
x.pendown()

for times in range(5):
    x.forward(10)
    x.right(25)
     


for times in range(9):
    x.forward(20)
    x.right(times+1)

x.left(90) 
x.circle(5)

x.penup()
x.goto(-15,30)
x.pendown()
#PERFECT LEAVE IT

for times in range(15):
    x.forward(times)
    x.left(times-3)
x.right(20)
for times in range(20):
    x.forward(9)
    x.left(1)
x.left(90)
for times in range(20):
    x.forward(5)
    x.left(3)

for times in range(20):
    x.forward(times-3)
    x.left(times-7)

x.left(180)
x.forward(20)
for times in range(25):
    x.forward(times)
    x.left(times)

for times in range(20):
    x.forward(times)
    x.left(times-5)

for times in range(10):
    x.forward(times)
    x.left(times*4)
x.begin_fill()
x.circle(5)
x.end_fill()

#LEFT SIDE DONE

x.penup()
x.goto(-15,30)
x.pendown()

#STARTING THE RIGHT

for times in range(13):
    x.forward(times+2)
    x.right(times-3)
x.left(30)
for times in range(17):
    x.forward(9)
    x.right(1)
x.right(90)
for times in range(20):
    x.forward(5)
    x.right(3)

for times in range(20):
    x.forward(times-3)
    x.right(times-7)
x.forward(50)
x.right(180)
x.forward(20)
for times in range(25):
    x.forward(times)
    x.right(times)

for times in range(23):
    x.forward(times)
    x.right(times-5)

for times in range(10):
    x.forward(times)
    x.right(times*4)

x.begin_fill()
x.circle(5)
x.end_fill()

#RIGHT SIDES DONEEEE
x.penup()
x.goto(-33,15)
x.pendown()
x.right(195)
for times in range(4):
    x.forward(times+30)
    x.left(5)
    
x.left(130)
for times in range(4):
    x.forward(times+30)
    x.left(14)


''''c=turtle.Turtle()
c.speed(11)
c.penup()
c.goto(-65,245)
c.pendown()
for times in range(8):
    c.color(100,0,100)
    c.circle(100)
    c.right(45)
#DONEEEEEE
    
x.penup()
x.goto(-15,290)
x.pendown()

x.begin_fill()
x.pencolor("blue")
x.circle(5)
x.end_fill()'''



#FLOWERRR

x.penup()
x.goto(100,-400)
x.pendown()
x.begin_fill()
x.color("yellow")
x.circle(150)
x.end_fill()

x.penup()
x.goto(-120,-322)
x.pendown()
x.pencolor("black")
x.speed(111111)

x.pencolor("magenta")
for times in range(203):
    x.forward(1)
    x.right(1)

x.left(155)
for times in range(203):
    x.forward(1)
    x.right(1)
x.left(155)
for times in range(203):
    x.forward(1)
    x.right(1)
x.left(155)
for times in range(203):
    x.forward(1)
    x.right(1)
x.left(155)
for times in range(203):
    x.forward(1)
    x.right(1)
x.left(155)
for times in range(203):
    x.forward(1)
    x.right(1)
x.left(155)
for times in range(203):
    x.forward(1)
    x.right(1)
x.left(155)
for times in range(203):
    x.forward(1)
    x.right(1)
x.left(155)
for times in range(203):
    x.forward(1)
    x.right(1)
x.left(155)
for times in range(203):
    x.forward(1)
    x.right(1)
x.left(155)
for times in range(203):
    x.forward(1)
    x.right(1)
x.left(155)
for times in range(203):
    x.forward(1)
    x.right(1)
x.left(155)
for times in range(203):
    x.forward(1)
    x.right(1)
x.left(155)
for times in range(203):
    x.forward(1)
    x.right(1)
x.left(155)
for times in range(203):
    x.forward(1)
    x.right(1)
x.left(155)
for times in range(203):
    x.forward(1)
    x.right(1)
x.left(155)
for times in range(203):
    x.forward(1)
    x.right(1)
x.left(155)
for times in range(203):
    x.forward(1)
    x.right(1)
x.left(155)
for times in range(203):
    x.forward(1)
    x.right(1)
#FLOWER DONEEEEE

x.penup()
x.goto(-100,250)
x.pendown()
for times in range(20):
    x.width(2)
    x.color("purple")
    x.right(30)
    x.circle(30)
    

x.penup()
x.goto(167,287)
x.pendown()

for times in range(20):
    x.width(2)
    x.color("pink")
    x.right(30)
    x.circle(30)



x.penup()
x.goto(-300,-324)
x.pendown()

for times in range(20):
    x.width(2)
    x.color("blue")
    x.right(30)
    x.circle(30)


x.penup()
x.goto(350,-125)
x.pendown()

for times in range(20):
    x.width(2)
    x.color("white")
    x.right(30)
    x.circle(30)


x.penup()
x.goto(167,287)
x.pendown()

for times in range(20):
    x.width(2)
    x.color("yellow")
    x.right(30)
    x.circle(30)



x.penup()
x.goto(-290,20)
x.pendown()

for times in range(20):
    x.width(2)
    x.color("cyan")
    x.right(30)
    x.circle(30)


x.penup()
x.goto(200,-200)
x.pendown()

for times in range(20):
    x.width(2)
    x.color("light green")
    x.right(30)
    x.circle(30)


x.penup()
x.goto(-390,380)
x.pendown()

for times in range(20):
    x.width(2)
    x.color("red")
    x.right(30)
    x.circle(30)







