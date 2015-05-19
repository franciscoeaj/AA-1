while True:
    n = int(raw_input())
    if n == 0: break
  
    alunos, forcas = [], []
    for i in xrange(n):
        alunos.append(raw_input())
        forca = 0
        for letra in alunos[i]:
            forca += ord(letra)
        forcas.append(forca)
     
    somas1, somas2, soma1, soma2 = [], [], 0, 0
    for i in range(len(forcas)):
        soma1 += forcas[i]
        somas1.append(soma1)
    for i in range(-1, -len(forcas), -1):
        soma2 += forcas[i]
        somas2.append(abs(soma2))

    somas2.append(0)
    soma1 = 0
    soma2 = sum(somas2)
    aux = len(somas2) - 1
    for j in xrange(len(somas1)):
        soma1 += somas1[j]
        soma2 -= somas2[aux]
        if soma1 == soma2:
            print alunos[j]
            break
        aux -= 1
 
    if soma1 != soma2:
        print 'Impossibilidade de empate.'
