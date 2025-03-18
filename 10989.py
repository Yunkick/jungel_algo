a = int(input())

arr = []

count = [0] * (a +1)

for i in range(a):
    arr.append(int(input()))
# print(arr)


for num in arr:
    count[num] += 1
# print(count)

sorted_arr = []
for num in range(len(count)):
    for _ in range (count[num]):
        sorted_arr.append(num)


for i in range (len(sorted_arr)):
    print(sorted_arr[i])