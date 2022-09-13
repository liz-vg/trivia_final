RED = '\033[31m'
YELLOW = '\033[33m'
RESET = '\033[39m'
import random, time

puntos = random.randint (0,10)

iniciar_trivia = True  # Iniciamos la variable en True
intentos = 0

print(RED+"Bienvenido a mi trivia"+RESET)
time.sleep(1)
nombre = input(YELLOW+"¿Cúal es tu nombre?: "+RESET)

# Es importante dar instrucciones sobre cómo jugar:
print("\nHola", nombre, "mucho gusto")

time.sleep(1)

print("Estas son las reglas:")

time.sleep(1)

print("-Responder las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")

time.sleep(1)
      
print('-responder solo con "a", "b", "c", "d"')

time.sleep(1)

print("iniciaras con", puntos, "puntos")

time.sleep(2)

print("mucha suerte!!!")

while iniciar_trivia == True: #  Mientras iniciar_trivia sea True, repite:
  intentos += 1
  puntos = 0

  print("\nIntento número:", intentos)
  input("Presiona Enter para continuar")
  
  # Pregunta 1
  print(YELLOW+"\n1) ¿Cuándo fue la independencia del perú?"+RESET)
  print("a) 27 de Agosto de 1821")
  print("b) 28 de Julio de 1821")
  print("c) 8 de Julio de 1821")
  print("d) 29 d Julio de 1821")

# Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_1 = input(YELLOW+"\nTu respuesta: "+RESET)

  time.sleep(1)

  while respuesta_1 not in ("a", "b", "c", "d"): 
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

# verificamos su respuesta para mandar un mensaje de acierto o de error
  if respuesta_1 == "a":
    print(YELLOW+"Incorrecto!"+RESET, nombre, "no es el 27 de agosto de 1821")
  elif respuesta_1 == "c":
    print(YELLOW+"Incorrecto!"+RESET, nombre, "no es el 8 de julio de 1821")
  elif respuesta_1 == "d":
    print(YELLOW+"Incorrecto"+RESET, nombre, "no es 29 de julio de 1821")
  else:
    puntos = puntos + 10
    print(YELLOW+"felicidades", nombre, "respuesta correcta"+RESET)

# Pregunta 2
  print(YELLOW+"\n2) ¿Cuál de estos no es un util escolar?"+RESET)
  print("a) Tijeras")
  print("b) Borrador")
  print("c) Peras")
  print("d) Plumones")

  respuesta_2 = input(YELLOW+"\nTu respuesta: "+RESET)

  time.sleep(1)

  while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

#verificamos su respuesta para mandar un mensaje de acierto o de error
  if respuesta_2 == "c":
    puntos = puntos +10
    print(YELLOW+"felicidades", nombre, "respuesta correcta"+RESET)
 
  else:
    print(YELLOW+"respuesta incorrecta"+RESET)
  
#pregunta 3
  print(YELLOW+"\n3) ¿Cuál de estas es una maravilla del mundo?"+RESET)
  print("a) Cataratas de Niagara")
  print("b) Templo Tiahuanaco")
  print("c) Lago Titicaca")
  print("d) Chichen Itza")

# Almacenamos la respuesta del usuario en la variable "respuesta_3"
  respuesta_3 = input(YELLOW+"\nTu respuesta: "+RESET)

  while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

  time.sleep(1)

  if respuesta_3 == "a":
    print (YELLOW+"Totalmente incorrecto! ..."+RESET)
    puntos = puntos / 2
  elif respuesta_3 == "b":
    print (YELLOW+"..."+RESET)
    puntos = puntos + 5
  elif respuesta_3 == "c":
    print (YELLOW+"Incorrecto! ..."+RESET)
    puntos = puntos - 5
  else:
    print (YELLOW+"Correcto! ..."+RESET)
    puntos = puntos * 2

  time.sleep(2)

  print (RED+"\nGracias", nombre, "por jugar mi trivia, alcanzaste", puntos, "puntos"+RESET)

  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

  if repetir_trivia != "si":  # != significa "distinto"
    print("\nEspero", nombre, "que lo hayas pasado bien, hasta pronto!")
    iniciar_trivia = False 