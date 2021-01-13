# Python 프로그래밍 기초
# 제어문 (조건문과 반복문)

# 조건문 (if - elif - else)
n = -2
if n > 0:
    print("양수")
elif n < 0:
    print("음수")
else:
    print("0")


# -> 조건 표현식 : C 또는 Java의 3항 연산자와 같은 역할
#value = {true-expr} if {condition} else {false-expr}
money = 8500
print("by taxi" if money > 10000 else "by bus")

# 반복문
# ex1)
# list 객체를 이용한 for문
animals = ['cat', 'cow', 'tiger']
for animal in animals:
    print(animal, end = " ")

# range 객체를 이용한 for 문
for x in range(1, 10, 3):
    print(x, end = " ")

# for ~ else 문의 활용
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in data :
    if x > 10 :
        break
else:
    print("10보다 큰 수 없음.")

# 반복문 - 요소의 값은 물론 인덱스가 필요할 경우 enumerate() 함수를 이용한다.
colors = ['red', 'orange', 'yellow', 'green', 'pink', 'blue']
for index, color in enumerate(colors):
    print(index, color)


# 반복문(break) - 어떤 조건에서 반복을 중지하고 빠져나가야 하는 경우 break문
l = [1, 3, 5, 7, 9, 11, 12, 13, 15, 17]
for x in l:
    if x % 2 == 0:
        break;
    print(x)


# 반복문(continue) : continue문을 만나면, 이후 구문은 실행하지 않고 처음으로 이동한다.
for x in range(10):
    if x % 2 == 0:
        continue
    print(x, end = " ")


# 반복문(while)
counter = 1
while counter < 11:
    print(counter, end = " ")
    counter += 1
else:
    print(" ")

sum, i = 0, 1
while i <= 100: # 1~100까지의 정수 합 구하기
    sum += i
    i += 1
print(sum)

# 반복문 : while 내부에서 Break, continue, else 사용하기
i = 0
while i < 100:
    i += 1
    if i < 5:
        continue
    print(i, end = " ")
    if i > 10:
        break
else:
    print("else block") # 이 블록은 실행되지 않을 것임. Why?

