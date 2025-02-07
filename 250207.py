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
di = [0, 1, 0, -1]     # 오른쪽부터 시계방향으로
dj = [1, 0, -1, 0]

N = 2
M = 3
for i in range(N):
    for j in range(M):
        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]
            if 0<=ni<=N and 0<=nj<M:    # 행렬을 벗어나면 없는 걸로 하는 ㅇㅇ
                print(ni, nj)

