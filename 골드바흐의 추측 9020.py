# import math

# a = int(input())

# def is_prime(n):
#     if n == 1:
#         return False
#     for j in range(2, int(math.sqrt(n)+1)):
#         if n % j == 0:
#             return False
        
#     return True 


# for i in range(a):
#     arr = []
#     diff = 0
#     min_diff = float('inf')
#     best_pair = (0,0)
#     num = int(input())  # 각 num 입력
#     for i in range(2, num):  # 2부터 num-1까지 소수 판별
#         if is_prime(i):
#             arr.append(i)
    
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if arr[i] + arr[j] == num:
#                 diff = abs(arr[i] - arr[j])
#                 if diff < min_diff:
#                     min_diff = diff
#                     best_pair = (arr[i], arr[j])
#     print(best_pair)
# 완전 하드 코딩

for _ in range(a):
    num = int(input())
    A = num//2
    B = num//2

    for _ in range(num//2):
        if is_prime(A) and is_prime(B):
            print (A,B)
            break
        else:
            A += 1
            B -= 1