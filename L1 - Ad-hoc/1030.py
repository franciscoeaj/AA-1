import sys
sys.setrecursionlimit(100000)
 
def sobrevivente(n, k):
    if (n == 1):
        return 0
    else:
        return (sobrevivente(n - 1, k) + k) % n
 
n = int(raw_input())
 
for i in range(n):
    dados = map(int, raw_input().split())
    pessoas = dados[0]
    intervalo = dados[1]
 
    print "Case %d:" % (i + 1), sobrevivente(pessoas, intervalo) + 1