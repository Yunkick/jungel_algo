import sys

n, r = map(int, sys.stdin.readline().split())
arr = list(range(1, n + 1))

result = [0] * r
checklist = [0] * n

def DFS(L):
    if L == r:
        print(*result)  # 리스트 형식 대신 공백을 포함한 숫자 출력
    else:
        for i in range(len(arr)):
            if checklist[i] == 0:  # 이미 선택한 숫자는 건너뜀 (백트래킹)
                result[L] = arr[i]
                checklist[i] = 1
                DFS(L + 1)
                checklist[i] = 0  # 백트래킹 (되돌리기)

DFS(0)
