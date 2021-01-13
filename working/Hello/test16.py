#순차 자료형 내장함수 : range

seq = range(10) # 0이상 10 미만의 순차적 정수 목록
print(seq, type(seq))
print(seq[0:])
print(len(seq))

for i in seq:
    print(i)

seq2 = range(5, 15) # 5 이상 15미만의 순차적 정수 목록
for i in seq2:
    print(i)

seq3 = range(0, -10, -1) # 0이하 -10 초과의 -1주기 순차적 정수 목록
for i in seq3:
    print(i)



# 글로벌 변수 선언
g_a = 1
g_b = "symbol"

def f(): # 로컬 변수 확인을 위한 함수 선언
    l_a = 2
    l_b = "table"
    print(locals()) #로컬 심볼 테이블 확인 / Local (지역변수) : memory와 관련 있는 함수임.
f()
globals()  # Globals (전역 변수) : 어떤함수에서도 참조 할 수 있음.

# 레퍼런스 카운트(함수를 참조하는 횟수)와 쓰레기 수집
# 참조 카운트가 0이 되는 순간 환원 받음. 사용하지 않는 객체로 판단 지역변수로 취급

import sys # 왜??
x = object()
print(sys.getrefcount(x)) # 레퍼런스 카운트(함수를 참조하는 횟수)
y = x
print(sys.getrefcount(x))
print(sys.getrefcount(y))
del(x) #레퍼런스 값이 줄어든다.
print(sys.getrefcount(y))

# 객체 변수명은 id (참조하고 있는 함수)
# 10값을 가지고 있는 객체를 i1, i2에다 각각 할당 하였다. (i1 = 10, i2 = 10)
# id를 찍어보니 동일 함. -> 같은 객체를 참고하고 있다.
i1 = 10
i2 = 10
print(hex(id(i1)), hex(id(i2)))
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(hex(id(i1)), hex(id(id)))
s1 = "hello"
s2 = "hello"
print(hex(id(s1)), hex(id(s2)))
print(i1 is i2)
print(l1 is l2)
print(s1 is s2)

#레퍼런스 복사
x = [1, 2, 3]
y = x #객체 참조 주소만 복사된다.
print(y)
print(hex(id(x)), hex(id(y)))
x[1] = 4
print(y)

x = [1, 2, 3]
y = x[:]
print(y)
print(hex(id(x)), hex(id(y)))
x is y
x[1] = 4
print(x, y)

print(hex(id(x)), hex(id(y)))


# Copy : copy 모듈의 copy 함수를 사용하여 복사한다
import copy
x = [1, 2, 3]
y = copy.copy(x)
print(x is y)
x[1] = 4
print(y)


# 복합형태의 복사 - deepcopy 함수 이용
#  copy 모듈의 deepcopy 함수를 사용하여 복사한다
#  deepcopy는 복합객체를 재귀적으로 생성하고 복사한다
a = [1, 2, 3]
b = [4, 5, a]
x = [a, b, 100]
import copy
y = copy.deepcopy(x)