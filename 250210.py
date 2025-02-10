# def seq_search(a, n, key):
#     for i in range(n):
#         if a[i] == key:
#             return i
#     return -1
#
#
# arr = [4, 9, 11, 23, 2, 19, 7]
# print(seq_search(arr, len(arr), 8))

# =

# key = 11
# ans = -1
# for i in range(len(arr)):
#     if arr[i] == key:
#         ans = i

# print(ans)
# ---
# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# N = 3
# key = 5
# ans = 0     # key가 있으면 1, 없으면 0
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == key:
#             ans = 1
#             break

# =

# def seq_search(arr, n, key):
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == key:
#                 return 1
#     return 0
#
# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# N = 3
# key = 5
# ans = 0
#---
# def seqeuntialSearch2(a, n, key)
#     i ← 0
#     while i<n and a[i]<key:     # 다시보기  # 유효한 범위를 앞에    # T/F
# ---
# def seq_search(a, n, key):
#     for i in range(n):
#         if a[i] == key:
#             return i
#         elif a[i] < key:
#             return -1
#         return -1       # 모든 원소가 key보다 작으면 찾을 수 없음
#
# arr = [4, 9, 11, 23, 2, 19, 7]
#
# arr.sort()
# print(arr)
# print(seq_search(arr, len(arr), 11))    # 다시보기  # 강사님 출력값은 4인데, 나는 -1
# print(seq_search(arr, len(arr), 100))
# ---

# 23370.
# # 내 코드
# n = int(input())
# A = [4, 2, 5, 3, 7, 6]
# B = [5, 3, 7]
#
# a = A[n:]
# b = B
#
# def is_same(a, b):
#     return a == b
#
#     flag = True
#     if flag:
#         print('O')
#     else:
#         print('X')

# ---

# def binarySearch(a, N, key):    # key를 찾으면 인덱스, 실패하면 -1 반환
#     start = 0
#     end = N-1
#     while start <= end:
#         middle = (start + end)//2
#         if a[middle] == key:    # 검색 성공
#             return middle
#         elif a[middle] > key:   # 찾는 값보다 크면
#             end = middle -1         # 왼쪽 구간 선택
#         else:                   # 찾는 값보다 작으면
#             start = middle + 1      # 오른쪽 구간 선택
#
#     return -1                   # 검색 실패

# ---

# def binary_search(a, n, key):
#     start = 0   # 검색 구간 설정
#     end = n-1
#     while start <= end:     # 검색 구간에 1개 이상의 원소가 있으면 검색 실행
#         middle = (start + end) // 2     # 기준 위치 계산
#         if a[middle] == key:        # 검색 성공!
#             return middle
#         elif a[middle] > key:       # key보다 크면 왼쪽 구간 선택
#             end = middle - 1
#         else:       # a[middle] < key, 키보다 작으면 오른쪽 구간 선택
#             start = middle + 1
#     return -1       # 검색구간이 남아있지 않으면, 검색 실패
#
# arr = [2, 4, 7, 9, 11, 19, 23]      # 오름차순 정렬된 배열
# print(binary_search(arr, len(arr), 19))     # 5
# print(binary_search(arr, len(arr), 100))    # -1
# print(binary_search(arr, len(arr), 1))      # -1

# ---

# def selection_sort(a, N):
#     for i in range(N-1):    # 기준위치(최솟값을 찾는 구간의 시작 인덱스)
#         min_idx = i         # 최솟값 인덱스 초기화, 구간의 맨앞 원소를 최솟값으로 가정
#         for j in range(i+1, N):      # 실제 최솟값인지 비교하는 위치
#             if a[min_idx] > a[j]:
#                 min_idx = j
#
#         a[i], a[min_idx] = a[min_idx], a[i]
#
# arr = [10, 25, 64, 22, 11]
#
# selection_sort(arr, len(arr))
# print(arr)      # [10, 11, 22, 25, 64]

# ---
# 과목평가 2번 문제
# ㄴ 19590번(K칸 마법 시전?)과 19591번(벽) 합친 난이도

# ---
# 19590.
# 강사님 코드
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# K = int(input())
#
# def magic(y, x):    # 매개변수 없이 전역변수 -> 함수에서 값을 읽어오기만 할 수 있다. # 매개변수 사용 -> 값을 수정하거나 재할당할 수 있다.
#     dy = [-1, 1, -1, 1]
#     dx = [1, 1, -1, -1]
#     sum_v = 0
#     for i in range(4):
#         for j in range(1, K+1):     # if 0부터 -> 자기자신
#             ny = y + dy[i] * j      # 방향배열에 파워를 곱해준다.
#             nx = x + dx[i] * j
#             if ny<0 or nx>0 or ny>=N or nx>=N: continue
#             sum_v += arr[ny][nx]
#
#     return sum_v
#
# result = 0
# for y in range(N):  # 행 순회
#     for x in range(N):
#         result = max(result, magic(y, x))
#
# print(result)

# NxN 행렬
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# K = int(input())

# 함수!!!
# 매개변수 없이 전역변수 : 값을 읽어오기만 할 수 있다.
# 매개변수 쓴다 : 값을 수정, 재할당
# def magic(y, x):
#     dy = [-1, 1, -1, 1]
#     dx = [1, 1, -1, -1]
#     sum_v = 0
#     for i in range(4): # 방향 대각선 4방향
#         for j in range(1, K + 1): # 마법사의 파워
#             ny = y + dy[i] * j # 방향배열에 파워를 곱해 준다
#             nx = x + dx[i] * j
#             if ny < 0 or nx < 0 or ny >= N or nx >= N: continue
#             sum_v += arr[ny][nx]
#
#     return sum_v
#
# result = 0
# for y in range(N): # 행순회
#     for x in range(N):
#         result = max(result, magic(y, x))
#
# print(result)

# ---
# 평가 - 방향배열이 이 문제보다 어렵게 나오지는 않음
# 서술형은 '정렬' 나옴 cf. DAT 자료구조 23396   # 무슨 정렬 나오는지 강사님께서 힌트
# 19591.
# 핵심: 벽 만나면 break

# N, M = map(int, input().split())
# K = int(input())
# arr = [list(input()) for _ in range(N)]
#
# def bomb(arr):
#     dy = [0, 0, -1, 1]
#     dx = [1, -1, 0, 0]
#
#     for y in range(N):
#         for x in range(M):
#             if arr[y][x] == '@':
#                 for i in range(4):
#                     for k in range(1, K+1):
#                         ny, nx = y + dy[i] * k ,x + dx[i] * k
#                         if ny<0 or nx<0 or ny>=N or nx>=M: continue
#                         if arr[ny][nx] == '_':arr[ny][nx] = '%'
#                         if arr[ny][nx] == '#': break
#
#                 arr[y][x] = '%'
#
# bomb(arr)
# for row in arr:
#     print(*row, sep = '')

# ---
# DAT: Direct Address Table
#
# 1. flag 처리
# flag를 bool타입 변수로 활용(True or False) ---> 1 or 0
# 2. break 사용
#
# Q. arr1과 arr2가 같으면 'O', 틀리면 'X' 출력
'''
arr1 = [1, 4, 2, 5]
arr2 = [1, 4, 3, 5]

flag = 1    # True
for i in range(len(arr1)):
    if arr1[i] != arr2[i]:
        flag = 0    # False
        break

if flag: print('O')
else: print('X')
'''

# 근데 이 flag 처리를 함수로 만들 수 있다. ---> is_same() 함수  # is - 판정 의문문
# arr1 = [1, 4, 2, 5]
# arr2 = [1, 4, 3, 5]
#
# # 내 코드
# def is_same(arr1, arr2):
#     for i in range(len(arr1)):
#         if arr1[i] != arr2[i]:
#             return False
#         else:
#             return True
#
# print(is_same(arr1, arr2))

# 강사님 코드
# def is_same():
#     for i in range(len(arr1)):
#         if arr1[i] != arr2[i]:
#             return 0
#     return 1    # for문 다 순회했는데도 0 return 안 되면
#
# if is_same(): print('O')
# else: print('X')

# ---
# 23370.
# [flag]
# A = [4, 2, 5, 3, 7, 6]
# B = [5, 3, 7]
#
# n = int(input())
#
# flag = 1
# for i in range(len(B)):
#     if A[n + i] != B[i]:
#         flag = 0
#         break
#
# if flag:
#     print('O')
# else:
#     print('X')

# [is_same()]
# A = [4, 2, 5, 3, 7, 6]
# B = [5, 3, 7]
#
# n = int(input())
#
# def is_same(n):
#     for i in range(3):      # '4, 2, 5' -> '2, 5, 3' -> '5, 3, 7' -> ...
#         if A[n + i] != B[i]: return 0
#     return 1
#
# if is_same(n): print('O')
# else: print('X')

# ---
# 23374.
# A = [5, 7, 5, 4, 2, 9]
# B = [5, 4, 2, 5, 6]
#
# # 강사님 코드
# def is_exist(n):
#     # A를 순회해야 할까, B를 순회해야 할까
#     for i in range(5):      # B를 순회
#         if B[i] == n: return 1
#     return 0
#
# # 함수 호출하면서 O나 X를 출력
# for i in range(6):
#     if is_exist(A[i]): print('O', end = ' ')
#     else: print('X', end = ' ')
# ---
# 23376.
# 내 코드
# A = [5, 2, 5, 7, 3]
# n = int(input())
# lst = []
#
# def get_count(n):
#     for i in range(5):
#         if A[i] == n:
#             lst.append(n)
#     return lst
#
# print(len(get_count(n)))

# 강사님 코드
# A = [5, 2, 5, 7, 3]
#
# def get_count(n):
#     cnt = 0
#     for i in range(len(A)):
#         if A[i] == n: cnt += 1
#
#     return cnt
#
# n = int(input())
# ret = get_count(n)
# print(ret)
# ---
# 23382.
# 내 코드
# A = [
#     [5, 5, 2, 6],
#     [9, 1, 1, 3]
# ]
# tar = [5, 6, 1, 1, 1, 1, 5, 4]
#
# def get_count():
#     cnt = 0
#     for i in range(2):
#         for j in range(4):
#             if A[i][j] in tar: cnt += 1
#
#     return cnt
#
# ret = get_count()
# print(ret)      # 5     # 애초에 문제를 잘못 봄. 이거 구하는 문제 x

# 강사님 코드
# A = [
#     [5, 5, 2, 6],
#     [9, 1, 1, 3]
# ]
# tar = [5, 6, 1, 1, 1, 1, 5, 4]
#
# def get_count(n):
#     cnt = 0
#     # target을 순회
#     for i in range(len(tar)):
#         if tar[i] == n: cnt += 1
#     return cnt
#
# # A를 행순회
# for y in range(2):
#     for x in range(4):
#         result = get_count(A[y][x])     # result에는 cnt가 할당
#         print(result, end = ' ')
#     print()

# ---
# [DAT, Direct Address Table]
# : 값을 인덱스로 쓰는 자료구조
# (예)
# arr = [4, 2, 4, 4, 2]
# dat 배열에서는 0, 1, 2, 3, 4(인덱스)
# cf. SWEA - 버스 노선

# [DAT 자료구조 왜 쓸까?(vs get_count())
# arr = [4, 4, 5, 5, 9, 1]
# for문 순회 - O(n)
# DAT 배열 - 미리 초기 세팅, for문 순회 x, 바로 갯수 확인 가능 - O(1), 매우 빠르다

# [한계]
# 1. 메모리를 많이 잡아먹는다.
# 2. 음수 처리 불가능

# 예시 1.
'''
A = [4, 2, 4, 4, 2]
dat = [0] * 5
idx = 0

for i in range(len(A)):
    idx = A[i]      # 값을 인덱스로
    dat[idx] += 1   # counting

# print(dat)
for i in range(len(A)):
    if dat[i] > 0: print(f'{i} : {dat[i]}')

# 예시 2.
# 'BTSKFCBBQ' 문자열에서 각 알파벳이 몇 개씩 있을까?
text = 'BTSKFCBBQ'
# 아스키 코드    # 대문자 / 소문자
dat = [0] * 200

for i in range(len(text)):
    dat[ord(text[i])] += 1 # 문자의 아스키코드를 dat배열의 인덱스

# print(dat)
for i in range(200):
    if dat[i] == 0: continue
    print(f'{chr(i)} : {dat[i]}')    # 아스키코드로 바꾼 것을 다시 문자로 바꿔서 출력
'''






# 23383.
# arr = [
#     [1, 5, 10, 15],
#     [15, 15, 20, 30]
# ]
#
# n = int(input())
#
# def get_count(n):
#     cnt = 0
#     for i in range(2):
#         for j in range(4):
#             if arr[i][j] == n: cnt += 1
#     return cnt
#
# ret = get_count(n)
# print(ret)

# [dat배열]
# arr = [
#     [1, 5, 10, 15],
#     [15, 15, 20, 30]
# ]
# dat = [0] * 31
# idx = 0
# n = int(input())
#
# for i in range(2):
#     for j in range(4):
#         idx = arr[i][j]
#         dat[idx] += 1
#
# for i in range(2):
#     for j in range(4):
#         if arr[i][j] == n:
#
# print(dat[idx])

# 강사님 코드
# arr = [
#     [1, 5, 10, 15],
#     [15, 15, 20, 30]
# ]
#
# dat = [0] * 31      # 0부터 30이니까 31개
#
# for y in range(2):
#     for x in range(4):
#         dat[arr[y][x]] += 1     # 값이 인덱스로, counting
#
# n = int(input())
# print(dat[n])

# ---
# 23387.
# text = 'ABCDE'
# dat = [0] * 200
# x, y, z = map(int, input().split())
#
# for i in range(len(text)):
#     if dat[text[i]]
#
#
#
#
#
# for i in range(len(text)):
#     if is_exist(text[i]): print('O', end = ' ')
#     else: print('X', end = ' ')

# 강사님 코드
# text = 'ABCDE'
#
# dat = [0] * 200
#
# arr = list(input().split())
# # print(arr)
#
# # 과정 1. DAT 배열 채우기
# for i in range(len(text)):
#     dat[ord(text[i])] = 1
#
# # 과정 2. 하나씩 검사
# for i in range(3):
#     ch = arr[i]  # 문자 하나를 ch에 할당
#     if dat[ord(ch)] == 1:
#         print('O', end=' ')
#     else:
#         print('X', end=' ')

# ---
# 23388.
# text = 'BBQBHCBTS'
#
# dat = [0] * 200
#
# for i in range(len(text)):
#     dat[ord(text[i])] == 1:

#
# text = 'BBQBHCBTS'
#
# dat = [0] * 200
#
# for char in text:
#     dat[ord(char)] += 1
#
# max_count = max(dat)
#
# print(max_count)

# 강사님 코드
# text = 'BBQBHCBTS'
#
# dat = [0] * 200
#
# for i in range(len(text)):
#     dat[ord(text[i])] += 1
#
# max_v = 0
# for i in range(200):
#     if dat[i] > max_v: max_v = dat[i]   # 최댓값 코드
#
# print(max_v)

# ㄴ for문 2개, but 중첩 x -> 시간복잡도: O(n)

# ---
# 23390.
# land = [
#     [4, 5, 7, 6],
#     [1, 5, 5, 4],
#     [1, 1, 1, 1]
# ]
#
# resident = [
#     [5, 6, 4],
#     [1, 5, 3]
# ]
#
# dat = [0] * 200
#
# for y in range(3):
#     for x in range(4):
#         dat[arr[y][x]] += 1     # 값이 인덱스로, counting
#
# n = int(input())
# print(dat[n])

#
# land = [
#     [4, 5, 7, 6],
#     [1, 5, 5, 4],
#     [1, 1, 1, 1]
# ]
#
# resident = [
#     [5, 6, 4],
#     [1, 5, 3]
# ]
#
# dat = [0] * 200
#
# for row in land:
#     for i in row:
#         dat[i] += 1
#
# for res in resident:
#     for i in res:
#         print(dat[i], end=" ")
#     print()

# 강사님 코드
# 2차원 리스트 dat 안 쓰면, get_count() 함수 쓰면 4중 for문

arr = [
    [4, 5, 7, 6],
    [1, 5, 5, 4],
    [1, 1, 1, 1]
]

tar = [
    [5, 6, 4],
    [1, 5, 3]
]

dat = [0] * 100

for y in range(3):
    for x in range(4):
        dat[arr[y][x]] += 1

for y in range(2):
    for x in range(3):
        print(dat[tar[y][x]], end = ' ')
    print()


# ---
# 23394.
# criminal = [
#     [5, 7, 9, 55],
#     [30, 10, 6, 8]
# ]
#
# resident = [
#     [1, 2, 3, 4],
#     [5, 7, 10, 15]
# ]

#

# criminal = [
#     [5, 7, 9, 55],
#     [30, 10, 6, 8]
# ]
#
# resident = [
#     [1, 2, 3, 4],
#     [5, 7, 10, 15]
# ]
#
# dat = [0] * 100
#
# for row in resident:
#     for i in row:
#         dat[i] = 1
#
# criminal_num = 0
# for row in criminal:
#     for j in row:
#         if dat[j]:
#             criminal_num += 1
#
# total_num = 0
# for row in resident:
#     for n in row:
#         if dat[n]:
#             total_num += 1
#
# good_citizen_num = total_num - criminal_num
#
# print(criminal_num, good_citizen_num)

# 강사님 코드
criminal = [
    [5, 7, 9, 55],
    [30, 10, 6, 8]
]

person = [
    [1, 2, 3, 4],
    [5, 7, 10, 15]
]

dat = [0] * 100

crim = 0
per = 0

# dat배열 범죄자
for y in range(2):
    for x in range(4):
        dat[criminal[y][x]] = 1

for y in range(2):
    for x in range(4):
        if dat[person[y][x]] == 1: crim += 1    # 범죄자
        else: per += 1      # 일반 시민

print(crim, per)