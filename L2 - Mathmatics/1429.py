def fatorial(n):
    if n == 1:
        return 1
 
    return n * fatorial(n - 1)
 
while True:
    numero_acm = raw_input()
 
    if numero_acm == "0": break
 
    numero = 0
    for i in range(len(numero_acm)):
        numero += int(numero_acm[i]) * fatorial(abs(i - len(numero_acm)))
 
    print numero