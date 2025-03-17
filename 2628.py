a, b = map(int, input().split())
c = int(input())

가로 = [0, b]  
세로 = [0, a]  

for _ in range(c):
    f, d = map(int, input().split())
    
    if f == 0:
        
        가로.append(d)
    else:
        
        세로.append(d)


가로.sort()
세로.sort()


최대가로차이 = max(가로[i] - 가로[i-1] for i in range(1, len(가로)))
최대세로차이 = max(세로[i] - 세로[i-1] for i in range(1, len(세로)))


print(최대가로차이 * 최대세로차이)
