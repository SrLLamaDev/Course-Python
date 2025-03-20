import random
from sympy import isprime, mod_inverse

# 1. Elegimos dos números primos pequeños
p = 61
q = 53
n = p * q
phi_n = (p - 1) * (q - 1)

# 2. Elegimos un número e coprimo con phi_n
e = 17  # Valor comúnmente usado en RSA

# 3. Calculamos d como el inverso modular de e módulo phi_n
d = mod_inverse(e, phi_n)

# 4. Definimos el mensaje a cifrar (convertido a número)
M = 42  # Mensaje original
C = pow(M, e, n)  # Cifrado: C = M^e mod n

# 5. Descifrar el mensaje
M_descifrado = pow(C, d, n)  # Descifrado: M = C^d mod n

# 6. Mostrar resultados
print(f"Clave pública: (e={e}, n={n})")
print(f"Clave privada: (d={d}, n={n})")
print(f"Mensaje original: {M}")
print(f"Mensaje cifrado: {C}")
print(f"Mensaje descifrado: {M_descifrado}")
