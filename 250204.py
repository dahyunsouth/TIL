# [ 온라인 ]

# [ 08. OOP2 ]

# 1. 상속

    # 

        # - super() 사용 예시 (다중 상속)   # *** 무조건 다시보기   # * 10-06 line 63


# 2. 에러와 예외

    # else & finally

        # - else & finally
            # 필수 x

        # - 내장 예외의 상속 계층구조 주의 (1/2)
            # except BaseException - BaseException: 1대 예외 -> BaseException은 모든 예외 포함
            #

# ==============================
# ==============================

# [ 오프라인 ]

# [ 공부할 것 ]
    # global / local
    # arr
    # sort / sorted
    # request / requests

# [ 과목평가 ]
    # pdf 꼼꼼히 보세요
    # 첫 평가는 어렵게 나오기 때문에 변별 위해 다소 지엽적

# [ 월말평가 ]
    # 모든 문제를 함수, return
    # 파이썬 내장 함수(min, max, sum, len, sort 이런 거) 만들 수 있어야
    # ㄴ * for문을 얼마나 잘 다루느냐


# [ 클래스 심화 ]

# [ 상속 ]

    # [도전] 상속 구현하기
        # 타이어 구현하기
            # 부모 타이어 메서드
                # run ("런" 출력)
            # 자식 타이어 1 메서드
                # ran ("랜" 출력) - 메서드 추가가
            # 자식 타이어 2 메서드
                # run ("런런" 출력) - 오버라이딩
                # ron("론" 출력) - 메서드 추가

        # 내 코드
class Tire:

    class P_Tire:
        def run(self):
            print("런런")

    class S1_Tire:
        def ran(self):
            print("랜")

    class S2_Tire(P_Tire):
        def run(self):
            print("런런")

        def ron(self):
            print("론")

        # 강사님 코드
class Tire:
    def run(self):
        print('런 출력')

class ChildTire1(Tire):
    def ran(self):
        print('랜 출력')

class ChildTire2(Tire):
    def run(self):
        print('런런 출력')

    def ron(self):
        print('론 출력')

        # 아래는 내가 임의로
tire = Tire()
tire.run()


    # MRO: 메서드 해석 순서
    # 핵심 - 다중 상속에서는 왼쪽에서 오른쪽으로 우선순위가 적용
# class D(B, C):  # 에서 B가 왼쪽, B 클래스의 속성이 우선적으로 상속

class Child(ParentA, ParentB):
MRO에 따르면 왼쪽에서 오른쪽으로 진행, ParentA가 우선순위 더 높음

    # super() 우선순위 묻는 문제 나올 수 있음
    # Tip. 다이아몬드 구조 그림 그리기


# [ 에러와 예외 ]
    # 외울 필요 x

# try - except
def get_v (arr, idx):
    try:
        return arr[idx]
    except IndexError:
        return -1   # 인덱스 범위 벗어난 경우
    
arr = [1, 2, 3]
result = get_v(arr, 5)
print(result)

# if - else
def get_v(arr, idx):
    if 0 <= idx <= len(arr) - 1:
        return arr[idx]
    return -1

arr = [1, 2, 3]
result = get_v(arr, 5)
print(result)


# [ 참고 ]
    # *** EAFP, LBYL, lambda 스펠링(주관식 내기 좋음)