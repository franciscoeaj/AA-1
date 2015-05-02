dados = map(int, raw_input().split())
  
while (dados != [0, 0]):
    n = dados[0]
    b = dados[1]
    bolas_geradas = []
    bolas_existentes = map(int, raw_input().split())
  
    for i in range(91):
        bolas_geradas.append(0)
  
    total_bolas = 0
    for i in range(b):
        for j in range(i, b):
            bola = abs(bolas_existentes[j] - bolas_existentes[i])
  
            if (bolas_geradas[bola] == 0):
                bolas_geradas[bola] = 1
                total_bolas += 1
  
    if (total_bolas == n + 1):
        print "Y"
    else:
        print "N"
  
    dados = map(int, raw_input().split())