import sys

def fact(n):
    if n == 0:
        return 1
    else:
        n = n * fact(n-1)
        return n 
    
a = int(sys.stdin.readline())
print(fact(a))
