from pymongo import MongoClient
from pymongo import errors
from pandas import DataFrame


# 당첨 번호와 회차만 나오도록 정리 오름 차순
def sort_and_get_nums(cursor_data):
    df = DataFrame(list(cursor_data))
    df = df[[
        'drwNo',
        'drwtNo1',
        'drwtNo2',
        'drwtNo3',
        'drwtNo4',
        'drwtNo5',
        'drwtNo6',
        'bnusNo'
    ]
    ].sort_values(by='drwNo', ascending=True)
    return df


# 몽고디비 연결 및 데이터프레임으로
def connect_mongodb_data_to_frame(func, params):

    try:
        # db connection
        conn = MongoClient('localhost')
        db = conn.lotto_db
        collection = db.lotto

        df = func(collection, params)
    except errors.ConnectionFailure:
        print("Connection Error")
    finally:
        conn.close()

    return df


# 전체 로또 당첨 정보
def get_all_episodes(collection, params):
    episodes = collection.find(params)
    df = sort_and_get_nums(episodes)
    return df


# 지정회차 로또 당첨 정보 ('episode' key값으로 해당 회차 정보를 가지고 옴)
def get_episode(collection, params):
    episode = collection.find({'drwNo': params['episode']})
    df = sort_and_get_nums(episode)
    return df


# 최근 num회 로또 당첨번호 정보
def get_recent_episodes(collection, params):
    recent_episodes = collection.find().sort('drwNo', -1).limit(params['num'])
    df = sort_and_get_nums(recent_episodes)
    return df


# 특정 회차 이전 n회 로또 당첨 정보
# episode와 before_num의 key값으로 해당 회차로부터 n회 이전 로또 당첨번호를 받아온다.
def get_assigned_before_episodes(collection, params):
    diff = params['episode'] - params['before_num']
    if diff < 1:
        diff = 1
        print('음수가 발행하였습니다. 1회부터 시작입니다.')
        assignend_episodes = collection.find(
            {'drwNo': {'$gte': diff, '$lt': params['episode']}})
        df = sort_and_get_nums(assignend_episodes)
        return df


# 특정 회차 이후 n회 로또 당첨 정보
# episode와 after_num의 key값으로 해당 회차로부터 n회 이후 로또 당첨번호를 받아온다.
def get_assigned_after_episodes(colllection, params):
    added = params['episode'] + params['after_num']
    assignend_episodes = colllection.find(
        {'drwNo': {'$gt': params['episode'], '$lte': added}})
    df = sort_and_get_nums(assignend_episodes)
    if len(df) < params['after_num']:
        print("현재까지 발표된 로또 회차를 초과합니다.")
    return df


# episode1회차 ~ episode2회차 까지의 당첨 정보 받아오기
def get_assigned_between_episodes(collection, params):
    assigned_episodes = collection.find(
        {'drwNo': {'$gte': params['episode1'], '$lte': params['episode2']}})  # $gte
    df = sort_and_get_nums(assigned_episodes)
    return df


if __name__ == '__main__':
    # 전체 로또 당첨 정보
    # lotto_data = connect_mongodb_data_to_frame(get_all_episodes, {})

    # 지정회차 로또 당첨 정보 ('episode' key값으로 해당 회차 정보를 가지고 옴)
    # lotto_data = connect_mongodb_data_to_frame(get_episode, {'episode': 15})

    # 최근 num회 로또 당첨번호 정보
    # lotto_data = connect_mongodb_data_to_frame(
    #     get_recent_episodes, {'num': 15})

    # 특정 회차 이전 n회 로또 당첨 정보
    # episode와 before_num의 key값으로 해당 회차로부터 n회 이전 로또 당첨번호를 받아온다.
    # lotto_data = connect_mongodb_data_to_frame(get_assigned_before_episodes, {
    #    'episode': 820, 'before_num': 15})

    # 특정 회차 이후 n회 로또 당첨 정보
    # episode와 after_num의 key값으로 해당 회차로부터 n회 이후 로또 당첨번호를 받아온다.
    # lotto_data = connect_mongodb_data_to_frame(get_assigned_after_episodes, {
    #    'episode': 810, 'after_num': 15})

    # episode1회차 ~ episode2회차 까지의 당첨 정보 받아오기
    lotto_data = connect_mongodb_data_to_frame(get_assigned_between_episodes, {
        'episode1': 30, 'episode2': 50})

    print(lotto_data)
