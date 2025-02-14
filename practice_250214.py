'''
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    pattern = list(map(int, input().split()))
    default = [0] * N
    cnt = 0

    for i in range(N):
        if default[i] != pattern[i]:
            cnt += 1
            if i > 1:
                for j in range(i, N, i):       # i가 0이라면?
                    default[j] = 1 - default[j]

    print(f'#{tc} {cnt}')
'''
'''
for i in range(1, 4):
    for j in range(1, 4):
        for a in range(1, 4):
            for b in range(1, 4):
                print(i, j, a, b)
'''
'''
def KFC(x):
    print(x)    # 8
    x += 1
    BTS(x + 5)
    print(x)    # 9

def BTS(x):
    print(x)    # 14

x = 3
KFC(x + 5)
print(x)    # 3
'''
# ---
'''
def KFC(x):
    KFC(x + 1)
    print('끝')

KFC(0)      # RecursionError: maximum recursion depth exceeded
'''
'''
def KFC(x):
    if x == 2:
        return
    print(x)
    KFC(x + 1)
    print(x)

KFC(0)
'''
'''
def KFC(x):
    if x == 6:
        return
    print(x, end = ' ')
    KFC(x + 1)
    print(x, end = ' ')

KFC(0)
'''

# 브랜치 2
# 레벨 3

'''
def KFC(x):
    if x == 3:
        return

    KFC(x+1)
    KFC(x+1)

    print(x)

KFC(0)

# 순열
중복 없이 순서를 고려하여 나열
# 중복순열
- 중복 허용

path = []

def KFC(x):
    if x == 2: # 2번 뽑는다.  # level = 2
        return

    for i in range(3): # 카드는 세 종류, branch = 3
        path.append(i)
        KFC(x+1)
        path.pop()

KFC(x)
'''

'''
num = [1, 2, 3, 4, 5, 6]
path = []

def KFC(x):
    if x == 3:
        print(path)
        return
    for i in range(1, 7):
        path.append(i)
        KFC(x+1)
        path.pop()

KFC(0)
'''

'''
n = int(input())

num = [1, 2, 3, 4, 5, 6]
path = []
used = [0] * 7

def KFC(x):
    if x == n:
        print(path)
        return

    for i in range(1, 7):
        if used[i] == 1: continue
        used[i] = 1
        path.append(i)
        KFC(x + 1)
        path.pop()
        used[i] = 0

KFC(0)
'''

# 23556.

n = int(input())


