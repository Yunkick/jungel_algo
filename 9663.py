import sys

N = int(sys.stdin.readline())

ans = 0
v1 = [0] * N
v2 = [0] * (N*2)
v3 = [0] * (N*2)

def dfs(n):
    global ans
    if n == N:
        ans += 1
        return
    else:
        for i in range(N):
            if v1[i] == v2[n+i] == v3[n-i]== 0:
                v1[i] = v2[n+i] = v3[n-i] = 1
                dfs(n+1)
                v1[i] = v2[n+i] = v3[n-i] = 0


dfs(0)
print(ans)