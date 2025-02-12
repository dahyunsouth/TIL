# 고지식한 알고리즘
'''
i = j = 0
while i<N and j<M:
    if t[i] != t[j]:
        i = i - j + 1       # i-j: 시작 위치
        j = 0


    else:       # 같으면
        i += 1
        j += 1

if j == M:
    return i - M        # 시작 위치
    return 1        # 해당 패턴이 있다.

else:
    return 0        # 해당 패턴이 없다.
    retrun -1
'''

# 함수
'''
def bruteforce(p, t):
    N = len(t)
    M = len(p)
    i = j = 0
    while i < N and j < M:
        if t[i] != p[j]:  # 다르면
            i = i - j + 1  # i - j: 비교를 시작했던 위치
            j = 0
        else:  # 같으면
            i += 1
            j += 1
    if j == M:  # while문 벗어난 이유가 j == M 이라면
        return i - j  # 패턴의 시작 인덱스
    else:
        return -1

t = 'TTTZTTATTAATA'
p = 'TTA'

print(bruteforce(p, t))
'''

# 함수 x
'''t = 'TTTZTTATTAATA'
p = 'TTA'
N = len(t)
M = len(p)

i = j = 0
while i<N and j<M:
    if t[i] != p[j]:        # 다르면
        i = i - j + 1       # i - j: 비교를 시작했던 위치
        j = 0
    else:                   # 같으면
        i += 1
        j += 1
if j == M:      # while문 벗어난 이유가 j == M 이라면
    print(i - j)        # 패턴의 시작 인덱스
else:
    print(-1)
'''
# 패턴의 개수
'''
def pattern_count(p, t):    # 패턴의 등장 횟수 리턴
    N = len(t)
    M = len(p)
    i = j = 0
    cnt = 0
    while i < N:
        if t[i] != p[j]:  # 다르면
            i = i - j + 1  # i - j: 비교를 시작했던 위치
            j = 0
        else:  # 같으면
            i += 1
            j += 1
        if j==M:     # 패턴을 찾은 경우
            cnt += 1
            i = i - j + 1
            j = 0
    return cnt


t = 'TTTTTATTAATA'
p = 'TTA'

print(pattern_count(p, t))      # 강사님이랑 답 다름    # git에 올려주심
'''

# KMP 알고리즘
'''def kmp(t, p):
    N = len(t)
    M = len(p)
    lps = [0] * (M+1)
    # preprocessing
    j = 0 # 일치한 개수== 비교할 패턴 위치
    lps[0] = -1
    for i in range(1, M):
        lps[i] = j          # p[i]이전에 일치한 개수
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[M] = j
    # search
    i = 0   # 비교할 텍스트 위치
    j = 0   # 비교할 패턴 위치
    while i < N and j <= M:
        if j==-1 or t[i]== p[j]:     # 첫글자자 불일치했거나, 일치하면
            i += 1
            j += 1
        else:               # 불일치
            j = lps[j]
        if j==M:    # 패턴을 찾을 경우
            print(i-M, end = ' ')    # 패턴의 인덱스 출력
            j = lps[j]

    print()
    return


t = 'zzzabcdabcdabcefabcd'
p = 'abcdabcef'
kmp(t, p)
t = 'AABAACAADAABAABA'
p = 'AABA'
kmp(t, p)
t = "AAAAABAAABA"
p =  "AAAA"
kmp(t, p)
t = "AAAAABAAABA"
p =  "AA"
kmp(t, p)
'''

# ---
# 19774. [Boss] 회문
'''
def is_palindrome(text):
    return text == text[::-1]       # True 또는 False return

def find_palindrome(N, M):
    # return을 어떻게 해야 할까?
    # 가로 방향 회문 찾기(행 순회) -> retrun 회문(문자열)
    for y in range(N):
        for x in range(N-M+1):      # 문자열 검사하면서 배열의 범위 벗어나지 않게 하기 위해 M 뺌
            word = ""
            for k in range(M):
                word += arr[y][x+k]
            # 회문 판별
            if is_palindrome(word):
                return word
    # 세로 방향 회문 찾기(열 순회) -> retrun 회문(문자열)
    for x in range(N):
        for y in range(N-M+1):
            word = ""
            for k in range(M):
                word += arr[y+k][x]
            if is_palindrome(word):
                return word
    # 회문 못 찾았어 -> return ''(빈 문자열) or -1
    return ""

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]        # 입력값이 문자열이기 때문에 map함수 쓸 필요 x
    result = find_palindrome(N, M)      # 디버깅 중단점 여기(함수 호출 지점)
    print(f'#{tc} {result}')
'''

# ---
# 18698. 거스름돈(난이도 low)
'''
n = int(input())
coin_types = [500, 100, 50, 10]
cnt = 0
min_cnt = 0


for coin in coin_types:
    cnt = n // coin
    n = n - coin*cnt
    min_cnt += cnt

print(min_cnt)
'''

# 강사님 코드
'''
price = int(input())
won = [10, 50, 100, 500]
won.sort(reverse=True)
cnt = 0
for i in range(4):
    cnt += (price//won[i])
    price %= won[i]
    
print(cnt)
'''
# ---
# 23461. 화장실 대기시간 줄이기(난이도 low)

'''
총 대기시간이 적은 사용 순서 정하기
-> 사용시간 적은 사람부터


한 사람이 화장실 이용할 때 다른 사람들은 대기
사람들의 전체 대기시간이 최소가 되도록 사용순서 정하고,
-> 사용시간 적은 사람부터
최소 대기시간 출력

people = list(map(int, input().split()))
people.sort()

N = len(people) - 1

wait_time = 0
min_wait_time = 0

for person in people:
    wait_time = person * N
    N = N - 1
    min_wait_time += wait_time

print(min_wait_time)
'''

# 강사님 코드
'''
times = list(map(int, input().split()))

times.sort()

total = 0       # 총 대기시간
for i in range(len(times)):      # 꼭 len 함수 쓰세요  # times가 얼마나 될지 모르니
    
    # 다 못 적음ㅠ
'''

# ---
# 23463. 막대 블럭 채우기(난이도 low)
'''
n = int(input())
sticks = list(map(int, input().split()))
sticks.sort()

space = 100

selected_sticks = []
cnt = 0

for stick in sticks:
    selected_sticks.append(stick)
    if sum(selected_sticks) <= space:
        cnt += 1
    else:
        break

print(cnt)
'''

# 강사님 코드
# <전략>
# 짧은 것부터(오름차순 정렬) 합이 100 넘지 않을 때까지 더하면 된다.(break)

'''
n = int(input())
blocks = list(map(int, input().split()))

blocks.sort()

cnt = 0
total = 0
# 작은 길이부터 하나씩 더해간다
for block in blocks:
    total += block
    if total > 100: break       # 내 코드보다 효율적    # 최대한 덜 탐색
    cnt += 1
    
print(cnt)
'''

# ---
# 22311. 회의실 배정(난이도 mid)

# 전략
# end - start = 소요시간
#
# 최대 회의, 말 그대로 회의를 최대한 많이 해야 함
# 회의를 최대한 많이 한다
# = 겹치면 소요시간 짧은 회의가 그 시간 가져간다
#
# 겹치는지 여부 어떻게 표현할 수 있을까

'''
required_time_lst = []

for num in range(N):
    time = list(map(int, input().split()))
    start = time[0]
    end = time[1]
    required_time = end - start
    required_time_lst.append(required_time)
    required_time_lst.sort()

    for i in required_time_lst:
'''
#
'''
N = int(input())

meetings = []

for num in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))
meetings.sort(key=lambda x: (x[1], x[0]))
print(meetings)

time = 0
max_cnt = 0
for meeting in meetings:
    if time <= meeting[0]:
        time = meeting[1]
        max_cnt += 1

print(max_cnt)
'''

# 강사님 코드
# 전략
# 빨리 끝나는 회의가 우선

'''
n = int(input())
meetings = []

for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

# end 시간을 기준으로 정렬(종료시간이 같다면, 시작시간이 빠른 순으로)
meetings.sort(key=lambda x: (x[1], x[0]))

cnt = 1
end_time = meetings[0][1]

for i in range(1, n):
    # 현재 회의 시작시간이 이전 회의 종료시간보다 크거나 같으면
    if meetings[i][0] >= end_time:
        cnt += 1
        # 현재 회의 종료시간 갱신
        end_time = meetings[i][1]
print(cnt)
'''

# ---
# 23464. 냉장고(난이도 mid)

#
N = int(input())

temperatures = []

for _ in range(N):
    start, end = map(int, input().split())
    temperatures.append((start, end))

temperatures.sort(key=lambda x: x[1])

min_cnt = 0
refrigerator = 0

for start, end in temperatures:
    if start > refrigerator:
        min_cnt += 1
        refrigerator = end

print(min_cnt)

# 강사님 코드
# <전략>
# 1. 시작점 기준으로 오름차순 정렬
# 2. 첫 구간의 끝점을 기준으로.
# 3. 다음 구간의 시작점이 전 끝점보다 크면 새로운 냉장고가 필요하다.
# 4.

'''
n = int(input())
food = []        # 식품
for i in range(n):
    start, end = map(int, input().split())
    food.append((start, end))

food.sort()     # start 기준으로 오름차순 정렬
cnt = 1
first_end = food[0][1]      # 첫 구간의 끝점
for start, end in food:
    if start > first_end:       # 그 다음 구간의 시작점이 첫 구간의 끝점보다 크다면
        cnt += 1
        first_end = end     # 갱신

print(cnt)
'''



