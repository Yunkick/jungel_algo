import sys  

a = int(sys.stdin.readline())
b = [] * a

for i in range(a):
    b.append(int(sys.stdin.readline()))

x = sorted(b)
for i in range(len(x)):
    print(x[i])
