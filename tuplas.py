import math

puntos = [(2, 9), (9, 9), (0, 2), (3, 3)]

ordenados= sorted(puntos, key=lambda punto: math.sqrt(punto[0]**2 + punto[1]**2))

print(ordenados)  

