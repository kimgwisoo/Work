#함수란?
# 입력값을 가지고 어떤 일을 수행한 다음 그 결과물을 내 놓는 것.
# 함수를 사용하는 이유
#   반복되는 부분이 있을 경우 재활용을 위해
#   프로그램의 흐름을 일목요연하기 볼 수 있다.
#  -> Def으로 정희하고, 함수 선언부는 :로 끝남. 들여쓰기 규칙 적용


def dummy():
    pass # 실행할 내용이 없을때는 pass
def my_funcuton():
    print("hello World")

def times(a, b):
    return a * b # 결과값을 돌려줘야 할 때는 return 문으로 반환
def do_nothing():
    return # returm 문만 썻을 경우, None이 반환

dummy()
my_funcuton()
print(times(10, 10))
print(do_nothing())

t = times
print(t(100, 100))
print(t, times, sep = ",") # 객체의 주소가 출력됨.

# 함수 return문 활용
# 여러 값을 반환할 때
def swap(a, b):
    return b, a
print(swap(10, 20)) # 결과값은 튜플로 반환된다.

#변경 가능 객체를 인수로 전달할 경우
def g(t):
    t[0] = 0

a = [1, 2, 3]
g(a)
print(a)


# 스코핑 롤(scope) L-E-G-B
x = 1
def func(a):
    return a + x #Local 스코프에 x가 없으므로 Global x를 사용한다.

def func2(a):
    x = 2
    return a + x # local 스코프에 x가 있으므로 Local x를 사용한다.

print(func(10))
print(func2(10))
print(x)


g = 1
def func3(a):
    global g
    g = 3 # 본 객체는 글로벌 객체이다.
    return a + g
print(func3(10))
print(g)

def sum(a, b):
    return a + b
def incr(a, step = 1) : # 두번째 인자의 기본값은 1
    return a + step
print(sum(2, 3))
print(incr(10)) # 두 번째 인자의 기본값을 사용한다.
print(incr(10, 2)) # 두 번째 인자를 직접 지정한다.