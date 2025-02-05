# [온라인]

'''
6
2 7 5 3 1 4
'''
# N = int(input())
# arr = list(map(int, input().split()))
#
# # 배열원소의 합 s 구하기
# s = 0
# for i in range(N):  # 모든 원소에 대해
#     s += arr[i]
#
# print(s)    # 22

# ---
#
# [SWEA 4828.]
# T = int(input())            # 테스트케이스 개수
# for tc in range(1, T+1):    # 케이스 별로 처리
#     N = int(input())        # 케이스 별 입력 개수
#     arr = list(map(int, input().split()))
#
#     max_v = arr[0]          # 첫 원소를 최댓값으로 가정
#     min_v = arr[0]          # 첫 원소를 최솟값으로 가정
#
#     for i in range(1, N):
#         if max_v < arr[i]:
#             max_v = arr[i]
#         if min_v > arr[i]:
#             min_v = arr[i]
#
#     print(f'#{tc} {max_v-min_v}')

# ==============================
# ==============================

# [오프라인]

# 강사님께서 SWEA에 올려주시는 IM 기출에서 실제 시험에 한두 문제는 똑같이 나옴

# 알고리즘 배워야 하는 이유
# ㄴ 문제 해결하기 위해
# SSAFY 한 학기가 4.5개월인데 그 중 6주가 알고리즘
# ㄴ 딥시크 - 저비용 고성능(HW도 있겠지만 알고리즘 최적화)
# ㄴ 1. 알고리즘 최적화는 곧 저비용 고성능의 핵심 기술
# ㄴ 2. 코딩테스트 통과

# ---

# 첫 번째 이론(SWEA 2반 솔빙 클럽 - 1~4번 문제)

# for i in range(n):
#     print(i, end = ' ')     # 0 1 2 3 ... n-1
# ㄴ n번 반복하는 반복문!

# 1.
# for i in range(9):
#     print('#', end = '')

# 2.
# 나
# for i in range(2):
#     for i in range(3):
#         print('#', end = '')

# for i in range(2):
#     print('###')

# 3.
# 나
n = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for i in range(n):
    print('#', end = '')

for j in range(n+5):
    print('!', end = '')

# 4.
#


