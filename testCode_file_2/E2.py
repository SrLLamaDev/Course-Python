#Ejercicio número 2
import turtle
v = turtle.Screen()
v.bgcolor("#3D5BA2")

t = turtle.Turtle()
t.color("yellow")
t.shape("turtle")
t.pensize(3)
#Acomodar para hacer el marco
t.up()
t.bk(200)
t.lt(90)
t.down()
#Hacer cuadrado desde el medio
t.fillcolor("green")
t.begin_fill()
t.fd(200)
t.right(90)
t.fd(400)
t.right(90)
t.fd(400)
t.right(90)
t.fd(400)
t.right(90)
t.fd(200)
t.end_fill()
#Parámetros para las letras
ti = turtle.Turtle()
ti.color("red")
ti.shape("turtle")
ti.pensize(4)
#Hacer la "Y"
#Acomodar

ti.up()
ti.bk(100)
ti.down()
#Letra
ti.lt(90)
ti.bk(100)
ti.fd(130)
ti.lt(45)
ti.fd(70)
ti.bk(70)
ti.right(90)
ti.fd(70)
#Hacer la letra "N"
#Acomodar
ti.right(45)
ti.up()
ti.fd(50)
ti.down()
ti.right(90)
#Letra
ti.fd(180)
ti.bk(180)
ti.lt(30)
ti.fd(200)
ti.lt(150)
ti.fd(180)




