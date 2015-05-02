while True:
    a, b = map(long,raw_input().split())

    if a == 0 and b == 0: break

    lista = [1, 2]
    i = 3

    cont = 0
    while True:
        valor = lista[-1] + lista[-2]
        if valor > b: break

        lista.append(valor)

    for i in lista:

        if a <= i <= b:
            cont +=1
            
    print cont