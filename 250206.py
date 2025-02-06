# n = int(input())
#
# for i in range(n):
#     print("".join(str(j) for j in range(n + i, 2 * n + i)))

# n = int(input())  # 정수 입력 받기
#
# for i in range(n):  # 1중 for문만 사용
#     print("".join(str(j) for j in range(n + i, n + i + (n + 1))))

# n = int(input())  # 정수 입력 받기

#
# for i in range(n):  # 1중 for문 사용
#     print("".join(str(j) for j in range(n + i, n + i + (n + 1))))
#
# for i in range(n):
#

# n = int(input())  # 정수 입력 받기
#
# for i in range(n + 1):
#     for j in range(n + i, n + i + n):
#         print(j, end=" ")
#     print()
#
# n = int(input())
#
# for x in range((n + 1) * n):
#     print(x // n + n + x % n, end=' ')
#     if x % n == n - 1:
#         print()

# ---
# swea 23165.

# n = int(input())
#
# for i in range(n, n*2+1):
#     print(i, i+1, i+2)


# swea 23167.
# n = int(input())

# if n % 2 == 0:
#     for i in range(6):
#         print(n + i * 2, end = ' ')
#
# else:
#     for i in range(11):
#         print(n + i * 3, end = ' ')
#
# -----
# final 2.
#
# n = int(input())
# if n % 2 == 0:
#     for i in range(6):
#         print(n + 2*i, end=' ')     # 2의 배수만큼 증가
#
# else:
#     for i in range(11):
#         print(n + 3*i, end=' ')     # 3의 배수만큼 증가
#
#         ----
#
# # 리스트(배열): 여러 개의 객체를 하나의 객체로 묶고 싶다.
# # 1. sequence: 자료형(순서가 있다)
# # 2. 가변형
#
# arr = [1, 2, 3, 4, 5]
#
# # 인덱싱
# 마지막 원소를 인덱싱
# arr[-1], arr[len(arr) -1]
# 이 리스트를 거꾸로 슬라이싱
# arr[::-1]

# swea 리스트 다루기 1
# 내 코드
# arr = [0, 3, 0, 0, 7, 9]    # 이게 하드코딩임
# arr = [0] * 6
#
# arr[4] = int(input())
# arr[5] = int(input())
#
# sum_result = arr[4] + arr[5]
# print(sum_result)
#
# # 강사님 코드
# arr = [0] * 6
# arr[1] = 3
# arr[4] = 7
# arr[5] = 9
# print(arr[4] + arr[5])

# ---
# 23182.
# n = int(input())
#
# arr = [n, 3, 2, 3 + 2]
#
# print(*arr)

# 강사님 코드
# arr = [1, 3, 2, -5]
#
# arr[0] = int(input())
# arr[3] = arr[1] + arr[2]
#
# print(*arr)
# # 언패킹 연산자 안 쓴다면
# print(' '.join(arr))    # TypeError <- join은 str만 쓸 수 있음
# print(' '.join(str(arr)))   # 그냥 str() 안 됨 <- 그냥 정수면 됨, 근데 얘는 리스트, 각각의 요소를 str로 바꿔줘야 하는 상황이기 때문
# print(' '.join(map(str, arr)))


# ---
# 23184.
# arr = [9, 5, 1, 15, 7, 3]
#
# for i in arr:
#     print()

# ---
# 23183.
# arr = [9, 5, 1, 15, 7, 3]
#
# for i in range(len(arr) - 1, -1, -1):
#     print(arr[i], end = ' ')

# 강사님 코드
# arr = [9, 5, 1, 15, 7, 3]

# for i in range(len(arr)) - 1, -1, -1):
#     print(i, end = ' ')

# ---
# 23187.
# 8칸의 리스트 만들기
# arr = []
#
# for i in range(4):
#     arr.append(7)
#
# for i in range(4):
#     arr.append(15)
#
# print(*arr)

# 강사님 코드
# arr = [0] * 8
#
# for i in range(4):
#     arr[i] = 7
#
# for j in range(4, 8):
#     arr[j] = 15
#
# print(*arr)

# ---
# 23190.
# arr = []
#
# for i in range(5):
#

# ---
# 리스트 2번째 이론

# a = []
# ---> a = [10, 10, 10, 10, 10, 10] 이렇게 채우고 싶다면

# 첫 번째 방법.
# for i in range(6):
#     a.append(10)
#
# # 두 번째 방법.
# a = [0] * 6
# for i in range(6):
#     a[i] = 10
#
# print(*a)

# 결론: 둘 다 알고 있어야 함

# ---
# 23194.
# 1.
# arr = []

# for i in range(10, -3, -3):
#     arr.append(i)
#
# print(*arr)

# 강사님 코드
# 1.
# for i in range(10, -3, -3):
#     arr.append(i)
# 2. ***
# arr = []
# t = 10  # 초기값이 10이기 때문
# for i in range(5):
#     t -= 3
#     arr.append(t)
#
# print(*arr)



#
#
# swea 4.
# n = int(input())
#
# if n > 10:
#     for i in range(5):
#         print('#', end = '')
#
# else:   # if 2번 쓰지 마세요
#     for i in range(n):
#         print('#', end = '')
#
# # swea 5.
# start와 end를 입력 받고, start부터 end까지 출력
# -> 2가지 경우
# 1. start < end
# for i in range(start, end+1):
#
# 2. start > end
# for i in range(start, end-1, -1)
#
# 핵심: 수직선 상에서 end는 항상 포함하지 않는다.
#
# for i in range(5, 1, -2):
#     print(i, end = ' ')     # 5 3   # 1 출력 x(end는 항상 포함 x)
#
# for i in range(1, 7, 2):
#     print(i, end = ' ')     # 1, 3, 5
# ---
# for i in range(1, 11):
#     print(i, end = '')
#
# print()
#
# for j in range(10, 0, -1):
#     print(j, end = ' ')
# ---
# 6.
# a, b = map(int, input().split())

# ---

# 23194.

# arr = []
#
# T = list(map(int, input().split()))
# a= T[0]
# b= T[1]
#
# for _ in range(3):
#     arr.append(a)
#
# for _ in range(2):
#     arr.append(b)
#
# for _ in range(3):
#     arr.append(a + b)
#
# print(*arr)

# ---
# 23196.
# arr = [2, 5, 1, 6, 4, 3]
#
# total_sum = 0
#
# for i in arr:
#     total_sum += i
#
# print(total_sum)

# 강사님 코드
# sum_v = 0     # **** 평가 때 초기화 안 하면 감점
# arr = [2, 5, 1, 6, 4, 3]
#
# # 1. 인덱싱 방식
# for i in range(len(arr)):
#     sum_v += arr[i]
#
# # 2. iterator 방식(더 파이써닉)
# for a in arr:
#     sum_v += a


# ---
# 23198.
# n = int(input())
#
# for i in range(n):
#     for j in range(n):
#         print('#', end='')
#     print()

# ---
# 23200.
# arr = ['A', 'B', 'Q', 'T']
#
# for i in range(4):
#     for j in range(len(arr)-1, -1, -1):
#         print(arr[j], end='')
#     print()

# 강사님 코드
# arr = ['A', 'B', 'Q', 'T']
# for i in range(4):
#     for j in range(3-1, -1, -1):
#         print(arr[j], end='')
#     print()


# -----
# 23203.
# 방법 1
# for y in range(4):
#     for x in range(4):
#         print(y, end='')
#     print()

# 강사님 코드


# ---
# 23206.
# 내 코드
# for i in range(1, 4):
#     for j in range(1, 5):
#         print(i, end = '')
#     print()
#
# # 지피티 코드
# for y in range(1, 4):
#     for x in range(1, 5):
#         print(y, x)

# 강사님 코드
# 첫 번째 방법.
# for y in range(4):  # 행 순회
#     for x in range(4):  # 열 순회
#         # y가 0일 때 4번 반복, y가 1일 때 4번 반복, y가 2일 때 4번 반복, y가 3일 때 4번 반복
#         print(y, end = '')
#
# # 두 번째 방법.
# t = 0
# for y in range(4):
#     for x in range(4):
#         print(t, end='')
#     t += 1  # 들여쓰기 얼마나 할지 너무 중요 ***
#     print() # 들여쓰기 얼마나 할지 너무 중요 ***



# ---
# 탐색: 처음부터 끝까지 전부 찾는 것
# 1. 전체 순회
# 2. cnt 변수 활용
# arr = [1, 4, 6, 1, 1, 9, 6]
# # Q) 탐색해서 1이 몇 개인지 counting
#
# cnt = 0
# for a in arr:
#     if a == 1:
#         cnt += 1
# print(cnt)

# 23213.
# arr = list(map(int, input().split()))
#
# cnt = arr.count(7)
#
# print(cnt)

# ---
# 2차원 배열은 1차원 배열을 여러 개 묶은 것
# 1. 좌표 찾기
# 2. 빈 배열 만들기 4 x 4 행렬
# MAP = []
# arr = [0] * 4
# for i in range(4):
#     MAP.append(arr)
#
# # List comprehension    # *** 능숙도 높여야 함 # 바로 리스트 컴프 쓰지 말고 논리 이해하고 ㅇㅇ
# arr = [[0] * 4 '''여기 append 생략''' for _ in range(4)]

# 23216.
# arr = [[0] * 4 for _ in range(4)]
#
# arr[0][0] = 7
# arr[1][3] = 1
# arr[2][1] = 3
# arr[3][3] = 9
#
# for value in arr[3]:
#     print(value, end=' ')

# 강사님 코드
# for i in range(4):
#     print(arr[3][i]. end = ' ')

# ---
# 23228.
# arr = [
#     [7, 1, 3, 5],
#     [9, 5, 9, 1],
#     [1, 3, 1, 5],
#     [3, 5, 9, 9]
# ]
#
# print(arr[0][1])
# print(arr[1][2])
# print(arr[2][3])
# print(arr[3][0])

# ---
# 23230.
# arr = [
#     [7, 1, 3, 5],
#     [9, 5, 9, 1],
#     [1, 3, 1, 5],
#     [3, 5, 9, 9]
# ]
#
# for row in arr:
#     print(row[2], end=' ')

# 가로로 나오는 거 맞음. # 첫 줄 튀어나오고, 그 줄의 [2] 나오고 / 두 번째 줄 튀어나오고, 그 줄의 [2] 나오고 ...

# ---
# 23233.
# arr = [
#     [5, 4, 2, 1],
#     [3, 7, 7, 7],
#     [2, 2, 1, 1]
# ]
#
# for col in range(len(arr[0])):
#     for row in arr:
#         print(row[col], end=' ')
#     print()

# ---

# 2차원 리스트 입력 받는 법
# 어차피 2차원 배열은 1차원 배열 묶어놓은 것이기 때문에
# 1차원 배열 4번 반복하면 4*4 행렬 됨
# 1차원 배열 입력받는 코드를 4번 반복하면 됨
# ㄴ 근데 비효율
# -> 리스트 컴프리헨션

# MAP = []
# arr = list(map(int, input().split()))
#
# for _ in range(4):
#     MAP.append(arr)
#
# # 리스트 컴프리헨션
# arr = [list(map(int, input().split)) for _ in range(4)]

# 23239.
arr = [list(map(int, input().split())) for _ in range(4)]
print(*arr[::-1])