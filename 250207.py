# [온라인]

# '''
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# '''
# N = int(input())    # 배열 행과 열의 크기
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# print(arr)

# arr2 = [[0] * N for in range(3)]
# print(arr2)

# for i in range(N):
#     for j in range(N):
#         print(arr[i][j])

# for i in range(n):
#     for j i range(m):
#         f(array[i][j + (m-1-2*j) * (i%2)])  # (i%2)를 곱해주면 짝수일 때는 (m-1-2*j) * (i%2) 없어짐, j만 남음




# di = [0, 1, 0, -1]     # 오른쪽부터 시계방향으로
# dj = [1, 0, -1, 0]
#
# i = 2
# j = 3
# for dir in range(4):
#     ni = i + di[dir]
#     nj = j + dj[dir]
#     print(ni, nj)

# 모든 칸의 인접 원소들의 합을 구해보자
# di = [0, 1, 0, -1]     # 오른쪽부터 시계방향으로
# dj = [1, 0, -1, 0]

# N = 2
# M = 3
# 1.
# for i in range(N):
#     for j in range(M):
#         for dir in range(4):
#             ni = i + di[dir]
#             nj = j + dj[dir]
#             if 0<=ni<=N and 0<=nj<M:    # 행렬을 벗어나면 없는 걸로 하는 ㅇㅇ
#                 print(ni, nj)


# 2.
# for i in range(N):
#     for j in range(M):
#         for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#             ni = i + di
#             nj = j + dj
#             if 0<=ni<N and 0<=nj<M:
#                 print(ni, nj, i, j)


# =============================================
# 23228.
# arr = [
#     [7, 1, 3, 5],
#     [9, 5, 9, 1],
#     [1, 3, 1, 5],
#     [3, 5, 9, 9]
# ]
#
# print(arr[0][1])

# =========================
# 디버깅이란,
# input 넣었는데 output 달라
# 문제 제출 ---> 100개 테케 중 87개 통과
# ㄴ 이런 상황일 때 하는 게 '디버깅'
#
# 1. breaking point를 찍는다.(중단점)
# - 내가 알고싶은 값, 처음부터 살펴보려면 for문 처음 순회할 때, 함수호출하는 부분
#
# 2. input값 입력하고, step over로 하나씩 살펴본다.
#     만약 함수가 있는 경우, 함수 안으로 들어가려면 step into로 들어간다.
#
# 빨간 불이 breakpoint

# =======================================
# 우리가 for문 배웠는데: 순회(열순회, 행순회)
# 탐색
# 방향배열 자료구조:
# 한 지점을 선택했을 때 상, 하, 좌, 우, 대각선 원하는 방향으로 탐색하는 자료구조



# 23289.

# arr = [
#     [1, 2, 1, 3, 1],
#     [2, 2, 2, 2, 2],
#     [1, 0, 1, 0, 1],
#     [3, 1, 2, 1, 3]
# ]

# arr[1][2]
#
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]

# for i in range(N):
#     for j in range(N):
#         for di, dj in

# sum_v = 0
# for i in range(N):
#     for j in range(N):
#         s = arr[i][j]
#         for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:



# sum_v = 0
# row, col = 1, 2
# s = arr[1][2]
#
# for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#     ni, nj = s + di, s + dj
#     if 0<=ni<len(arr) and 0<=nj<len(arr[0]):
#         s += arr[ni][nj]
#
# sum_v = s
#
# print(sum_v)


# arr = [list(map(int, input().split())) for _ in range(5)]
#
# cnt = 0
# sum_v = 0
# max_v = float('-inf')
#
# for y in range(5):
#     for x in range(5):
#         # 2의 개수 세기
#         if arr[y][x] == 2:
#             cnt += 1
#         # 최댓값 갱신
#         if arr[y][x] > max_v:
#             max_v = arr[y][x]
#         # 최솟값 갱신	# 최대값 갱신 코드와 부등호 방향만 반대
#         if arr[y][x] < min_v:
#             min_v = arr[y][x]
#     # 대각선 합 계산
#     sum_v += arr[y][y]
#
# print(cnt)
# print(max_v, min_v)
# print(sum_v)

# ======
# 23289.
# 내 코드 - 노가다
# arr = [
#     [1, 2, 1, 3, 1],
#     [2, 2, 2, 2, 2],
#     [1, 0, 1, 0, 1],
#     [3, 1, 2, 1, 3]
# ]
#
# point = arr[1][2]
#
# point_up = arr[0][2]
# point_down = arr[2][2]
# point_left = arr[1][1]
# point_right = arr[1][3]
#
# sum_v = point_up + point_down + point_left + point_right
# print(sum_v)


# 강사님 코드 - 방향 배열 x
# arr = [
#     [1, 2, 1, 3, 1],
#     [2, 2, 2, 2, 2],
#     [1, 0, 1, 0, 1],
#     [3, 1, 2, 1, 3]
# ]
#
# y = 1
# x = 1
# sum_v = 0
# # 하나하나 인덱싱해서 sum_v에 누적
# sum_v += arr[y-1][x+0] # 상
# sum_v += arr[y+1][x+0] # 하
# sum_v += arr[y+0][x-1] # 좌
# sum_v += arr[y+0][x+1] # 우
#
# print(sum_v)

# 강사님 코드 - 방향배열 o
# y의 방향 배열: dy = [-1, 1, 0, 0]
# x의 방향 배열: dx = [0, 0, -1, 1]

# d: direct
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
#
# for i in range(4): #상, 하, 좌, 우 ----> 4방향
#         ny = y + dy[i]
#         nx = x + dx[i]
#         sum_v += arr[ny][nx]

# print(sum_v)
#
#
#
# # 23291.
# 0<=ny<4 and 0<=nx<5

# arr = [
#     [1, 2, 1, 3, 1],
#     [2, 2, 2, 2, 2],
#     [1, 0, 1, 0, 1],
#     [3, 1, 2, 1, 3]
# ]
#
# y = 0
# x = 1
#
# sum_v = 0
#
# # 상하좌우 이동 방향
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
#
# # 초기값 설정
# point = arr[y][x]
#
# # 상하좌우 값 더하기
# for dy, dx in directions:
#     ny, nx = y + dy, x + dx
#     if 0 <= ny < len(arr) and 0 <= nx < len(arr[0]):
#         s += arr[ny][nx]
#
# print("상하좌우 합:", s)

# 내 코드
# arr = [
#     [1, 2, 1, 3, 1],
#     [2, 2, 2, 2, 2],
#     [1, 0, 1, 0, 1],
#     [3, 1, 2, 1, 3]
# ]
#
# point = arr[0][1]
#
# point_down = arr[1][1]
# point_left = arr[0][0]
# point_right = arr[0][2]
#
# sum_v = point_down + point_left + point_right

# print(sum_v)
#
# # 강사님 코드
# arr = [
#     [1, 2, 1, 3, 1],
#     [2, 2, 2, 2, 2],
#     [1, 0, 1, 0, 1],
#     [3, 1, 2, 1, 3]
# ]
#
# y = int(input())
# x = int(input())
#
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
#
# for i in range(4): #상, 하, 좌, 우 ----> 4방향
#         ny = y + dy[i]
#         nx = x + dx[i]
#         if 0 <= ny < 5 and 0 <= nx < 4:
#             sum_v += arr[ny][nx]
#
# print(sum_v)




# 23291.
# arr = [
#     [1, 2, 1, 3, 1],
#     [2, 2, 2, 2, 2],
#     [1, 0, 1, 0, 1],
#     [3, 1, 2, 1, 3]
# ]
#
# y = 0
# x = 1
# sum_v = 0
#
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
#
# for i in range(4): #상, 하, 좌, 우 ----> 4방향
#         ny = y + dy[i]
#         nx = x + dx[i]
#         # if 0 <= ny < 5 and 0 <= nx < 4:
#         #     sum_v += arr[ny][nx]
#         # code ...
#         # if 조건: ---> 들여쓰기를 최소화하자. 들여쓰기 많을수록 가독성 x
#         if ny < 0 or nx < 0 or ny >= 4 or nx >= 5: continue        # 이렇게 하면 들여쓰기 안 해도 됨
#         sum_v += arr[ny][nx]
# print(sum_v)

# 23292.
# arr = [
#     [1, 2, 1, 3, 1],
#     [2, 2, 2, 2, 2],
#     [1, 0, 1, 0, 1],
#     [3, 1, 2, 1, 3]
# ]
#
# y = 2
# x = 2
#
# dy = [-1, -1, 1, 1]
# dx = [-1, 1, 1, -1]
#
# for i in range(4):
#     ny = y + dy[i]
#     nx = x + dx[i]
#
#     if ny < 0 or nx < 0 or ny >= 4 or nx >= 5: continue
#     mul_v *= arr[ny][nx]
#
# print(mul_v)



# arr = [
#     [1, 2, 1, 3, 1],
#     [2, 2, 2, 2, 2],
#     [1, 0, 1, 0, 1],
#     [3, 1, 2, 1, 3]
# ]
#
# y, x = map(int, input().split())
# mul_v = arr[y][x]
#
# dy = [-1, -1, 1, 1]
# dx = [-1, 1, 1, -1]
#
# for i in range(4):
#     ny = y + dy[i]
#     nx = x + dx[i]
#
#     if ny < 0 or nx < 0 or ny >= 4 or nx >= 5: continue
#     mul_v *= arr[ny][nx]
#
# print(mul_v)



# arr = [
#     [1, 2, 1, 3, 1],
#     [2, 2, 2, 2, 2],
#     [1, 0, 1, 0, 1],
#     [3, 1, 2, 1, 3]
# ]
#
# y = int(input())
# x = int(input())
#
# point = arr[y][x]
# point_ur = arr[y-1][x+1]
# point_dr = arr[y+1][x+1]
# point_dl = arr[y+1][x-1]
# point_ul = arr[y-1][x-1]
#
# mul_v = point*point_ur*point_dr*point_dl*point_ul
# print(mul_v)
#
#
# arr = [
#     [1, 2, 1, 3, 1],
#     [2, 2, 2, 2, 2],
#     [1, 0, 1, 0, 1],
#     [3, 1, 2, 1, 3]
# ]
#
# y = int(input())
# x = int(input())
#
# point = arr[y][x]
# point_ur = arr[y-1][x+1]
# point_dr = arr[y+1][x+1]
# point_dl = arr[y+1][x-1]
# point_ul = arr[y-1][x-1]
#
# mul_v = point*point_ur*point_dr*point_dl*point_ul
# print(mul_v)

# =====
# 23300.

# arr = [
#     [1, 2, 1, 3, 1],
#     [2, 2, 2, 2, 2],
#     [1, 0, 1, 0, 1],
#     [3, 1, 2, 1, 3]
# ]
#
# y, x = map(int, input().split())
# max_v_list = [0] * 4
#
# dy = [0, 1, 1, 0]
# dx = [1, 1, 0, -1]
#
# for i in range(4):
#     ny = y + dy[i]
#     nx = x + dx[i]
#
#     if ny < 0 or nx < 0 or ny >= 4 or nx >= 5: continue
#     max_v_list.append(i)
#
# print(*max_v_list)
#
#
# # 23292.
# # 자기자신 1. 자기자신 할당 2. 방향 (0, 0) 할당
#
# # 23292.
# arr = [
#     [1, 2, 1, 3, 1],
#     [2, 2, 2, 2, 2],
#     [1, 0, 1, 0, 1],
#     [3, 1, 2, 1, 3]
# ]
#
# y, x = map(int, input().split())
#
# # 자기자신, 위왼쪽, 위오른쪽, 아래왼쪽
# dy = [0, -1, -1, 1, 1]
# dx = [0, -1, 1, -1, 1]
#
# # gop = arr[y][x]   # 자기자신  # 0으로 초기화하면 뭘 곱해도 0이 되기 때문에 안 됨
# gop = 1
# for i in range(5):
#     ny, nx = y + dy[i], x + dx[i]
#
#     if ny < 0 or nx < 0 or ny >= 4 or nx >= 5: continue     # 테케가 2, 2 밖에 없는 거고 / 입력받는 형식이기 때문에 if문 있어야 됨
#     gop *= arr[ny][nx]
#
# print(gop)

# =======
# 23300.
# arr = [
#     [1, 2, 1, 3, 1],
#     [2, 2, 2, 2, 2],
#     [1, 0, 1, 0, 1],
#     [3, 1, 2, 1, 3]
# ]
#
# y, x = map(int, input().split())
#
# # 아래, 오른쪽, 왼쪽, 오른쪽 아래 대각선
# dy = [1, 0, 0, 1]
# dx = [0, 1, -1, 1]
#
# max_v = float('-inf')
#
# for i in range(4):      # 4번인 이유: 순회해야 하는 방향이 4개이기 때문
#     ny = y + dy[i]
#     nx = x + dx[i]
#
#     if ny < 0 or nx < 0 or ny >= 0 or nx >= 5: continue
#     # 최댓값
#     if arr[ny][nx] > max_v: max_v = arr[ny][nx] # 최댓값 갱신
#
# print(max_v)    # 왜 출력 -inf..?



# arr = [
#     [1, 2, 1, 3, 1],
#     [2, 2, 2, 2, 2],
#     [1, 0, 1, 0, 1],
#     [3, 1, 2, 1, 3]
# ]
#
# y, x = map(int, input().split())
#
# # 아래, 오른쪽 , 왼쪽, 오른쪽아래
# dy = [1, 0, 0, 1]
# dx = [0, 1, -1, 1]
#
# max_v = float('-inf') # 음의 무한대
#
# for i in range(4): # 아래, 오른쪽, 왼쪽, 오른쪽아래 (4방향)
#     ny = y + dy[i]
#     nx = x + dx[i]
#
#     if ny < 0 or nx < 0 or ny >= 4 or nx >= 5: continue
#
#     if arr[ny][nx] > max_v: max_v = arr[ny][nx] # 최대값 갱신
#
# print(max_v)

#==========================
# 19595.

# for i in range(4):
#     for j in range(5):
#         print('_', end = ' ')
#     print()
#
# y1, x1 = map(int, input().split())
# y2, x2 = map(int, input().split())
#
# dy = [-1, -1, 0, 1, 1, 1, 0, -1]
# dx = [0, 1, 1, 1, 0, -1, -1, -1]
#
# for i in range(8):
#     ny = y + dy[i]
#     nx = x + dx[i]
#
#     if ny < 0 or nx < 0 or ny >= 4 or nx >= 5: continue
#
#     if arr[]

# 강사님 코드
arr = [['_'] * 5 for _ in range(4)]

for _ in range(2): # 좌표를 2번 입력받아야 함
    y, x = map(int, input().split())

    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]

    for i in range(8):  # 방향이 총 8 방향
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= 4 or nx >= 5: continue
        arr[ny][nx] = '#'

for row in arr:
    temp = row
    print(*row)



