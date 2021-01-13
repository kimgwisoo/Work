
vowels = ['a', 'e', 'i', 'o', 'u']  # 'vowels' 변수에 리스트 작성
word = input("Provide a word to search for vowels: ")  # 'word' 변수에 input함수 적용
found = {}   # found에 빈 딕셔너리 생성

found['a'] = 0
found['e'] = 0
found['i'] = 0          # 각 모음키와 관련된 값은 0으로 초기화
found['o'] = 0
found['u'] = 0


for letter in word:           # word라는 변수안에 letter값을 반복시킴
    if letter in vowels:      # vowels 변수안에 letter 값이 있으면
        found[letter] += 1    # found[letter]가 가리키는 값을 1 증가 시킴

# 'for' 루프가 'items'메서드를 사용하므로 키에 대응하는 'k'와 값에 대응하는 'v' 두가지 루프 변수를 제공해야 됨
for k, v in sorted(found.items()):
                                          # 'found' 딕셔너리에 'items' 메서드를 호출해 각 행의 데이터에 접근합니다.
    print(k, 'was found', v, 'time(s).')  # 'k' 와 'v'를 이용해 각각의 출력 메시지를 만듬.
