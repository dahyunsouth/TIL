# 2. 어려웠던 부분
#     라이브 강의자료 pull하려고 했는데 error 발생

#     SSAFY@DESKTOP-3HB59PA MINGW64 ~/Desktop/online_private (master|MERGING)
#     $ git pull origin master
#     error: You have not concluded your merge (MERGE_HEAD exists).
#     hint: Please, commit your changes before merging.
#     fatal: Exiting because of unfinished merge.

#     지피티 曰 이전에 병합(merge) 작업이 완료되지 않은 상태에서 새로운 병합을 시도해서서 발생하는 문제
#     1. 현재 병합 상태 확인
#         git status

#         $ git status
#         On branch master
#         Your branch and 'origin/master' have diverged,
#         and have 2 and 1 different commits each, respectively.
#         (use "git pull" if you want to integrate the remote branch with yours)

#         All conflicts fixed but you are still merging.
#         (use "git commit" to conclude merge)

#         Changes to be committed:
#                 new file:   08-data-structure/01-method.py
#                 new file:   08-data-structure/02-string.py
#                 new file:   08-data-structure/03-list.py
#                 new file:   08-data-structure/04-dict.py
#                 new file:   08-data-structure/05-set.py
#                 new file:   08-data-structure/99-copy.py
#                 new file:   08-data-structure/99-hash-table-example.ipynb
#                 new file:   08-data-structure/99-hash-table.py
#                 new file:   08-data-structure/99-method-chaining.py

#         Changes not staged for commit:
#         (use "git add <file>..." to update what will be committed)
#         (use "git restore <file>..." to discard changes in working directory)
#                 modified:   06-modules/01-basic.py
#                 modified:   08-data-structure/01-method.py
#                 modified:   08-data-structure/02-string.py
#                 modified:   08-data-structure/03-list.py
#                 modified:   08-data-structure/99-copy.py
#                 modified:   08-data-structure/99-method-chaining.py

#     대충 수정사항이 있는데 commit이 안 됐다는 뜻인 것 같아서
#     add, commit함

#     pull 성공


# ==============================
# ==============================

# [ 온라인 ]

# [ 07. OOP1]

# 1. 프로그래밍과 패러다임

# # 절차 지향과 객체 지향

#     - 객체 지향 프로그래밍, OOP
#         절차 지향 프로그래밍을 보완하기 위해 등장

#     - 객체 지향 사고 예시
#         list.append()
#         dict.items()
#         alice.introduce()

#     - 절차 지향 & 객체 지향
#         절차 지향과 객체 지향은 대조(VS) 관계 x

#     - 객체 지향 - "데이터가 살아나다"
#         절차 지향에서 데이터는 수동적 존재, 재료, 수단

#         introduce(name, age)    # 절차 지향 # '누가'가 빠져있음
#         alice.introduce()       # 객체 지향 # 누가.행동한다     # 'alice가 소개한다' 인간의 어순과 비슷(가독성? 좋음음)

#     - 절차 지향과 객체 지향은 대조되는 개념이 아니다.
#         객체 지향은 기존 "절차 지향을 기반"으로 두고
#         보완하기 위해 객체라는 개념 도입


# # 객체와 클래스

#     - 객체 (Object)
#         속성- 변수 / 동작 - 메서드

#     - 클래스 (Class)
#         a = 'abc'
#         print(type(a))  # <class 'str'> # 강의 다시보기

#     - 객체와 클래스
#         아이유, BTS 각각에 대한 함수 만들 필요 없이
#         가수에 대한 함수 만들어놓고 찍어내면 됨

# ==============================

# 2. 클래스 기초

# # 클래스

#     - 클래스 정의
#         - 클래스 이름은 Pascal Case(대문자) 방식으로 작성
#         cf. 변수, 함수 이름은 Snake_case 방식(단어와 단어를 언더바로 구분)으로 작성

#     - 클래스 예시
#         - __init__ 메서드 - 초기화
#         cf 1. 매직 메서드 - 앞뒤로 언더바 2개 붙은 메서드
#         cf 2. 개발자가 호출 시점 결정 x, '새로운 객체를 만들 때' 자동 호출됨

#     - 인스턴스
#         클래스를 통해 만들어진 객체

#     - 클래스와 인스턴스
#         '누구의' 인스턴스인지
#         cf. line 37, 38
#             아이유는 인스턴스다(△)

#         'Alice'는 str class의 인스턴스

#     - 인스턴스와 메서드
#         "hello".upper()
#         "hello"는 str의 인스턴스
#         upper는 str class 안에 들어가있음
#         cf) list.append()
#             append는 list class 안에 들어가있기 때문에
#             모든 list class의 instance가 append 쓸 수 있는 것

        
# # 클래스 구성요소

#     - 클래수 구조 (1/3)
#         - 생성자 메서드
#             __init__ - c1 호출할 때(c1 = Circle(1)) 자동 호출

#     - 클래스 구조 (2/3)
#         - 인스턴스 변수(속성) # 강의 다시보기

#     - 클래스 구조 (3/3) # 강의 다시보기

# ==============================

# 3. 메서드

# # 메서드란

#     - 메서드 종류   # 강의 다시보기


# # 인스턴스 메서드

#     - 인스턴스 메서드
#         인스턴스가 호출하는 메서드
#         목적 - 클래스 호출 x, 인스턴스 호출 or 인스턴스가 어떤 동작을 수행하도록?

#     - 인스턴스 메서드 구조
#         - 반드시 첫 번째 인자로 인스턴스 자신(self)을 받음
#             * self는 매개변수의 이름일 뿐이며 다른 이름으로 설정 가능, 하지만 다른 이름을 사용하지 않을 것을 강력히 권장

#     - self 동작 원리 (1/2)
#         * 인스턴스 메서드의 첫 번째 인자가 반드시 자기 자신인 이유

#     - self 동작 원리 (2/2)
#         - 'hello'.upper()은 str.upper('hello')를 객체 지향 방식의 메서드로 호출하는 표현 (단축형 호출)

#     - 생성자 메서드
#         도 큰 틀에서는 인스턴스 메서드? # 강의 다시보기


# # 클레스 메서드

#     - 클래스 메서드
#         인스턴스 메서드와 분리

#     - 클래스 메서드 구조
#         데코레이터는 아래 함수 꾸며주는 역할
#         - 클래스 메서드의 첫 번째 인자는 '클래스 자기 자신'
#             * cls는 매개변수의 이름일 뿐이며 다른 이름으로 설정 가능, 하지만 다른 이름을 사용하지 않을 것을 강력히 권장


# # 스태틱 메서드 aka 정적 메서드

#     - 스태틱(정적) 메서드
#         클래스, 인스턴스와 상관 없이 독립적으로 동작하는 메서드
#         클래스, 인스턴스 조작과 무관

#     - 스태틱 메서드 구조
#         - @staticmethod 데코레이터를 사용하여 정의
#         - 호출 시 자동으로 전달받는 인자(self, cls 등) 없음     # 일반 함수라고 생각하면 됨 # 그러나 엄연히 메서드이기 때문에 클래스가 호출
#         - 인스턴스나 클래스 속성에 직접 접근하지 않는, '도우미 함수'와 비슷한 역할


# # 메서드 활용

#     - 입출금이 가능한 은행 계좌 클래스 만들기


# # 메서드 정리

#     - 메서드 정리
#         - 인스턴스 메서드

#         - 클래스 메서드

#         - 스태틱 메서드

#     - 누가 어떤 메서드를 사용해야 할까 (1/2)
#         - 클래스가 사용해야 할 것

#         - 인스턴스가 사용해야 할 것것

#     - 누가 어떤 메서드를 사용해야 할까 (2/2)
#         인스턴스도 클래스 메서드, 스태틱 메서드 호출 가능하고
#         클래스도 인스턴스 메서드, 스태틱 메서드 호출 가능함

#     - 클래스, 인스턴스가 할 수 있는 것
#         - 클래스, 인스턴스는 모든 메서드를 호출할 수 있음
#         * 하지만 클래스는 클래스 메서드와 스태틱 메서드만 사용하도록 한다.
#         * 하지만 인스턴스는 인스턴스 메서드만 사용하도록 한다.

#     - 할 수 있다 != 써도 된다

# ==============================

# 4. 참고

# # 클래스와 인스턴스 간 이름 공간
#     * p. 87

# # 매직 메서드

#     - __str__ 예시
#         # 강의 다시보기

# # 데코레이터

#     - 데코레이터
#         # 강의 다시보기
#         원본은 유지한채로 추가 기능 넣거나 확장하기 위해 사용
#         * 데코레이터도 사실 함수

# ==============================
# ==============================

# [ 오프라인 ]

# [ 05. Data structure]

# 5. 비시퀀스 데이터 구조

# 딕셔너리

    # - 딕셔너리 메서드 *** 외워야 돼

        # get
# person = {
#     'name': 'sangho',
#     'age': 20,
#     'interest': {'hobby': 'computer', 'invest': 'bitcoin'}
# }
# computer 출력
# print(person['interest']['hobby'])
# request.get, 딕셔너리의 get 메서드는 다르다
# print(person.get('interest').get('hobby'))
# print(person.get('height', 185))   # key가 없을 경우 딕셔너리에 추가 x
# print(person)

        # get 메서드와 setdefault 메서드 유사
        # get 메서드와 setdefault 메서드 차이 *** 과목평가
            # key가 없을 경우 딕셔너리에 추가하는지, 안 하는지의 차이

# print(person.setdefault('height', 185))   # key가 없을 경우 딕셔너리에 추가 o
# print(person)

        # * 알고리즘 과정에서 가장 많이 쓰일 딕셔너리 메서드는 keys, values, items
        # ㄴ for문과 함께 많이 쓰임

# print(person.keys())

# for key in person.keys():
#     print(key)

        # 리스트의 pop 메서드와 딕셔너리 pop 메서드의 차이
        # ㄴ 리스트는 인덱스 기준, 딕셔너리는 key 기준
        # 해시테이블 개념
# print(person.pop('age'))
# print(person)

        # update - 굳이 쓸 필요 없고
# person['height'] = 185    # 이렇게 하면 됨됨

# other_person = {'height': 185}
# person.update(other_person)
# print(person)


# 세트

    # - 세트 메서드

        # ***
        # 리스트 element 추가 메서드: append
        # 세트 element 추가 메서드: add

        # pop과 discard의 차이
        # ㄴ 임의의 항목 제거하고 반환환: pop / 특정 항목 제거하고 반환: discard

        # '임의의 항목'과 'random(무작위)' 같은 말일까?
        # ㄴ 다른 말.
        # ㄴ 임의의 항목 -> 해시테이블의 순서. pop은 해시테이블 순서에 따라 제거

    # - 세트의 집합 메서드
        # 그냥 연산자 쓰면 되기 때문에 잘 안 씀
        # 그러나 과목평가 봐야 되니 외우세요

# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
# print(set1 - set2)  # 훨씬 직관적
# print(set1.difference(set2))

# ==============================

# 6. 해시 테이블

    # # 해시 테이블
        # - 해시 함수를 사용하여 변환한 값을 '인덱스'로 삼아아

    # sequence 타임(list, tuple, string)에는 '인덱스'가 존재
    # set와 dictionary에는 '해시테이블'이 존재
    # 둘의 차이를 비교했을 때 해시테이블 개념을 왜 알야둬야 할까?
    # ㄴ pop 등 for문 등에 쓰면 해시테이블 순서에 따라 진행되기 때문
    # 특징 2가지
    # 1. set와 dictionary는 리스트에 비해 성능이 매우 빠르다(검색, 삽입, 삭제)
        # 예) set와 dictionary: O(1)    # 오더(1): 시간복잡도 1(매우 빠른 것) = y=1
        # 예) list: O(n)                # 오더(n): = y=n = y=x: n이 커질수록 시간복잡도 커짐 = 느려짐
        # 리스트에서 검색: 특정값을 찾기 위해서 전체 element를 순회. 그래서 O(n)
        # 리스트에서 삽입: 중간에 삽입 -> 뒤로 한 칸씩 밀려난다. 그래서 O(n)
# lst = [1, 2, 3, 4, 5]
# print(lst[3]) # 3 한 번에 찾아내는 게 아니라, 앞에서부터 순회
# lst.insert(3, 6)    # *** insert 외워야 돼
# -> 기존 인덱스 3 이후로는 한 칸씩 밀려남
    # 2. set와 dictionary는 중복을 허용하지 않는다.


    # 해시테이블의 해시 값은 '정수'일 때와 '문자'일 때 다름
        # 1. 정수의 해시 값은 일정(아무리 실행해도 같은 값)     # * 정수가 작을수록 해시값도 작을까? No
        # 2. 문자의 해시 값은 난수화(실행할 때마다 달라짐)

# ==============================

# 클래스
    # Class는 변수와 함수를 하나로 묶은 덩어리이다.
        # *** 생성자, 필드, 메서드 암기하세요!
        # class 안에서 __init__ 함수를 '생성자' 라고 함, 이곳에서 클래스 안에서 사용할 변수를 만든다.
        # 그 안에서 초기화된 변수, 클래스 안에서 사용할 변수: '필드'
        # '메서드': 클래스 안에서 만든 함수

# class SetMenu:  # 클래스 정의
#     def __init__(self): # 생성자
#         self.sanghai = 4500 # 필드
#         self.bigmac = 4200

#     def eat(self):  # 메서드
#         print('햄버거 주문하기')
#         print(f'{self.sanghai + self.bigmac}원 입니다')

# mc = SetMenu()
# mc.eat()

    # [도전] 저글링 클래스 만들기
        # 필드(생성자에서 구현)
            # - hp = 20
            # - mana = 50
        # run() 메서드
            # - "뛴다" 라는 Text 출력
            # - hp가 1 줄어든다.
            # - mana가 1 올라간다.
        # show_status() 메서드
            # - hp와 mana를 출력한다.

        # 내 풀이
# class Zergling :
#     def __init__(self):
#         self.hp = 20
#         self.mana = 50

#     def run(self):
#         print("뛴다")
#         self.hp -= 1
#         self.mana += 1

#     def show_status(self):
#         print(f'hp: {self.hp} mana: {self.mana}')

# mc = Zergling()
# mc.run()
# mc.show_status()

        # 강사님 풀이
# class Zergling :
#     def __init__(self):
#         self.hp = 20
#         self.mana = 50

# def run(self):
#         self.hp -= 1
#         self.mana += 1
#         print("뛴다")

# def show_status(self):
#     print(f'hp: {self.hp}')
#     print(f'mana: {self.mana}')


    # [도전] 앞에서 제작한 저글링 클래스 사용하는 코드 만들기
        # 저글링 두 마리를 만든다.
            # - 변수 z1, z2에 생성
        
        # 저글링을 각각 동작시킨다.
            # - z1은 run 이후 show_status 호출
            # - z2는 run 5회 이후 show_status 호출

        # 내 코드
# class Zergling :
#     def __init__(self):
#         self.hp = 20
#         self.mana = 50

# def run(self):
#         self.hp -= 1
#         self.mana += 1
#         print("뛴다")

# def show_status(self):
#     print(f'hp: {self.hp}')
#     print(f'mana: {self.mana}')

# z1 = Zergling()
# z1.run()
# z1.show_status()

# z2 = Zergling()
# # 미완

        # 강사님 코드
# class Zergling :
#     def __init__(self):
#         self.hp = 20
#         self.mana = 50

# def run(self):
#         self.hp -= 1
#         self.mana += 1
#         print("뛴다")

# def show_status(self):
#     print(f'hp: {self.hp}')
#     print(f'mana: {self.mana}')

# z1 = Zergling()
# z2 = Zergling()

# z1.run()
# z1.show_status()

# for i in range(5):
#     z2.run()
# z2.show_status()

    # 저글링 뽑기 - 발업 - 저글링 뽑기
    # ㄴ 발업하기 전에 뽑은 저글링들도 발업됨
    # ㄴ 이게 '클래스'


    # 객체와 변수의 차이 ***
        # - 파이썬에서는 수, 문자열, 리스트, 클래스의 인스턴스들을 '객체'라고 한다.
            # - 즉, 파이썬에서는 모든 데이터를 객체로 취급한다.

        # - 모든 객체는 변수에 할당한 후에, 그 변수를 이용하여 객체를 제어한다.
            # - 변수는 객체의 이름표이다.

        # [도전] 개수 맞추기
            # - 아래 코드에서 등장하는 변수의 개수는?   # 3     # a, b, c
            # - 아래 코드에서 등장하는 객체의 개수는?   # 5     # 3(정수), [1, 4, 2, 5, 4](리스트), SetMenu()(인스턴스), 15(정수), 2(정수)
            # - 할당 횟수는?    # 5     # 'b[3] = 2'는 할당 x

# a = 3 # 3은 객체, a는 변수, 할당
# b = [1, 4, 2, 5, 4] # []는 객체, b는 변수, 할당
# c = SetMenu() # 변수가 2개인 거고, 객체는 하나  # SetMenu()는 객체, c는 변수, 재할당
# a = 15  # 재할당    # 15는 객체, a는 변수, 재할당
# b[3] = 2    # 할당 아님 # -> 객체 x     # b[3]은 인덱싱 element(요소), 할당 x, 2는 객체 x->o   # 'b = [1, 4, 2, 5, 4]'에서 리스트(대괄호)가 할당되는 거지, 리스트의 element 아무리 바꿔도 (재)할당 x
    # 2 객체 맞음. 그러나 '할당' 관점에서 보면 객체 x   # 그냥 SSAFY 수준에서는 2 객체라고 생각하셈 cf. line 477
# a = SetMenu() # 변수가 2개인 거고, 객체는 하나      # SetMenu()는 객체, a는 변수, 재할당


    # [도전] GameMachine Class 제작
        # input_coin(집어넣을 코인 수)
            # - 코인은 최대 5개까지 넣을 수 있음
            # - 입력된 코인이 10보다 초과될 수 없음

        # play_game()
            # - 1코인씩 감소됨

        # 집어넣은 코인이 얼마나 되는지 확인할 수 있어야 함
            # - 메서드 추가 생성 필요

# gm = GameMachine()
# gm.input_coin(2)
# gm.show_status()
# gm.play_game()
# gm.show_status()

# # 출력 결과
# 남아있는 코인은 2 입니다
# 게임 재밌다
# 남아있는 코인은 1 입니다


        # 내 코드
# class GameMachine:
#     def __init__(self):
#         self.input_coin <= 5

#     def play_game(self):
#         self.input_coin -= 1
#         print('게임 재밌다다')
    
#     def show_status(self):
#         print(f'남아있는 코인은 {self.input_coin} 입니다')

# gm = GameMachine()
# gm.input_coin(2)
# gm.show_status()
# gm.play_game()
# gm.show_status()

# # 출력 결과
# 남아있는 코인은 2 입니다
# 게임 재밌다
# 남아있는 코인은 1 입니다


        # 강사님 코드
class GameMachine:
    def __init__(self):
        self.coins = 0  # 코인 초기화

    def input_coin(self, amount):
        if amount > 5:
            return
        if self.coins + amount > 10:
            return
        self.coins += amount

    def play_game(self):
        if self.coins < 1:
            print('코인을 넣어주세요!')
            return
        self.coins -= 1
        print('게임 재밌다')
    
    def show_status(self):
        print(f'남아있는 코인은 {self.coins} 입니다')

gm = GameMachine()
gm.input_coin(2)
gm.show_status()
gm.play_game()
gm.show_status()

# 출력 결과
# 남아있는 코인은 2 입니다
# 게임 재밌다
# 남아있는 코인은 1 입니다


    # [도전]
        # 시사점 - 다형성: 무엇을 넣느냐에 따라 달라진다?
class Duck:
    def quack(self):
        print("꽥꽥")

class Person:
    def quack(self):
        print("사람이 꽥꽥 소리를 냅니다!")

def 


    # 상속
        # - 기존 클래스의 필드와 메서드를 물려받으면서, 새로운 클래스를 만드는 것
        # - 사용하는 이유: 부모클래스보다 더 많은 필드와 메서드 추가할 수 있음
class Person:
    def walk(self):
        print("사람이 걷는다")

class SuperMan(Person):
    def fly(self):
        print("난다")

a = SuperMan()
a.fly() # 난다
a.walk()    # 사람이 걷는다

# walk는 오버라이딩된 메서드이다.   # 오버라이딩(= 재정의): 부모의 메서드를 자식이 변경할 수 있음

# ==============================

# 메서드

    # 클래스 변수와 인스턴스 변수의 차이
        # p. 67
        # ㄴ 클래스 변수 - Population / 인스턴스 변수 - name

class Student:
    # 클래스 변수
    total_students = 0
    # 생성자 함수
    def __init__(self, name, grade):
        # 왼쪽 name - 인스턴스 변수 / 오른쪽 name - parameter
        self.name = name
        self.grade = grade
        Student.total_students += 1

    @classmethod
    def get_total_student(cls):
        return cls.total_students
    
    # 중요한 순서
        # 1. 인스턴스 메서드
        # 2. 생성자 메서드
        # 3. 데코레이터

    # Ex)
    # @login_required   # 로그인된 상태에서만 게시글 생성할 수 있도록 하기 위해 사용하는 것이 데코레이터
    # 게시글 생성 함수
    def create():
        pass