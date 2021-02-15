estudo = int(input("Por favor insira seus anos de estudo: "))

if estudo <= 1:
  print("Iniciante")
elif estudo <= 3:
  print("Intermediário")
elif estudo <= 6:
  print("Avançado")
elif estudo >= 7: 
  print("Jedi Master")