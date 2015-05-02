bn = map(int, raw_input().split())
saldo_banco = map(int, raw_input().split())
 
while (bn != [0, 0]):
    num_bancos = bn[0]
    num_debentures = bn[1]
     
    for i in range(num_debentures):
        dcv = map(int, raw_input().split())
         
        banco_devedor = dcv[0]
        banco_credor = dcv[1]
        valor_debenture = dcv[2]
         
        saldo_banco[banco_devedor - 1] -= valor_debenture
        saldo_banco[banco_credor - 1] += valor_debenture
        
    resultados = []
    for i in range(len(saldo_banco)):
        if (saldo_banco[i] >= 0):
            resultados.append(True)
        else:
            resultados.append(False)
             
    if (False in resultados):
        print "N"
    else:
        print "S"
 
    bn = map(int, raw_input().split())
    if (bn != [0, 0]):
        saldo_banco = map(int, raw_input().split())