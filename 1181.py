a = int(input())

arr = []

for i in range(a):
    arr.append(input())


arr = set(arr)
arr = list(arr)
arr.sort()
arr.sort(key=len)

print(arr)
