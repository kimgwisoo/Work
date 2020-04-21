import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
pd.options.display.max_rows = 20
np.random.seed(12345)
plt.rc('figure', figsize=(10, 6))
np.set_printoptions(precision=4, suppress=True)


# df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b', 'd', 'd'],
# 'data1': range(8)})
# df2 = pd.DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],
# 'data2': range(5)})
# print(pd.merge(df1, df2, how='inner'))

data = pd.DataFrame(np.arange(6).reshape((2, 3)),
                    index=pd.Index(['Ohio', 'Colorado'], name='state'),
                    columns=pd.Index(['one', 'two', 'three'],
                                     name='number'))
result = data.stack()
print(result)
# df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
#                     'data1': range(7)})
# df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'],
#                     'data2': range(3)})
# print(pd.merge(df3, df4, left_on='lkey', right_on='rkey'))

# print(df1)
# print(df2)


# print(pd.merge(df1, df2))

# print(pd.merge(df1, df2, on='key'))

# print(pd.merge(df1, df2, how='outer'))
