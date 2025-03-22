n = int(input())

total_score = 0
current_score = 0
for i in range (n):
    text = input()
    current_score = 0
    total_score = 0
    for c in text:
        if c == ('O'):
            current_score += 1
            total_score += current_score
        else:
            current_score = 0
        
    
    print(total_score)
