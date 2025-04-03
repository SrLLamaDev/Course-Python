def in_a_post(expresion):
    resultado = []
    pila = []
    precedencia = {'+':1, '-':1, '*':2, '/':2, '^':3} #definir presedencia de
    pilaAux = []                          #operadaores
    for caracter in expresion:
        print (caracter)
        if caracter.isalnum():
            resultado.append(caracter)
        elif caracter == '(':
            pila.append(caracter)
        elif caracter == ')':
            while pila and pila[-1] != '(':
                resultado.append(pila.pop())
            pila.pop()
        else:
            while pila and precedencia.get(pila[-1],0) >= precedencia.get(caracter, 0):
                resultado.append(pila.pop())
            pila.append(caracter)
    print ("---------------")
    while pila:
        print (caracter)
        resultado.append(pila.pop())
    
    return ''.join(resultado)

exp_in = "2 * 3 + 4"

exp_post = in_a_post(exp_in)
print(exp_post)
'''lectura'''
##var = input()
##exp_post = in_a_post(var)
##print(exp_post)

