#리스트 : 리스트의 메서드
a = [1, 2, 3]
print(a)
a.append(5)
print(a)
a.insert(3, 4) # 인덱스 3에 요소 4를 추가
print(a)
print(a.count(2)) #리스트 내 요소 2의 개수를 반환
a.reverse()
print(a)
a.sort()
print(a)
a.remove(3) #내부에 있는 요소 3을 제거
print(a)
a.extend([6, 7, 8]) #extend - 확장
print(a)

a.append([5, 6, 7]) #리스트 내부에 리스트가 추가됨.
print(a)
print(len(a))
