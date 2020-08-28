import re
import sys


def text_sl():

    file = open("wrt.txt", 'r', encoding='utf=8')

    st = file.read()

    li = st.replace(' ', '').split('\n')

    reg1 = re.compile(r'▶|http://|hxxp://|\d+\)')  # 특정 문자열 제거
    reg2 = re.compile('[가-힣]')  # 한글
    reg3 = re.compile('\(.*?\)')  # 괄호안 문자열
    reg4 = re.compile('[a-zA-Z]')  # 알파벳
    reg5 = re.compile('[가-힣]')  # 한글

    domain = ""
    country = ""
    dm_list = []

    print("====================================================")
    for data in li:

        if len(data) == 0:
            continue  # 빈줄 Skip

        orgStr = reg1.sub('', data)  # 특정 문자열 제거
        country = "".join(reg2.findall(orgStr))  # 한글국가코드 추출
        str3 = "".join(reg3.findall(orgStr))  # 괄호안 문자열 추출

        if len(str3) == 4:  # 괄호안이 국가코드인 경우
            domain = orgStr[0:-4]
            country = str3[1:-1]  # 국가코드
        elif len(str3) > 0:  # 괄호체크
            if len(reg4.findall(str3)) > 0:  # 괄호 안에 영문자 포함하고 있으면 도메인
                domain = str3[1:-1]
            else:  # 괄호 밖 문자열 도메인
                domain = orgStr[0:orgStr.find("(")]
        elif orgStr.find(",") > 0:  # 괄호 없으면서 ,로 구분된 경우
            domain = orgStr[0:orgStr.find(",")]
        else:
            domain = orgStr

        domain = reg5.sub('', domain)  # 한글

        print("1차 경유지 : http://" + domain + " (" + country + ",")
        dm_list.append(domain)

    print("====================================================")
    for dm in dm_list:
        print(dm, end=', ')
    print("")
    print("====================================================")


text_sl()
Finish = input()
sys.exit(1)
