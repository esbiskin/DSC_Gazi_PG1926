import turtle

ybs=turtle.Turtle()

def kare():
    for i in range(4):
        ybs.fd(100)
        ybs.left(90)

for i in range(36):
    kare()
    ybs.left(10)
