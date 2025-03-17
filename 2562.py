arr = []
maximum = 0
max_index = 0

for i in range (9):
    num = int(input())
    arr.append(num)

    if num > maximum:
        maximum = num
        max_index = i

print (maximum)
print (max_index+1)
