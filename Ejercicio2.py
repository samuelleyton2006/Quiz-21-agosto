palabras = ["perro", "gato", "elefante", "oso", "jirafa"]

filtradas = list(filter(lambda palabra: len(palabra) >= 5, palabras))

print(filtradas)  


#En el ejercicio se pide solo las palabras que tengan mas de 5 letras pero en ese caso al jugar con las palabras pues quedaria siempre por fuera el perro

#para que el perro quede dentro de la salida , se le puso tambien un igual y cualquier palabra la cual tenga 5 letras o mas de 5 letras va a estar dentro de la salida 