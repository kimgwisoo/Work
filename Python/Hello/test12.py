#리스트 : 슬라이스 이용한 삭제와 삽입
#슬라이스를 이용한 삭제
a = [1, 12, 123, 1234]
a[1:2] = [ ]
print(a)
a[0:] = [ ]
print(a)

# 슬라이스를 이용한 삽입
a = [1, 12, 123, 1234]

a[1:1] = ['a']
print(a)

a[5:] = [12345]
print(a)

a[:] = [-12, -1, 0]
print(a)
