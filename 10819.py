import sys

n = int(sys.stdin.readline()) #
arr = [] #순열을 저장할 배열
total = 0 #배열에서 수식을하고 잠깐 저장해서 answer이랑 비교
answer = 0 #비교해서 큰값 저장
A = list(map(int,sys.stdin.readline().split())) #리스트를 받음
checklist = [0] * len(A) #백트래킹 할때 필요한 배열
def tam(a):
    global answer
    if a == n: #재귀함수값이 n 이 되었을때
        total = 0
        for i in range(n-1):
            total += abs(arr[i] - arr[i+1])
        answer = max(total,answer)
        return

    else:
        for i in range(len(A)):
            if checklist[i] == 0:
                checklist[i] = 1
                arr.append(A[i]) 
                tam(a+1)
                checklist[i] = 0
                arr.pop()
tam(0)

print(answer)