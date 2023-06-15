import turtle as t 

def rectangle(horizontal,vertical,color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range(1,3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()

t.penup()
t.speed('slow')
t.bgcolor('peach puff')

#feet
t.goto(-100, -150)
rectangle(50,20,'red')
t.goto(-30,-150)
rectangle(50,20,'blue')

#legs
t.goto(-25, -50)
rectangle(15,100,'black')
t.goto(-55,-50)
rectangle(-15,100,'grey')

#body
t.goto(-90,100)
rectangle(100,150,'goldenrod')

#arms
t.goto(-150, 70)
rectangle(60,15,'hotpink')
t.goto(-150,110)
rectangle(15,40,'grey')

t.goto(10, 70)
rectangle(60,15,'thistle')
t.goto(55,110)
rectangle(15,40,'black')

#neck
t.goto(-50,120)
rectangle(15,20,'grey')

#head
t.goto(-85,170)
rectangle(80,50,'red')

#eyes
t.goto(-60, 160)
rectangle(30,10,'navy')
t.goto(-55,155)
rectangle(5,5,'black')
t.goto(-40,155)
rectangle(5,5,'lawngreen')

#mouth
t.goto(-65,135)
t.right(5)
rectangle(40,5,'black')

t.hideturtle()
