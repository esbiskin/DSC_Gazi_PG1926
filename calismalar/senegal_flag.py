import turtle
ybs=turtle.Turtle()
ybs.speed(100)

#senegal bayrağı
ybs.begin_fill()
ybs.color("#00853F")
for i in range(2):
  ybs.fd(60)
  ybs.right(90)
  ybs.fd(120)
  ybs.right(90)
ybs.end_fill()
ybs.fd(60)
ybs.begin_fill()
ybs.color("#FDEF42")
for i in range(2):
  ybs.fd(60)
  ybs.right(90)
  ybs.fd(120)
  ybs.right(90)
ybs.end_fill()
ybs.fd(60)
ybs.begin_fill()
ybs.color("#E31B23")
for i in range(2):
  ybs.fd(60)
  ybs.right(90)
  ybs.fd(120)
  ybs.right(90)
ybs.end_fill()
ybs.pu()
ybs.left(180)
ybs.fd(30)
ybs.left(90)
ybs.fd(41)
ybs.right(16)
ybs.pd()
ybs.begin_fill()
ybs.color("#00853F")
for i in range(5):
    ybs.fd(38)
    ybs.left(144)
ybs.end_fill()
ybs.hideturtle()
