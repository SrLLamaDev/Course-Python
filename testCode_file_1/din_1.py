##primera funcion para fibonacci
def fibo_1(n):
    if n <= 1:
        return n
    else:
        return fibo_1(n-1) + fibo_1(n-2)
##imprimir de manera vertical
def fibo_v(n):
    for i in range(n):
        print(fibo_1(i))
def fibo_h(n):
    for i in range(n):
        print(fibo_1(i), end=" ")

##-------llamadas-----
print(fibo_1(5))
fibo_v(5)
fibo_h(5)
