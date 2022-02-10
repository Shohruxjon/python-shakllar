import turtle
t=turtle.Pen()
t.width(3)
colors=['red','blue','green']
number_of_circle=int(turtle.numinput('ajoyib aylana',
                                   'doiralar soni',6))
background=['blue']
for x in range(number_of_circle):
    t.pencolor(colors[x%3])
    t.circle(100)
    t.left(90/number_of_circle)
for x in range(1):
    t.pencolor(colors[1])
    t.circle(90)
    t.left(25)
for x in range(1):
    t.pencolor(colors[2])
    t.circle(80)
    t.left(25)
for x in range(1):
    t.pencolor(colors[3])
    t.circle(70)
    t.left(25)    
for x in range(1):
    t.pencolor(colors[0])
    t.circle(60)
    t.left(25)
for x in range(1):
    t.pencolor(colors[1])
    t.circle(50)
    t.left(25)
for x in range(1):
    t.pencolor(colors[2])
    t.circle(40)
    t.left(25)
for x in range(1):
    t.pencolor(colors[3])
    t.circle(30)
    t.left(25)
for x in range(1):
    t.circle(20)
    t.left(25)
for x in range(1):
    t.circle(10)
    t.left(25)
