'''s1 = list(input())
print(s1)       # ['a', 'b', 'c']

s2 = input()
print(s2)       # abc

print(s1[1])
print(s2[1])

s1[1] = 'e'
print(s1)       # ['a', 'e', 'c']
s2 = 'aec'
print(s2)       # aec
s2[1] = 'e'
print(s2)       # TypeError: 'str' object does not support item assignment
'''
# ---
'''N = int(input())
txt = input()

for j in range(8-N+1):      # 회문을 확인하는 구간의 첫 글자 인덱스
    for k in range(N//2):       # 회문의 길이 절반만큼 비교
        if txt[j+k] != txt[j+N-1-k]:        # 비교 글자가 다르면 현재 구간 중지
            break
        else:       # break에 걸리지 않고 for문 종료, 회문이면
            total += 1
print(total)
'''
# ---
# 내 코드
'''T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    len_A = len(A)
    len_B = len(B)

    cnt = 0

for i in range(len(A)):
    if A[i] != B[i]:
        cnt += 1
        for j in range(len(B)):
            if B[j] != B[j+1]:
                cnt += 1
    else:
        continue

    print(f'#{tc} {cnt}')
'''
# 함수
'''def min_switch_operations(T, test_cases):
    results = []
    for t in range(T):
        N, A, B = test_cases[t]
        count = 0

        for i in range(N):
            if A[i] != B[i]:  # 현재 상태와 목표 상태가 다르면 스위치 눌러야 함
                count += 1
                # i번부터 N번까지 상태 반전
                for j in range(i, N):
                    A[j] = 1 - A[j]

        results.append(f"#{t + 1} {count}")

    for result in results:
        print(result)


# 입력 처리
T = int(input().strip())
test_cases = []
for _ in range(T):
    N = int(input().strip())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    test_cases.append((N, A, B))

# 결과 출력
min_switch_operations(T, test_cases)
'''
# 함수 x
'''
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0

    for i in range(N):
        if A[i] != B[i]:  # 현재 상태와 목표 상태가 다르면 스위치 눌러야 함
            cnt += 1
            # i번부터 N번까지 상태 반전
            for j in range(i, N):
                A[j] = 1 - A[j]

    print(f'#{tc} {cnt}')
'''
# ---
'''
i번째 돌을 사이에 두고 마주보는 j개의 돌
같은 색이면 뒤집고, 다른 색이면 그대로 둔다.
주어진 돌을 벗어나는 경우 뒤집기 중지

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    i, j = map(int, input().split())

    A[i]
'''

# ---
'''T = int(input())

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
'''
# ---
# T = int(input())
# results = []
# for t in range(1, T + 1):
#     N, M = map(int, input().split())
#     stones = list(map(int, input().split()))
#     flips = [tuple(map(int, input().split())) for _ in range(M)]
#
#     for i, j in flips:
#         left, right = i - 2, i
#         while left >= 0 and right < N:
#             if stones[left] == stones[right]:
#                 stones[left] ^= 1
#                 stones[right] ^= 1
#             else:
#                 break
#             left -= 1
#             right += 1
#
#         result = f"#{t} "
#         for stone in stones:
#             result += str(stone) + " "
#
#         results.append(result)
#     for res in results:
#         print(res)

# ---
T = int(input())  # 테스트 케이스의 개수

for tc in range(1, T + 1):
    N = int(input())  # 격자 크기 N
    arr = [list(map(int, input().split())) for _ in range(N)]  # NxN 격자

    sum_row = [sum(row) for row in arr]  # 각 행의 합
    sum_col = [sum(arr[i][j] for i in range(N)) for j in range(N)]  # 각 열의 합

    max_score = float('-inf')  # 최대 점수 차이를 구하기 위한 변수

    # 두 풍선을 선택해서 얻는 점수 차이의 최대값을 구함
    for r1 in range(N):
        for c1 in range(N):
            score1 = sum_row[r1] + sum_col[c1] - arr[r1][c1]  # 첫 번째 터짐에서 얻는 점수

            for r2 in range(N):
                for c2 in range(N):
                    if r1 == r2 and c1 == c2:
                        continue  # 같은 풍선을 두 번 터트리면 안됨
                    score2 = sum_row[r2] + sum_col[c2] - arr[r2][c2]  # 두 번째 터짐에서 얻는 점수
                    max_score = max(max_score, abs(score1 - score2))  # 점수 차이의 최대값 갱신

    print(f"#{tc} {max_score}")
