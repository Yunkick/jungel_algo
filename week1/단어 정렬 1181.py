import sys

a = int(sys.stdin.readline())

arr = []

for i in range(a):
    arr.append(sys.stderr.readline())


arr = set(arr)
arr = list(arr)
arr.sort()
arr.sort(key=len)

for i in range(arr):
    print(i)
