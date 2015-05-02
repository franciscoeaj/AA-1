import sys
sys.setrecursionlimit(100000)
 
def ultima_cidade(n, k):
    if (n == 1):
        return 0
    else:
        return (ultima_cidade(n - 1, k) + k) % n
 
n = int(raw_input())
 
while (n > 0):
    m = 1
    while (ultima_cidade(n - 1, m) + 2 != 13):
        m += 1
 
    print m
 
    n = int(raw_input()