n = int(input())

a = (n//10)%10
b = n%10
c = str((a+b)%10)
d = str(b)+c

a = (n//10)+(n%10)
b = 
count = 0

while True:
    n = a+b
    if n == d:
        count += 1
        break


print(d)