#리스트 : 리스트를 stack으로 사용
 # 리스트의 append와 pop에서드를 이용하여 스택을 구현할 수 있다.

stack = [ ]

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

print(stack.pop())
print(stack.pop())
print(stack)


#리스트 : 리스트를 Queue로 사용하기

queue = [ ]
queue.append(100)
queue.append(200)
queue.append(300)

print(queue)

print(queue.pop(0)) # 가장 앞쪽 인덱스의 요소를 pop
print(queue.pop(0))

print(queue)

# 리스트 : sort에서드의 reverse를 true로 설정하면 역순으로 정렬할 수 있다.

l = [1, 5, 3, 8, 4, 2]
print(l)
l.sort()
print(l)

l.sort(reverse=True)
print(l)


# Sort 에서의 활용 : 키값 기반의 사용자 정의 정렬
l = [10, 2, 22, 9, 8, 33, 4, 11]
l.sort(key = str) # 문자열 정렬 X
print(l)

l.sort(key = int) # 정수 정렬 O
print(l)

l = ["ㄱ", "ㄷ", "ㅂ" ,"ㅊ" ,"ㅇ" ,"ㄱ"]
l.sort(key = str) # 한글 문자열에 대해서는  " "로 묶음.
print(l)
l.sort(reverse=True)
print(l)

# 세트(Set)
# 1. 순서가 없고 중복이 없는 개체들의 집합(non sequence), [ ] 기호로 정리
# 2. len(), in, not in 정도만 활ㄹ용
# 3. 수정이 가능한 (mutable) 자료형
# 4. 수학의 집합을 표한 할 때 사용한다.
# 리스트 [ ], 세트 { }, 튜플 ( ), 사전 'key' :val

a= {1, 2, 3}
print(a, type(a))

print(len(a))
print(2 in a)
print(2 not in a)

a= {"hello"}
print(a, type(a))

print(len(a))
print(2 in a)
print(2 not in a)

#add(x) 세트에 x를 추가
#remove(x) 세트에 x를 제거, x가 세트에 업승면 오류 발생
#discard(x) 세트에 x를 제거, x가 세트에 없으면 무시
#updatae({set}) 세트에 여러개의 ㄱ밧응 추가
#clear() 세틀 비움

s = {1, 2, 3}
s.add(4)
print(s)
s.add(1)
print(s)
s.discard(2)
print(s)
s.remove(3)
print(s)
s.update({2, 3})
print(s)
s.clear()
print(s)

#집합 교집합 a&b a.intersection(b)
     #합집합 a|b a.union(b)
     #차집합 a-b a.difference(b)
     #모집합 a.issuperset(b)
     #부분집합 a.issubset(b)
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s2 = {10, 20, 30}

s3 = s1.union(s2) #합집합
print(s3)

s3 = (s1 & s2) #교집합
print(s3)

s4= s1.intersection(s2) #교집합
print(s4)

s5 = s1.symmetric_difference(s2)  #대칭자 (둘 모두 속하지 않은 원소 집합)
print(s5)

print(s1.issuperset(s4)) # 확대집합?
print(s5.issuperset(s1))
print(s2.issubset(s3)) # 부분집합

# 튜플 - 리스트와 거의 비슷하지만 다름 : 시퀀스 자료형
# 1) 튜플은 () 기호로 생상하며 그 값을 바꿀 수 없다.(immutable)
# 2) 하나의 요소만을 가질 때는 요소 뒤에 컴마(,)를 반드시 붙임
# 3) 괄호를 생략해도 튜플로 인식
t = (1, 2, 3)
print(t, type(t))

t = 1, 2, 'python' # ()를 생략해도 튜플을 생성할 수 있따.
print(t, type(t))

print(t[-2], t[0], t[-1], t[2]) #인덱싱
print(t[1:3]) #슬라이싱
print(t[:])

print(t * 2) #반복 (*)
print(t + (3, 4, 5)) # 연결 (+)
print(len(t)) # 요소 개수 반환
print(5 in t) # 요소 5가 내부에 있는지 확인.
# t1 = ( )
# t2 = (1, )

### 리스트 - [ ] 원소변경 가능 , 튜플 - ( ) 원소 변경 불가능


# 튜플
# 1) Packing : 나열된 객체를 Tuple로 저장하는 것
# 2) Unpacking : 튜플, 리스트 안의 객체를 변수로 할당하는 것

t = 10, 20, 30, 'python'
print(t)
print(type(t))

# unpacking tuple
a, b, c, d= t
print(a, b, c, d)

# unpacking list
a, b, c, d = [10, 20, 30, 'python']
print(a, b, c, d)

# unpacking 시 왼쪽 변수가 부족한 경우, 에러가 발생한다(ValueError)
# 확장 Unpacking에서는 왼쪽 변수가 적은 경우에도 적용할 수 있다.(*)

t = (1, 2, 3, 4, 5, 6)
a, *b = t
print(a, b)

*a, b = t
print(a, b)

a, b, *c = t
print(a, b, c)

a, *b, c = t
print(a, b, c)

## 사전(Dict)
# 순서가 가지지 않는 객체의 집합
# Key 기반으로 값을 저장하고 참조하는 매핑형 자료형
# 시퀀스 자료형이 아니므로 Len(), in, not in 정도만 가능
d = {'basketvall': 5, 'soccer': 11, 'baseball': 9}
print(d, type(d))

print(d['backetball'])

d['volleyball'] = 6
print(d)

print(len(d))
print('soccer' in d)
print('volleyball' not in d)


# 다양한 사전 생성 방법
