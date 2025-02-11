# [DAT 자료구조] 23396.
# List1 교재에 코드 나와있음
# 강사님 코드
# scores = list(map(int, input().split()))
#
# def counting_sort(arr):
#     dat = [0] * 101
#
#     for score in arr:
#         dat[score] += 1
#
#     result = []
#
#     for i in range(101):
#         if dat[i] == 0:continue
#         for j in range(dat[i]):     # 점수 등장 횟수만큼 반복
#             result.append(i)        # 0이 아닌 i만 추가   # 0부터 append되니 오름차순으로 정렬됨
#
#
#     return result
#
# ret = counting_sort(scores)
# print(*ret)

# ---
# [DAT 자료구조] 23398.
# IM 난이도
# T = int(input())
#
# for tc in range(1, T+1):        # 출력값 보면 tc 번호 1부터 시작
#     N = int(input())        # 버스 노선의 수
#     # dat 배열(버스 정류장은 5000번)
#     dat = [0] * 5001
#     for i in range(N):
#         A, B = map(int, input().split())
#         # dat 배열에 카운팅
#         for j in range(A, B+1):
#             dat[j] += 1
#
#     P = int(input())        # 확인할 정류장 수
#     result = []
#     for i in range(P):
#         C = int(input())
#         result.append(dat[C])       # 카운팅된 수가 result 배열에 추가
#
#     print(f'#{tc}', end = ' ')
#     print(*result)



# ---
# Parsing 문제는 쓸 수 있는 메서드 다 써야 함. 특히 find.

# 23421.
# 내 코드 1
# text = input()
#
# def is_palindrome(n):
#     if n == n[::-1]:
#         print(1)
#     else:
#         print(0)
#
# is_palindrome(text)

# 강사님 코드
# def is_palindrome(n):
#     if n == n[::-1]:
#         return 1
#     return 0        # else(x)
#
# text = input()
# print(is_palindrome(text))

# ---
# 23427.
# 내 코드
# text = 'BBQBHCKFCMC'
#
# print(text.find('KFC'))

# ---
# 23428.
# 내 코드
# text = 'helloworld[92084]answer'
#
# start = text.find('[') + 1
# end = text.find(']')
#
# num = text[start:end]
#
# print(num)

# ---
# 이 문제는 왜 함수 만드는 게 나을까?
# ㄴ iterator 방식으로 순회할 것이기 때문

# 23430.
# arr = [
#     'ABCQ',
#     'B[4]R',
#     'CCDA',
#     'BT[15]'
# ]
#
# def get_find(text):
#     for string in text:
#         if string.isalpha():
#             continue
#         start = string.find('[') + 1
#         end = string.find(']')
#         num = string[start:end]
#         print(num, end = ' ')
#
# get_find(arr)

# def get_find(text):
#     for string in text:
#         if string.isalpha():
#             continue
#         start = string.find('[') + 1
#         end = string.find(']')
#         num = string[start:end]
#         return num
#
# ret = get_find(arr)
# print(*ret)

# 강사님 코드
# arr = ['ABCQ', 'B[4]R', 'CCDA', 'BT[15]']
#
# def get_find(text):
#     if text.find('[') == -1: return ""
#     start = text.find('[') + 1
#     end = text.find(']')
#     return text[start:end]
#
#
# for text in arr:
#     ret = get_find(text)
#     # 빈 문자열이나 0이면 False, 아니면 True   # 0.0도 False
#     if ret: print(ret, end = ' ')

# ---

# 23431.
# 내 코드
# text = 'B[45]AB[9994]'
#
# sum_v = 0
#
# for i in range(2):
#     start = text.find('[', i)
#     end = text.find(']', i)
#     num = text[start:end]
#     sum_v += num
#
# print(sum_v)

#
# text = 'B[45]AB[9994]'
#
# sum_v = 0
# start = 0
#
# for i in range(2):
#     start = text.find('[', start) + 1
#     end = text.find(']', start)
#     num = int(text[start:end])
#     sum_v += num
#
# print(sum_v)

# 강사님 코드
# text = 'B[45]AB[9994]'
#
# start1 = text.find('[')
# end1 = text.find(']', start1 + 1)
# start2 = text.find('[', end1 + 1)
# end2 = text.find(']', start2 + 1)
#
# t1 = text[start1+1:end1]
# t2 = text[start2+1:end2]
#
# print(int(t1) + int(t2))

# ---
# 23432.
# 내 코드
# text = 'ABCDEFABCKKKKKABC'
#
# cnt = 0
#
# while cnt <= 3:
#     cnt = text.find('ABC', cnt) + 1
#     print(cnt)

#
# text = 'ABCDEFABCKKKKKABC'
# object = 'ABC'
#
# cnt = 0
# index = text.find(object)
#
# while index != -1:      # index가 -1이 아니면 == text에 object가 있으면
#     cnt += 1
#     index = text.find(object, index + 1)
#
# print(cnt)

# 강사님 코드
# text = 'ABCDEFABCKKKKKABC'
#
# a = 0
# b = 0
# cnt = 0
#
# while True:     # 'while True'는 break 쓰지 않으면 무한루프
#     b = text.find('ABC', a)
#     if b == -1: break
#     cnt += 1
#     a = b + 1
#
# print(cnt)

# ---
# *** while문 주의사항
# ㄴ 무한루프(cf. break)

# 23433.
# text = [
#     'GOLDABCGOLD',
#     'HELLOWORLD',
#     'WHITEGOLD'
# ]
# object = 'GOLD'
#
# cnt = 0
#
# for string in text:
#     index = string.find(object)
#     while index != -1:
#         cnt += 1
#         index = string.find(object, index + 1)
#
# print(cnt)
#
# # 강사님 코드
# text = ['GOLDABCGOLD', 'HELLOWORLD', 'WHITEGOLD']
#
# def get_count(word):
#     cnt = 0
#     a = 0
#     while True:
#         b = text.find(word, a)
#         if b == -1: break
#         cnt += 1
#         a = b + 1
#     return cnt
#
# ret = 0
# for text in text:
#     ret += get_count('GOLD')
# print(ret)

# ---
# 회문 판별 함수 만들기 -> 행순회, 열순회
# 19774.
# 내 코드
# T = int(input())
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]


# a = 0
# b = 0
# while True:
#     b = arr.find(object, a)
#     a = b + M/2

#
# for tc in range(1, T+1):
#     def is_palindrome(c):
#         return c == c[::-1]
#
#     def find_palindrome(N, M, arr):
#         for i in range(N):
#             for j in range(N - M + 1):
#                 c = arr[i][j:j + M]
#                 if is_palindrome(c):
#                     return "".join(c)
#
#         for j in range(N):
#             for i in range(N - M + 1):
#                 c = [arr[x][j] for x in range(i, i + M)]
#                 if is_palindrome(c):
#                     return "".join(c)
#
#         return "Not Found"
#
# ret =
#
# print(f'#{tc} {})  # ABA 같은 회문이 나오도록

# ---
# 과목, 월말 기출
# find 메서드 활용
# 19783.

# text = 'ABC123[10]B{3}AT[20][10]BB{2}Q'

def get_nums(a, b):
    temp = text[a+1:b]
    return int(temp)

text = input()
n = len(text)
a, b = 0, 0
result = 0

# while문 구성요소 - 초기식, 증감식, 조건식
i = 0   # 초기식
while i < n:    # 조건식
    if text[i] == '[':
        a = i
        b = text.find(']', a + 1)
        result += get_nums(a, b)
        i += (b-a)
    elif text[i] == '{':
        a = i
        b = text.find('}', a + 1)
        result += get_nums(a, b)
        i += (b-a)

    i += 1  # 증감식

print(result)