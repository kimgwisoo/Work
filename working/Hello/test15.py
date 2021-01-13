## 사전(Dict)
# 순서가 가지지 않는 객체의 집합
# Key 기반으로 값을 저장하고 참조하는 매핑형 자료형
# 시퀀스 자료형이 아니므로 Len(), in, not in 정도만 가능
d = {'basketball': 5, 'soccer': 11, 'baseball': 9}
print(d, type(d))

print(d['basketball'])

d['volleyball'] = 6
print(d)

print(len(d))
print('soccer' in d)
print('volleyball' not in d)


# 다양한 사전 생성 방법

d = dict() #empty dict
print(d)

d = dict(one=1, two=2)
print(d)

d = dict([('one', 1), ('two', 2),])
print(d)


keys = ('one', 'two', 'three')
values = (1, 2, 3)
d = dict(zip(keys, values)) #키와 값을 별도로 선언 후 합침
print(d)

# 사전의 키
## 사전의 키는 해싱해야 하기 때문에 수정 불가능한 객체여야 한다.

d = {}
print(d)

d[True] = 'true'
d[10] = '10'
d["twenty"] = '20'
d[(1, 2, 3)] = '6'
print(d)

# 사전의 메서드

d = {'basketball': 5, 'soccer': 11, 'baseball':9}
d['volleyball'] = 6 #새로운 값 할당
 # 전부 리스트로 반환
print(d.keys()) #key 목록 가져오기
print(d.values()) #value 목록 가져오기
print(d.items()) #(key, value) 튜플 목록 가져오기


d = {'basketball': 5, 'soccer': 11, 'baseball':9}
d['volleyball'] = 6

print(d.keys())
print(d.values())
print(d.items())

# x = d["handball'] # keyError
x = d.get('handball') # None 반환
del d['soccer']
print(x)

d.clear()
print(d)

# 사전순회

d = {'basketball': 5, 'soccer': 11, 'baseball':9}
for key in d:
    print(str(key) + ":" + str(d[key]), end = ' ')
else:
    print()

for key in d.keys():
    print("{0}:{1}".format(key, d[key]), end = ' ')
else:
    print()

for key, value in d.items():
    print("{0}:{1}".format(key, value), end = ' ')
else:
    print()


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

seq3 = range(0, -10, -1) # 0이하 -10 초과의 순차적 정수 목록
for i in seq3:
    print(i)