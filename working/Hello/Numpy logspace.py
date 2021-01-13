# numpy.logspace(start,stop, num, endpoint,base,dtype)  logspace명령어 작성
# set base of log space to 2
import numpy as np
a = np.logspace(1, 10, num=10, base=2)
print(a)
