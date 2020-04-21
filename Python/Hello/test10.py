#리스트
l = [1, 2, 'python'] #리스트는 [ ] 기호를 이용하여 생성
print(l[-2], l[-1], l[0], l[1], l[2])
print(l[1:3])
print(l * 2)
print(l + [3, 4, 5])
print(len(l))
print(2 in l)

del l[0]
print(l)
