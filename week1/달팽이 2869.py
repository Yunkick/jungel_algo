a, b, v = map(int,input().split())
count = 0
current = 0
total = 0
for _ in iter(int,1):
    count = count + 1
    current = current + a
    
    if v <= current:
        print (count)
        
        break
    current = current - b
    
    
    
