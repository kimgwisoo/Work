from Data_Processing_LottoNumber import sort_and_get_nums, get_assigned_before_episodes, get_episode
from pymongo import MongoClient
from pymongo import errors
from pandas import Series
from pandas import DataFrame


# 몽고디비 연결 및 데이터프레임으로
def connect_mongodb_data_to_frame(func, params):

    try:
        # db connection
        conn = MongoClient('localhost')
        db = conn.lotto_db
        collection = db.lotto

        df = func(collection, params)
    except errors.ConnectionFailure:
        print("Connection Err")
    finally:
        conn.close()

    return df


# 지정회차 로또 당첨 정보
def get_episode(collection, params):
    episode = collection.find({'drwNo': params['episode']})
    df = sort_and_get_nums(episode)
    return df


# episode회차 이전 num회 당첨 정보
def get_assigned_before_episodes(collection, params):
    diff = params['episode'] - params['before_num']
    if diff < 1:
        diff = 1
        print('음수가 발생하였습니다. 1회부터 시작입니다.')
    assignend_episodes = collection.find(
        {'drwNo': {'$gte': diff, '$lt': params['episode']}})
    df = sort_and_get_nums(assignend_episodes)
    return df


# 로또 빈도수 별 당첨번호, 빈도수, 빈도별 번호 Count
def get_frequency_lists(df):
    # 로또 번호만 확인
    num_with_no_bonus = df.loc[:, 'drwtNo1': 'drwtNo6']

    # 1~6번호를 하나의 Series로
    full_value = Series()
    for idx in num_with_no_bonus:
        full_value = full_value.append(num_with_no_bonus[idx])

    # 1~6번호의 count 값이 들어 있는 Series
    full_value_count = full_value.value_counts()

    # 각 빈도수 별 번호 집합(Number)
    number_list = []

    # 빈도수 List
    freq_list = []

    # 빈도별 번호 갯수List(표 Y값 Array)
    freq_number_count_list = []

    for value in full_value_count.unique():
        temp_df = full_value_count[full_value_count == value]
        temp_df.index.values.sort()
        number_list.append(temp_df.index.values)
        freq_list.append(value)
        freq_number_count_list.append(temp_df.count())
    return number_list, freq_list, freq_number_count_list


def get_frequency_lists_to_df(df):
    number_list, freq_list, freq_number_count_list = get_frequency_lists(df)
    data = {
        'frequency': freq_list,
        'numbers': number_list,
        'count': freq_number_count_list
    }
    freq_df = DataFrame(data)
    print(freq_df)
    return freq_df


# df 데이터 에서 빈도수 별 숫자의 Count에서 win_episode의 숫자들이 몇 빈도수에 해당하는지 count and 번호 return
def get_win_numbers_in_frequency_lists(df, win_episode):
    # 확인할 회차 데이터 불러오기
    win_lotto_data = connect_mongodb_data_to_frame(
        get_episode, {'episode': win_episode})
    win_lotto_data_no_bonus = win_lotto_data.loc[:,
                                                 'drwtNo1':'drwtNo6'].iloc[0]
    freq_df = get_frequency_lists_to_df(df)

    # 빈도수가 자체로 들어가 있는 리스트
    freq_raw_list = []

    # 빈도수 포함 당첨 번호
    win_num_in_freq_list = []

    # 당첨 번호가 빈도수 몇에 위치하는지 확인
    for win_num in win_lotto_data_no_bonus:
        for row_index in range(len(freq_df.index)):
            if win_num in freq_df['numbers'].iloc[row_index]:
                freq_raw_list.append(freq_df.iloc[row_index]['frequency'])
                win_num_in_freq_list.append(win_num)
                continue

    # 빈도수 별  Count
    freq_list_count = Series(freq_raw_list).value_counts()
    freq_list_count.index.name = 'frequency'
    freq_list_count.name = 'count'
    return freq_list_count, win_num_in_freq_list


# start_episode 에서 end_episode 까지 EX) 1~4 -> 1,2 | 2,3 | 3,4 이렇게 3경우를 확인
def analysis_check_numbers_with_before_episode(start_episode, end_episode):
    count = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count0 = 0
    for episode in range(start_episode + 1, end_episode + 1):
        df = connect_mongodb_data_to_frame(
            get_assigned_before_episodes,
            {
                'episode': episode,
                'before_num': 1
            }
        )
        freq_list_count, win_num_in_freq_list = get_win_numbers_in_frequency_lists(
            df, episode)
        freq_size = len(win_num_in_freq_list)
        if freq_size > 0:
            count += 1
        if freq_size == 1:
            count1 += 1
        elif freq_size == 2:
            count2 += 1
        elif freq_size == 3:
            count3 += 1
        elif freq_size == 4:
            count4 += 1
        elif freq_size == 5:
            count5 += 1
        elif freq_size == 6:
            count6 += 1
        else:
            count0 += 1

    print("count : ", count)
    print("count1 : ", count1)
    print("count2 : ", count2)
    print("count3 : ", count3)
    print("count4 : ", count4)
    print("count5 : ", count5)
    print("count6 : ", count6)
    print("count0 : ", count0, '\n')

    print(start_episode, '회 부터 ', end_episode, '회 까지 이전회차 출현 비율')
    print('이전회차 번호 1개 출현 비율 : %.2f' %
          (count1 / (end_episode - start_episode) * 100.0) + '%')
    print('이전회차 번호 2개 출현 비율 : %.2f' %
          (count2 / (end_episode - start_episode) * 100.0) + '%')
    print('이전회차 번호 3개 출현 비율 : %.2f' %
          (count3 / (end_episode - start_episode) * 100.0) + '%')
    print('이전회차 번호 4개 출현 비율 : %.2f' %
          (count4 / (end_episode - start_episode) * 100.0) + '%')
    print('이전회차 번호 5개 출현 비율 : %.2f' %
          (count5 / (end_episode - start_episode) * 100.0) + '%')
    print('이전회차 번호 6개 출현 비율 : %.2f' %
          (count6 / (end_episode - start_episode) * 100.0) + '%')
    print('이전회차 번호 0개 출현 비율 : %.2f' %
          (count0 / (end_episode - start_episode) * 100.0) + '%')
    print('이전회차 번호 출현 비율 : %.2f' %
          (count / (end_episode - start_episode) * 100.0) + '%')


print(analysis_check_numbers_with_before_episode(915, 945))
# if __name__ == '__main__':
#     check_episode = 841
#     before_episode = 30

#     # # 예측하는 회차 번호
#     lotto_data = connect_mongodb_data_to_frame(
#         get_episode, {'episode': check_episode})
#     print(lotto_data)

#     lotto_data = connect_mongodb_data_to_frame(
#         get_assigned_before_episodes,
#         {
#             'episode': check_episode,
#             'before_num': before_episode
#         }
#     )
#     print(lotto_data)
# lotto_data = connect_mongodb_data_to_frame(
#     analysis_check_numbers_with_before_episode(check_episode, before_episode))
# print(lotto_data)
