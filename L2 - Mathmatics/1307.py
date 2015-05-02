def MDC(a, b):
    if (b == 0):
        return a
    else:
        return MDC(b, a % b)
 
def conversor_binario_decimal(binario):
    soma = 0
    for i in range(len(binario)):
        potencia = abs(i - len(binario)) - 1
        if (int(binario[i]) == 1):
            valor = 2 ** potencia
            soma += valor
 
    return soma
 
n = int(raw_input())
 
for i in range(n):
    s1 = raw_input()
    s2 = raw_input()
 
    s1_int = conversor_binario_decimal(s1)
    s2_int = conversor_binario_decimal(s2)
     
    if (MDC(s1_int, s2_int) != s1_int) and (MDC(s1_int, s2_int) > 1):
        result = "All you need is love!"
    else:
        result = "Love is not all you need!"
         
    print "Pair #%d: %s" % (i + 1, result)