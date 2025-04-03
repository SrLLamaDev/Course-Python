import turtle

#Abrir la ventana de
v = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
#Ajusta posición
t.up()
t.bk(300)
t.down()
t.lt(15)
#Alrededor del pentagono
t.fd(100)
t.lt(72)
t.fd(100)
t.lt(72)
t.fd(100)
t.lt(72)
t.fd(100)
t.lt(72)
t.fd(100)
t.lt(72)
#Triangulosinscritos en el pentágono
t.lt(54)
t.fd(85)
t.right(108)
t.fd(85)
t.bk(85)
t.lt(72)
t.fd(85)
t.bk(85)
t.lt(72)
t.fd(85)
t.bk(85)
t.lt(72)
t.fd(85)
t.bk(85)

#Acomodar para la figura 2
t.lt(188)
t.up()
t.fd(250)
t.down()

#Figura 2
t.lt(85)
t.fd(85)

t.bk(85)
t.lt(60)
t.fd(85)
t.bk(85)
t.lt(60)
t.fd(85)
t.bk(85)
t.lt(60)
t.fd(85)
t.bk(85)
t.lt(60)
t.fd(85)
t.bk(85)
t.lt(60)
t.fd(85)
#Contorno del hexágono
t.lt(120)
t.fd(85)
t.lt(60)
t.fd(85)
t.lt(60)
t.fd(85)
t.lt(60)
t.fd(85)
t.lt(60)
t.fd(85)
t.lt(60)
t.fd(85)
#Acomodar figura 3
t.bk(42)
t.right(90)
t.up()
t.fd(200)
t.down()
#Figura 3
t.lt(15)
t.fd(85)
t.bk(85)
a=(360//7)
t.lt(a)
t.fd(85)
t.bk(85)
t.lt(a)
t.fd(85)
t.bk(85)
t.lt(a)
t.fd(85)
t.bk(85)
t.lt(a)
t.fd(85)
t.bk(85)
t.lt(a)
t.fd(85)
t.bk(85)
t.lt(a)
t.fd(85)
#Bordes de la figura 3







#cerrar la ventana



v.exitonclick()
