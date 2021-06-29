import time
import pyupbit
import datetime

access = "710vTenV4owEWwmEaO5RlbDa3CsuokL9Rw3PTfrc"
secret = "tMP0lHWt84ewjZKiRbvKgTxfkfLan4fDxTj0X9x6"


def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + \
        (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price


def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time


def get_ma15(ticker):
    """15일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=15)
    ma15 = df['close'].rolling(15).mean().iloc[-1]
    return ma15


def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0


def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]


# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# 자동매매 시작
while True:
    stock_krw = ['KRW']
    stock_list = [{'stock': 'BTT', 'count': 0.4},
                  {'stock': 'QKC', 'count': 0.2}]
    # print(type(stock_list[0]['count']))
    try:
        for stocks in stock_list:
            now = datetime.datetime.now()
            start_time = get_start_time("KRW-{}".format(stocks['stock']))
            end_time = start_time + datetime.timedelta(days=1)
            if start_time < now < end_time - datetime.timedelta(seconds=10):

                target_price = get_target_price(
                    "KRW-{}".format(stocks['stock']), stocks['count'])

                ma15 = get_ma15("KRW-{}".format(stocks['stock']))

                current_price = get_current_price(
                    "KRW-{}".format(stocks['stock']))

                if target_price < current_price and ma15 < current_price:
                    krw = get_balance("KRW")
                    if krw > 5000:
                        upbit.buy_market_order(
                            "KRW-{}".format(stocks['stock']), krw*0.9995)
            else:
                btc = get_balance("{}".format(stocks['stock']))
                if btc > 0.00008:
                    upbit.sell_market_order(
                        "KRW-{}".format(stocks['stock']), btc*0.9995)
            print(stock_list)
            print(start_time)
            print(end_time)
            print(target_price)
            print(ma15)
            print(current_price)
            print(krw)
            print(btc)
            time.sleep(1)

    except Exception as e:
        print(e)
        time.sleep(1)
