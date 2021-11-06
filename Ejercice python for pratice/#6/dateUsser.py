#1
dateUsser = ["Yhonatan", "Peguero", 23]
print(dateUsser)

new_name = input("Ingrese su nombre: ")

dateUsser.insert(0 , new_name)
print(dateUsser)

#Lo que ocurre luego de esto es que se agrega el nuevo dato al indice donde estaba con anterioridad el nombre del usuario, porque con el metodo insert se especifico donde iba.
