def tamanhoSequencia(n):
    tamanho = 1
    resto1 = 1
    resto2 = 10 % n
 
    while (resto1 * resto2 % n > 0):
        resto1 = (resto1 * resto2) % n + 1
        tamanho += 1
 
    return tamanho
 
while True:
    try:
        n = int(raw_input())
    except EOFError: break
 
    print tamanhoSequencia(n)