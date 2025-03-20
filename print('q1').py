import sys

n, r = map(int,sys.stdin.readline().split())
arr = list(range(1, n + 1))
    



result = [0] * r
checklist = [0] * n

def DFS(L):
    if L == r:
        print(*result)

    else:
        for i in range(len(arr)):
            if checklist[i] == 0:
                result[L] = arr[i]
                checklist[i] = 1
                DFS(L+1)
                checklist[i] = 0

DFS(0)