import numpy as np  # numpy, pandas는 나중에 분석을 하기 위해 import 를 합니다.
import pandas as pd
import requests
import sys
import bs4
import re
import urllib.request
import random
from prompt_toolkit import document


# 크롤링 하기 위한 URL 주소, 회차별 {page}에 원하는 회차를 입력하면 해당 회차의 당첨번호 페이지가 나옵니다.
search_url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={page}"


def one_lotto_number(page):  # 로또 회차별 당첨 번호를 선별하는 함수
    response = urllib.request.urlopen(search_url.format(page=page))
    lotto_data = response.read()

    soup = bs4.BeautifulSoup(lotto_data)
    ret = []
    newret = []

    for winnums in soup.findAll('div', attrs={'class': 'num win'}):
        winnum = winnums.findAll('span')
        ret.append(winnum)
    ret = ret[0]

    # ret 안에 있는 값을 하나씩 문자열로 치환후 re.sub를 이용하여 '<>' 괄호안에 있는 모든 것들을 지우고 onlynum 변수에 저장
    # 그리고 onlynum 변수를 newret 배열에 저장
    for i in ret:
        string = str(i)
        onlynum = re.sub('<.+?>', '', string, 0, re.I | re.S)
        newret.append(onlynum)
    newret = list(map(int, newret))  # 배열에 있는 당첨번호를 숫자형태로 변환하기 위해 map을 활용.

    return newret


def getLast():
    resp = requests.get(search_url)
    soup = bs4.BeautifulSoup(resp.text, 'lxml')
    # meta tag에서 id 속성이 desc이고 name 속성이 description인 tag를 찾아 content를 string으로 result에 저장
    result = str(
        soup.find('meta', {'id': 'desc', 'name': 'description'})['content'])

    s_idx = result.find(" ")  # 1. 회차 앞에 공란이 있고
    e_idx = result.find("회")  # 2. 회차 다음에 '회'가 나오기 때문에

    # 3. 공란 다음부터 '회'이전까지가 마지막 회차이며 이것을 integer로 변환하여 리턴한다.
    return int(result[s_idx + 1: e_idx])


last = getLast()


old_lotto_numbers = []
my_lotto_numbers = []

for i in range(1, last):
    # list에 one_lotto_number 뽑아낸 결과를 순차적으로 append를 시킵니다.
    old_lotto_numbers.append(one_lotto_number(i))

# 번호를 수집했고

# my_lotto_numbers가 10이 될때 까지 while문으로 돌려주고 내가 원하는 셋트의 수이기 때문에 원하는 숫자로 변경할수 있음
while len(my_lotto_numbers) < 10:
    list_of_numbers = list(range(1, 46))  # range함수로 1부터 45까지 만든 후 list를 만듭니다.
    # shuffle이라는 함수는 list에 있는 숫자를 random하게 섞을수 있습니다. 1~45까지 숫자가 섞임
    random.shuffle(list_of_numbers)
    numbers = list_of_numbers[:6]  # 그중 첫 6개 숫자를 뽑아 numbers라는 변수에 집어 넣고

    if numbers not in old_lotto_numbers or numbers not in my_lotto_numbers:
        # if문을 사용하여 이렇게 뽑은 번호(numbers)가 과거 로또 번호와 내가 뽑은 로또 번호가 겹치는지 확인을 하며, not in 키워드를 사용하면 해당 리스트 안에 같은 값이 들어갔는지 여부를 check 함
        # old_lotto_number와 my_lotto_numbers에 모두 없다면 my_lotto_nubers에 numbers를 삽입하겠다
        my_lotto_numbers.append(numbers)


# bestnumbers1.txt 파일에 쓰기로 합니다. // 참고로  w : 쓰기모드 , r : 읽기 모드, A : 추가모드
f = open("./bestnumbers.txt",
         'w', encoding='UTF-8')
for nums in my_lotto_numbers:  # my_lotto_numbers에 내용이 바닥날때까지 반복을 하겠다
    # nums는 숫자 list임으로 sorted로 정렬를 하고 str으로 변환하여 끝 지점에 \n를 하게 됩니다.
    f.write(str(sorted(nums)) + "\n")
f.close()  # 그리고 파일을 닫습니다.
