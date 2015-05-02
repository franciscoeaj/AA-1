while True:
    lista = [1, 2]

    a = int(raw_input())

    if a == 0: break

    if a == 1:
        print lista[0]
        continue
    elif a == 2:
        print lista[1]
        continue
    for i in range(2, a):
        lista.append(lista[i - 1] + lista[i - 2])
        
    print lista[-1]