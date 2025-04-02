while True:
    numero = int(input("informe um numero: "))

    if numero == 10:
        break

  
    if numero % 2 == 0:
        continue           #se inverter os ifs nao vai funcionar pq o 10 é um numero par


    print(numero)