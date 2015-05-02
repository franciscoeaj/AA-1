dimensoes = map(int, raw_input().split())
 
while (dimensoes[0] > 0 and dimensoes[1] > 0):
    altura = dimensoes[0]
    comprimento = dimensoes[1]
    alturas = map(int, raw_input().split())
 
    ativacoes = 0
    for i in range(comprimento):
        if (i == 0):
            ativacoes += altura - alturas[i]
        else:
            if (i > 0) and (alturas[i] < alturas[i - 1]):
                ativacoes += alturas[i - 1] - alturas[i]
 
    print ativacoes
 
    dimensoes = map(int, raw_input().split())