a, b= map(int,input().split())
a = str(a)[::-1]
b = str(b)[::-1]


if int(a) < int(b) :
    print (b)
else:
    print (a)