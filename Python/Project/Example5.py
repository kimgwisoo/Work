# import numpy as np
# dt = np.dtype(np.int32)
# print(dt)


# import numpy as np
# dt = np.dtype([('age', np.int8)])
# print(dt)


import numpy as np

dt = np.dtype([('age', np.int8)])
a = np.array([(10,), (20,), (30,)], dtype=dt)
print(a['age'])
