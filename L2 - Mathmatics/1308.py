import math
 
n = int(raw_input())
 
for i in xrange(n):
    guerreiros = int(raw_input())
    linhas = int(math.sqrt(guerreiros*2 + 3.0/4) - 1.0/2)
     
    print linhas