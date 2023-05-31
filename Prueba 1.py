Niñó=5500
Joven=7000
Adulto=9000
total_n=0
total_J=0
total_a=0
entradas_n=0
entradas_j=0
entradas_a=0
while True:
  print("''''Bienvenido Al Cine De MORO'''")
  print("*******Categorias*****")
  print("  Niño $5500")
  print("  Joven $7000")
  print("  Adulto $9000")
  print("============================")

  edad=int(input("Ingrese la edad: "))
  cant_entradas=int(input("Ingrese la cantidad de entradas que desea: "))
  if edad <=13:
    print(f"Categoria Niño El Valor Por Entrada ES:${Niñó}")
    total_n=cant_entradas*5500
    entradas_n=cant_entradas
    print(f"Cantidad De Entradas:{cant_entradas}")
    print(f"El total a pagar es ${total_n}")
   

  elif edad >14 and edad <21:
    print(f"Categoria Joven El Valor Por Entrada Es:${Joven}")
    total_J=cant_entradas *7000
    entradas_j=cant_entradas
    print(f"Cantidad De Entradas {cant_entradas}")
    print(f"El Total a Pagar Es ${total_J}")

    

  elif edad >=22:
    print(f"Categoria Adulto El Valor Por Entrada Es :${Adulto} ")  
    total_ad=cant_entradas*9000
    entradas_a=cant_entradas
    print(f"Cantidad De Entradas {cant_entradas}")
    print(f"El Total a Pagar Es De ${total_a}")
  print("Disfrute Su Funcion\n=================================")
  print("desea saber la cantidad de entradas vendidas en el dia")
  respuesta=int(input("[1] si , no [2]..."))
  if respuesta==1:
    print(f"Entradas De Niños {entradas_n} entradas ",total_n*100/cant_entradas, "%")  
    print(f"Entradas De Joven {entradas_j} entradas ",total_J*100/cant_entradas, "%")  
    print(f"Entradas De Adulto {entradas_a} entradas ",total_a*100/cant_entradas, "%")  
