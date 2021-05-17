import pyupbit
import numpy as np


def get_ror(k=0.5):
    # OHLCV(open, high, low, close, volume)로 당일 시가, 고가, 저가, 종가, 거래량에 대한 데이터
    df = pyupbit.get_ohlcv("KRW-EOS", count=7)

    # 변동성 돌파 기준 범위 계산, (고가 - 저가) * k
    df['range'] = (df['high'] - df['low']) * k

    # range 컬럼을 한칸씩 밑으로 내림(.shift(1))
    df['target'] = df['open'] + df['range'].shift(1)

    # np.where(조건문, 참일때 값, 거짓일때 값)
    df['ror'] = np.where(df['high'] > df['target'],
                         df['close'] / df['target'],
                         1)

    #
    ror = df['ror'].cumprod()[-2]
    return ror


for k in np.arange(0.1, 1.0, 0.1):
    ror = get_ror(k)
    print("%.1f %f" % (k, ror))
