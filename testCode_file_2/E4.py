#Ejercicio 4
import turtle
v = turtle.Screen()
#Figura Triangulo equilatero
#---------------------------
#Acomodar imagen
a = turtle.Turtle()
a.pensize(1)
a.color("black")
a.shape("turtle")
#Acomodar
a.up()
a.bk(200)
a.right(90)
a.fd(50)
a.lt(90)
a.down()
#Triangulo equilatero
a.fillcolor("skyblue")
a.begin_fill()
a.bk(50)
a.lt(60)
a.fd(50)
a.bk(50)
a.right(60)
a.fd(50)
a.lt(120)
a.fd(50)
a.lt(120)#No se porque
a.fd(50)#No se por que :v
a.end_fill()
#-----------------------
#Figura cuadrado
t = turtle.Turtle()
t.color("black")
t.shape("turtle")
t.pensize(1)
#Acomodar
t.up()
t.bk(100)
t.down()
#Haer cuadrado
t.fillcolor("red")
t.begin_fill()
t.fd(30)
t.right(90)
t.fd(60)
t.right(90)
t.fd(60)
t.right(90)
t.fd(60)
t.right(90)
t.fd(30)
t.end_fill()
#--------------------
#Figura rectangulo
r = turtle.Turtle()
r.color("black")
r.shape("turtle")
r.pensize(1)
#Acomodar
r.up()
r.down()
#Haer cuadrado
r.fillcolor("yellow")
r.begin_fill()
r.fd(120)
r.right(90)
r.fd(60)
r.right(90)
r.fd(120)
r.right(90)
r.fd(60)
r.right(90)
r.fd(120)
r.end_fill()
#--------------------
#Figura cirulo
g = turtle.Turtle()
g.shape("turtle")
#Acomodar
g.up()
g.fd(250)
g.right(90)
g.fd(30)
g.lt(90)
g.down()
#Circulo
g.color("black")
g.fillcolor("green")
g.shape("circle")
g.shapesize(3,3,1) #(Ancho,Alto,Grosor)
#---------------------
#Figura rombo
s = turtle.Turtle()
s.color("black")
s.shape("turtle")
s.pensize(1)
#Acomodar
s.up()
s.bk(240)
s.right(90)
s.fd(150)
s.lt(90)
s.down()
#Rombo
s.fillcolor("yellow")
s.begin_fill()
s.lt(45)
s.fd(30)
s.right(90)
s.fd(60)
s.right(90)
s.fd(60)
s.right(90)
s.fd(60)
s.right(90)
s.fd(30)
s.end_fill()
#---------------------------
#Figura que parece cuadrado :v
t = turtle.Turtle()
t.color("black")
t.shape("turtle")
t.pensize(1)
#Acomodar
t.up()
t.bk(130)
t.right(90)
t.fd(180)
t.lt(90)
t.down()
#No se
t.fillcolor("skyblue")
t.begin_fill()
t.fd(60)
t.lt(45)
t.fd(60)
t.lt(135)
t.fd(60)
t.lt(45)
t.fd(60)
t.end_fill()
#---------------------------------------
#Otra figura que no es cuadrado
x = turtle.Turtle()
x.color("black")
x.shape("turtle")
x.pensize(1)
#Acomodar
x.up()
x.fd(40)
x.right(90)
x.fd(180)
x.lt(90)
x.down()
#No se
x.fillcolor("green")
x.begin_fill()
x.fd(60)
x.lt(60)
x.fd(60)
x.bk(60)
x.right(60)
x.bk(60)
x.lt(120)
x.fd(60)
x.right(120)
x.fd(120)
x.right(120)
x.fd(60)
x.end_fill()
#----------------------------------
#Figura elipse
z = turtle.Turtle()
z.shape("turtle")
#Acomodar
z.up()
z.fd(250)
z.right(90)
z.fd(170)
z.lt(90)
z.down()
#Elipse
z.color("black")
z.fillcolor("red")
z.shape("circle")
z.shapesize(3,6,1) #(Alto,Ancho,Grosor)
#---------------------------------




