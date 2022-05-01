from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# s = pd.Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
# s.plot()
# plt.show()

# df = pd.DataFrame(np.random.randn(10, 4).cumsum(0),
#                   columns=['A', 'B', 'C', 'D'],
#                   index=np.arange(0, 100, 10))
# df.plot()
# plt.show()

fig, axes = plt.subplots(2, 1)
data = pd.Series(np.random.rand(16), index=list('abcdefghijklmnop'))
data.plot(kind='bar', ax=axes[0], color='k', alpha=0.7)
data.plot(kind='barh', ax=axes[1], color='k', alpha=0.7)

df = pd.DataFrame(np.random.rand(6, 4),
                  index=['one', 'two', 'three', 'four', 'five', 'six'],
                  columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus'))

df.plot(kind='barh', stacked=True, alpha=0.5)

plt.show()
