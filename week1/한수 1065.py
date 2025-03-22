


def 한수(n):
    b = (n//100)%10
    c = (n//10)%10
    d = n%10

    if n < 100 :
        return True
    if 1000> n >= 100 and b - c == c - d:
        return True
    
    
    return False
    
    
n = int(input())



count = 0

for i in range(1, n+1):
    if 한수(i) == True:
        count += 1
print(count)
