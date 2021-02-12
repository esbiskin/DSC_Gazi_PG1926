import turtle

ybs=turtle.Turtle()

def kare(buyukluk):
    for i in range(4):
        ybs.fd(buyukluk)
        ybs.left(90)

for i in range (50):
    kare(i*5)
