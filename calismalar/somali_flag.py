import turtle
ybs=turtle.Turtle()
ybs.speed(100)

#somali bayrağı
ybs.begin_fill()
ybs.color("#4189DD")
ybs.fd(180)
ybs.left(90)
ybs.fd(120)
ybs.left(90)
ybs.fd(180)
ybs.left(90)
ybs.fd(120)
ybs.end_fill()
ybs.pu()
ybs.right(180)
ybs.fd(68)
ybs.right(90)
ybs.fd(114)
ybs.left(180)
ybs.pd()
ybs.begin_fill()
ybs.color("#FFFFFF")
for i in range(5):
    ybs.fd(48)
    ybs.left(144)
ybs.end_fill()
ybs.hideturtle()
