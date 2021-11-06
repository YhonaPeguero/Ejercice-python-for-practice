#a. Dividir un numero entero entre cero
try:
  dividir = 1 / 0
except ZeroDivisionError :
  print("Op: dividir = 1 / 0, typeError: ZeroDivisionError division by zero.")

#b. Concatenar "Hello" a una variable llamada MENSAJE que no esta definida
try:
  concatenar = "Hello" 
  variable = MENSAJE
  concatenacion = concatenar + variable
except NameError :
  print("NameError: name 'MENSAJE' is not defined")


#b. Concatenar "Hello" a una variable llamada MENSAJE que no esta definida
try:
  number= 20
  text = "string text"
  result = number + text 
except TypeError :
  print(" result = number + text, TypeError: unsupported operand type(s) for +: 'int' and 'str'")

#c. Concatenar un numero entero a una cadena de texto.
try:
  number= 20
  text = "string text"
  result = number + text 
except TypeError :
  print(" result = number + text, TypeError: unsupported operand type(s) for +: 'int' and 'str''")


#d. Dividir una cadena de texto entre un numero entero.
try :
  div2 = 20
  div3 = "texto"
  resultDiv = div2 / div3
except TypeError :
  print(" Division entre texto y entero, TypeError: unsupported operand type(s) for /: 'int' and 'str' ")