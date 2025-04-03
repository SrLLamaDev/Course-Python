'''
salario base de X por mes.
Por cada Y años de antiguedad del docente, se le otorga un aumento del 5 %, y por cada Z
horas que dedica a tutorıas y cursos extras, se le suman 20 Bs adicionales. Calcula el salario
mensual y de un ano del Docente.
'''
#x=float(input('Ingrese el salario base del docente: ')) # Salario base
#y=float(input('Ingrese la cantidad de años de antiguedad del docente: ')) # Años de antiguedad  
#w=float(input('Ingrese la cantidad de horas de tutorias y cursos extras: ')) # Horas de tutorias y cursos extras
#Entrada
x, y, w = map(float, input().split())
# Proceso
# Salario mensual 
s= x + (x * 0.05 * y) + (20 * w) # Salario mensual
# Salario anual
s_a= s * 12 # Salario anual
# Salida de datos
print(f'Salario mensual: {s} Bs') # Salida del salario mensual

