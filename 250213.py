# [Stack]
# 스택 자료구조에서 사용하는 메서드 2개는? append, pop
# append, pop 쓰면 무조건 스택이다? XXXX

# pop 소괄호 안에는 아무 것도 없어야.

# 교재 연습문제 1
# push 함수, pop 함수
'''
def push(stack, item):      # stack에 추가한다 -> stack을 매개변수로 써야 함-
    stack.append(item)      # append는 반환값 없는 메서드, 반환하는 메서드 x -> return 불필요

def pop_stack(stack):
    if stack:       # = stack이 비어있지 않으면
        return stack.pop()      # pop()을 하면 반환값이 있다.
    return None     # stack이 비어있으면 None 반환

stack = []
push(stack, 1)
push(stack, 2)
push(stack, 3)
print(stack)

a = pop_stack(stack)
b = pop_stack(stack)
c = pop_stack(stack)
print(stack)    # 비어있다.
print(a)    # 3 # 후입선출
print(b)    # 2
print(c)    # 1
'''

# ---
# 교재 - 연습문제 2

# 1. 열린 괄호가 나왔다 -> 스택에 추가, append
# 2. 닫힌 괄호가 나왔다 -> 스택에서 제거, pop
# -> stack이 비어있으면 -> 올바른 괄호 사용!
'''
def push(s):
    stack = []

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            # stack이 비어있으면 제거 안 됨 -> error 남
            if not stack:   # stack이 비어있으면
                return False
            stack.pop()     # stack에서 제거

    return len(stack) == 0      # stack이 비어있어야 True

arr = [
    '()())((()))',
    '((()((((()()((()())((()))))'
]

for text in arr

    if not stack:
        print('올바른 괄호 사용!')
    else:
        print('잘못된 괄호 사용!')

text = '()())((()))'
push(text)
'''

# 19975.
# s에서 반복된 문자 지우기
# 반복문자 지운 후 남은 문자열의 길이 출력
# 남은 문자열 없으면 0 출력

# arr = []
# arr.append(1)
# arr.append(2)
# arr.append(3)
#
# arr.pop()
# arr.pop()
# arr.pop()
#
# print(arr)

'''
def push(stack, char):
    stack.append(char)


def pop(stack):
    if stack:
        stack.pop()
'''

# 예시
# ABCCB

# 스택이 비어있지 않고 / 현재 문자가 스택의 맨뒤 문자와 같다면
# pop
# stack[-1] == 마지막 문자
# stack.pop()





'''T = int(input())

for tc in range(1, T + 1):
    s = input()
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    len_stack = len(stack)
    print(f'#{tc} {len_stack}')'''
# len(stack)  # 남은 문자열 길이 반환

'''
# 입력 처리
T = int(input())  # 테스트 케이스 개수 입력

for tc in range(1, T + 1):
    s = input()
    length = len(stack)
    print(f"#{tc} {length}")
'''

# ---
# LED

# T = int(input())
#
# for tc in range(1, T+1):


# 18733. 그리디 boss - 액체괴물
# <전략>
'''
1. 가장 작은 두수를 더한다
2. 더한 값을 배열에 넣고 정렬
3. 한 개의 수가 남을 때까지 반복(while문)
'''
'''
N = int(input())
weight = list(map(int, input().split()))
weight.sort(reverse=True)
arr = []

for i in range(N):
    if i+1 <= N:
        sum_v = weight[i] + weight[i+1]
        arr.append(sum_v)
        weight.pop()
        weight.pop()
        print(weight)
'''
#
'''
N = int(input())
weight = list(map(int, input().split()))
weight.sort(reverse=True)

sum_v = 0

while len(weight) == 1:
    # for _ in range(N):  # while이 반복문 ㅇㅇ
    arr = []
    sum_v = weight[-1] + weight[-2]
    arr.append(sum_v)
    weight.pop()
    weight.pop()
    if len(arr) == 0:
        break
print(sum_v)
'''
# 강사님 코드
'''
N = int(input())
arr = list(map(int, input().split()))

# 내림차순 정렬
arr.sort(reverse=True)

sum_v = 0
while len(arr) > 0:     # pop으로 빼다가 길이가 0이 되면 반복문 종료
    # 가장 작은 두 수를 더한다(pop으로 빼서)
    temp = arr.pop() + arr.pop()
    sum_v += temp       # 누적합
    # pop으로 뺐는데 비어있는 리스트다? -> break
    if len(arr) == 0:
        break
    arr.append(temp)    # 더한 값을 배열 arr에 다시 추가
    arr.sort(reverse=True)

print(sum_v)
'''

# 19975. 반복문자 지우기(low)







# 19837. 괄호검사(mid)
'''
<전략>
1. 처음에 여는 괄호가 나온다? ---> 무조건 stack에 append
2. 닫는 괄호가 나오면 ---> stack의 맨뒤 element와 짝이 맞는지 확인
    1) 짝이 맞으면 ---> pop으로 제거
    2) 짝이 안 맞으면 ---> stack에 추가
3. 이걸 반복하다가
4. 스택이 비어있으면 모든 괄호의 짝이 맞는 것

<예시>
print('{} {}'.format(1, 2))
stack = []

'(' 발견 ---> stack = ['(']
'{' 발견 ---> stack = ['(', '{']
'}' 발견 ---> stack의 마지막 요소와 짝이 맞는지 비교 ---> '{'와 짝이 맞음 ---> pop()
stack = ['(']

'{' 발견 ---> stack = ['(', '{']
'}' 발견 ---> '{'와 짝이 맞음 ---> pop()
stack = ['(']
마지막에 ')' 발견 ---> '('와 짝이 맞음 ---> pop()
stack = []      # 1 출력(올바른 괄호 사용 ㅇㅇ)

'''
# 강사님 코드









'''def is_brackets(text):
    stack = []

    for char in text: # 괄호 하나하나
        if char == '(': # 열린 괄호다 --> 스택에 추가
            stack.append(char)
        elif char == ')': # 닫힌 괄호다 ---> 스택에서 제거
            if not stack: # 스택이 비어있으면 pop()을 못쓴다
                return False
            stack.pop() # 스택에서 제거

    return len(stack) == 0 # 스택이 비어있어야 ---> True

arr = [
    '()()((()))',
    '((()(((()()((()())))'
]

for text in arr:
    if is_brackets(text):
        print(f'{text}는 올바른 괄호식 입니다')
    else:
        print(f'{text}는 올바르지 않은 괄호식 입니다.')'''



T = int(input())
'''
for tc in range(1, T+1):
    N = int(input())
    default = list(map(int, input().split()))
    pattern = list(map(int, input().split()))

    cnt = 0     # 스위치를 누르는 횟수

    for i in range(N):      # N번, 그러니까 요 리스트의 길이만큼 탐색을 할 거예요
        if default[i] != pattern[i]:        # 그림을 준비했는데 # 초기 배열의 인덱스 i번째 전등의 상태와 최종 배열의 인덱스 i번째 전등의 상태가 다르다면
            cnt += 1
            for j in range(i, N):
                default[j] = 1 - default[j]

                print(f'#{tc} {cnt}')       # f스트링 사용해서 출력하겠습니다.

'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0

    for i in range(N):
        if A[i] != B[i]:
            cnt += 1
            for j in range(i, N):
                A[j] = 1 - A[j]

    print(f'#{tc} {cnt}')

    # for문을 하나 더 만들 건데, 왜 때문이냐면, 문제를 보면 # 스위치를 조작하면 그 전등부터 맨 끝에 있는 전등까지 상태가 바뀐대잖아요 # 그림으로 나타내보자면
    # i번째부터 N번째 전등까지 1과 0을 오가야 되잖아요 # 그걸 이 식으로 정의를 한 거구요
    # 끝났습니다











