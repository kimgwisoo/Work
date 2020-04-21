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
    print("else block") # 이 블록은 실행되지 않을 것임. WhY?