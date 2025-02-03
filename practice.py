# print('hello')
# print(1, 2)
# print('a', 'b')

# print("남다현", end ='\n')
# print("24")

# print("남다현", end ='')
# print("24")

# print('남다현', 24)

# print('### ', end = '')
# print('###', end = '\n')
# print('#7# ', end = '')
# print('#3#', end = '\n')
# print('### ', end = '')
# print('###', end = '')

# print('###', end = ' ')
# print('###')
# print('#7#', end = ' ')
# print('#3#')
# print('###', end = ' ')
# print('###')

#\n: 줄바꿈
#\': 따옴표
# print('안녕 나는 \'컴미\'야')

# =: 할당 연산자자
# PI = 3.14 # 할당
# PI = '삼점일사' # 재할당

# 할당과 재할당의 차이
# a = 10
# b = 20
# a = 50
# c = 30
# print(a, b, c)

# [변수명 규칙]
# 1. 숫자로 시작 불가
# 2. _(underscore)로 시작 가능
# 3. 대시(-) 사용 불가
# 4. 파이썬 내부적으로 이미 사용 중인 키워드 사용 불가(if, True, for, sum 등), Ex. sum을 변수명으로 사용한다면 print는 됨, 그런데 그 다음부터 더하는 함수로는 사용 불가
# 5. 대소문자 구분(PI와 pi는 다름)

# Q. 다음 중 가능한 변수 개수
# abc421
# 3ba
# apython
# python-3
# f7
# 9b
# _d
# show_3
# A. 5개

# [변수를 출력하는 2가지 방법]
# a = 10
# print(a)
# 비추

# ㄴ 파이썬 권장 문법: f-string
# 가장 가독성, 성능(출력 속도) 좋음

# name = '남다현'
# age = 24
# area = 'Mapogu'

# print('저는', name, '이고') #비추
# print(f'저는 {name}이고, {age}세이고, {area}에서 살고 있습니다.')

# *** f-string으로 소수점 출력하기
# f'{variable: 소수점 자리수}'

# PI = 3.141592
# print(f'{PI:.2f}') # 소수 둘째 자리까지 반올림

# PI = int(PI) # 정수로 형변환
# Q. 올림? 반올림? 버림? | A. 버림

# 아래 소스코드를 'a와 b를 합치면 30.6이 됩니다.'가 출력되도록
# 내 코드
# a = 10.25
# b = 20.31
# sum = a + b
# sum_v = f'{sum:.1f}'
# print(f'a와 b를 합치면 {sum_v}이 됩니다.')

# 강사님 코드
# a = 10.25
# b = 20.31
# sum_v = a + b
# print(f'a와 b를 합치면 {sum_v}이 됩니다.')

# id: 메모리 주소를 알 수 있는 내장함수
# a = 10
# print(f'10은 {id(a)}번 방에 저장되어 있다.')

# a = 50
# print(f'50은 {id(a)}번 방에 저장되어 있다.')

# Q. type() 함수를 사용해서 데이터 타입 5개 이상을 출력해보자.
# 내 답안
# print(type(3.14))
# print(type('안녕'))
# print(type(3))

# 강사님 답안
# a = 3
# b = -2.3
# c = 3 + 3j # 복소수
# d = '3.123'
# e = True #Boolean #첫 글자 대문자여야
# f = None
# g = '' # *** None Type 아님

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(g))

# a = 10
# a = a + 4 # 지양
# a += 4 # 지향
# print(a) # 14

# d = 11
# d //= 2 # 지향
# print(d) # 5

# n = input() # 문자
# print(n)

# num = int(input())
# print(num)

# a, b = map(int, input().split())
# print(a, b)

# arr = list(map(int, input().split()))
# print(arr)

# 1 2 3 4 5를 입력 받아 출력해보자
# 1. 변수 1개 사용
# arr = list(map(int, input().split()))
# print(arr)
# 2. 변수 5개 사용
# a, b, c, d, e = map(int, input().split())
# print(a, b, c, d, e)

string = "hello"

string[start:end:step]

핵심: end를 항상 포함하지 않는다다
1. start > end
start부터 end-1까지 step만큼 증가
2. end > start
start  end+1까지 step만큼 감소

start가 생략되면 0부터
end가 생략되면 끝까지
step이 생략되면 step은 1