import sys

def search(arr, num):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left+right)//2
        if arr[mid] == num:
            return 1
        if arr[mid] > num :
            right = mid - 1
        else:
            left = mid + 1
    return 0


n = int(sys.stdin.readline())
x = list(map(int,sys.stdin.readline().split()))
b = int(sys.stdin.readline())
y = list(map(int,sys.stdin.readline().split()))

x.sort()

for i in y:
    print(search(x, i))