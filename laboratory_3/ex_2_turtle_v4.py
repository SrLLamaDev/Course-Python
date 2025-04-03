import turtle

def dibujar_flecha(t, x_ini, y_ini, x_fin, y_fin):
    t.pensize(3)  # Establecer grosor de la línea
    
    # Dibujar la línea de la flecha
    t.penup()
    t.goto(x_ini, y_ini)
    t.pendown()
    t.goto(x_fin, y_fin)
    
    # Dibujar la cabeza de la flecha con otro turtle
    t_head = turtle.Turtle()
    t_head.pensize(3)
    t_head.penup()
    t_head.goto(x_fin, y_fin)
    t_head.setheading(t_head.towards(x_ini, y_ini))
    t_head.left(90)
    
    # Crear el triángulo
    '''
    t_head.pendown()
    t_head.begin_fill()
    for _ in range(3):
        t_head.forward(10)
        t_head.right(120)
    t_head.end_fill()
    t_head.hideturtle()
    '''
def main():
    t = turtle.Turtle()
    t.speed(3)
    screen = turtle.Screen()
    
    # Dibujar un cuadrado con flechas
    dibujar_flecha(t, -50, -50, 50, -50)  # Abajo
    dibujar_flecha(t, 50, -50, 50, 50)  # Derecha
    dibujar_flecha(t, 50, 50, -50, 50)  # Arriba
    dibujar_flecha(t, -50, 50, -50, -50)  # Izquierda
    
    screen.mainloop()

main()

