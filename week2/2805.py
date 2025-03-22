import sys
a , k = map(int,sys.stdin.readline().split())

trees = list(map(int,sys.stdin.readline().split()))

    



right = max(trees)
left = 0

while left <= right:
    mid = (left + right)//2
    total = 0
    for i in trees:
        if i >= mid:
            total += i - mid
    if total >= k:
        left = mid + 1
    else :
        right = mid - 1



print(right)