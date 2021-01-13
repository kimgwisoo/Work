from pymongo import MongoClient
from pymongo import errors
from pandas import DataFrame
from pandas import Series
from matplotlib import pyplot as plt
from matplotlib import font_manager as fm
from Data_Processing_LottoNumber import connect_mongodb_data_to_frame, get_episode, get_assigned_before_episodes
import numpy as np


path = 'C:\\WINDOWS\\Fonts\\NanumMyeongjoBold.ttf'
fontprop = fm.FontProperties(fname=path, size=15)


# 데이터 시각화 함수
# - MongoDB에서 읽은 데이터를 표에 맞는 데이터 형식으로 한번 더 가공하여 시각화한다.
def analysis_by_frequency(df):
    global fontprop

    # 확인하고자 하는 회차
    last_episode = max(df['drwNo']) + 1

    # 로또 번호만 확인
    num_with_no_bonus = df.loc[:, 'drwtNo1': 'drwtNo6']

    # 1~6번호를 하나의 Series로
    full_value = Series()
    for idx in num_with_no_bonus:
        full_value = full_value.append(num_with_no_bonus[idx])

    # 1~6번호의 count 값이 들어 있는 Series
    full_value_count = full_value.value_counts()

    # 테이블 형식으로 빈도수 당첨 번호 표
    plt.subplot(211)

    # 테이블에 들어갈 행List
    cell_text = []

    # 빈도별 번호 갯수List
    number_length = []

    for value in full_value_count.unique():
        temp_df = full_value_count[full_value_count == value]
        temp_df.index.values.sort()
        number_length.append(temp_df.count())
        cell_text.append([value, temp_df.index.values])

    columns = ['Frequency', 'Number']
    plt.title('빈도수 당첨번호 표', fontproperties=fontprop)
    plt.axis('off')
    plt.table(cellText=cell_text, colLabels=columns, loc='center')

    # 막대 그래프로 당첨번호가 출현한 횟수 번호가 몇개 인지 확인
    plt.subplot(212)

    # 빈도수 인덱스로 정렬
    freq_count = full_value_count.value_counts().sort_index()
    y = freq_count.values
    x = np.arange(len(y))
    x_label = freq_count.index.values
    plt.title('%s회 이전 %s회 로또 빈도' % (last_episode, len(
        num_with_no_bonus)), fontproperties=fontprop)
    plt.bar(x, y)
    plt.xticks(x, x_label)
    plt.yticks(np.arange(max(number_length) + 1))
    plt.xlabel('출현 빈도수', fontproperties=fontprop)
    plt.ylabel('번호 갯수', fontproperties=fontprop)
    plt.subplots_adjust(hspace=0.5)
    plt.show()


# main 실행 함수
# 데이터 가공 함수와 시각화 함수로 원하는 결과를 출력한다.
# 예측하려는 회차를 check_episode에 대입하여 콘솔창으로 데이터를 미리 출력하고
# before_episode에 해당 회차 이전  n개 회차에 대한 데이터를 통계내어 시각화한다.
if __name__ == '__main__':

    check_episode = 841
    before_episode = 30

    # 예측하는 회차 번호
    lotto_data = connect_mongodb_data_to_frame(
        get_episode, {'episode': check_episode})
    print(lotto_data)

    lotto_data = connect_mongodb_data_to_frame(
        get_assigned_before_episodes,
        {
            'episode': check_episode,
            'before_num': before_episode
        }
    )
    analysis_by_frequency(lotto_data)
