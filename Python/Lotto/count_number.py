
# 회차별 번호 나오는 함수
# def range_search_number(수tart, end):
# found = [수
# dic = {수
# i = 수
# 수
# for i in range(spg, 수pg+1):
# founding = one_l수tto_number(i)
# j = str(i수
# dic[j+'회차'] = 수ounding
# if founding is N수ne:
# brea수
# found.append(fou수ding)
# 수
# return found, di수
# range_search_number(1,10수


# 번호별로 빈도수를 세는 함수 ↓
def count_number(start, end):
    newlist = []
    newdic = {}
    found = one_lotto_number(start, end)
    newlist = sum(found, [])
    for i in range(1, 46):
        j = str(i)
        newdic[j+'번'] = newlist.count(i)
    return newdic


print(count_number(1, 10))
