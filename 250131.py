# *** 메서드는 '클래스' 안에 있는 함수라는 점이 내장함수와의 차이점점

# a = [1, 2, 3]
# a.append(4)
# result = max(a)
# print(a)
# print(result)

# 대문자, 소문자, 알파벳 여부부 확인
# 1. 메서드 isalpha
# 2. 유니코드(아스키코드) * 이거 더 많이 씀
# A의 유니(아스키)코드, a의 유니(아스키)코드는 암기하는 게 좋음

chr1 = 'A'
print(ord(chr1)) # 65

chr2 = 'a'
print(ord(chr2)) # 97

# 소문자가 대문자보다 32 더 큼
# 대문자 + 32 = 소문자
print(chr(ord(chr1) + 32)) # a

# 모든 문자, 심지어는 공백에도 유니코드 있음



a = 'hello'

print(a.find('b'))
# print(a.index('b'))

# try:
#     print(a.index('b'))
# except:
#     print('찾지 못했습니다.')

# index 사용하고 찾지 못했을 때 error 뜨지 않게 하는 법
# if else
if 'b' in a:
    print(a.index('b'))
else:
    print('찾지 못했습니다.')

    
arr = ['a', 'b', 'c']
# 문자열로 출력할 때 두 가지 방법
# 1. join 메서드
# 2. 언패킹 연산자

print(' '.join(arr))
print(*arr)

# split과 join은 서로 반대


# append와 extend의 차이
# append는 요소(항목)를 추가할 때
# extend는 iterable을 추가할 때
a = [1, 2, 3]
# 나는 4를 추가할 거야 -> append
# 나는 [4, 5, 6](이라는 리스트)을 추가할 거야 -> extend

# pop(): 마지막 요소를 제거하고 반환 # 단순 제거 x, 반환이 최종 o
# append()와 pop() 알고리즘에서 엄청 많이 씀
# stack: 후입선출
# pop(0) -> queue: 선입선출

# arr = [4, 1, 3, 2]
# arr.sort()
# print(arr)
# arr.sort(reverse=True)
# print(arr)

# sort와 sorted의 차이: 반환값 유무
# 원본을 유지하고 싶은 경우 -> sorted
# arr = [4, 1, 3, 2]
# arr2 = sorted(arr)
# print(arr2)

# 얕은복사: 복사본이 변경되면 원본도 변경
# 깊은복사: 복사본이 변경되어도 원본이 변경되지 않는다.

arr1 = [1, 2, 3, [4, 5, 6]]
arr2 = arr1[:]
arr3 = arr1.copy()
arr2[0] = 7
print(arr1)
print(arr2)
arr2[3][0] = 8
print(arr1)
print(arr2)