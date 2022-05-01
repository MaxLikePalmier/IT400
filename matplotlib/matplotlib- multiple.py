# 載入 matplotlib 模組
import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(0, 10, 1001)
# y1 = x
# y2 = 100-x

# fig = plt.figure()
# sub = fig.add_subplot(1,1,1)
# sub.plot(x, y1, label=r'$y=x$')
# sub.set_xlabel(r'$x$', fontsize=15)
# sub.set_ylabel(r'$y$', fontsize=15, color='C0')
# sub.tick_params(which='both', axis='y', colors='C0')
# sub.legend(loc='center left')

# sub2 = sub.twinx() # twinx()共用x, twiny()共用y
# sub2.plot(x, y2, label=r'$y=100-x$', color='C1')
# sub2.legend(loc='center right')
# sub2.set_ylabel(r'$y2$', fontsize=15, color='C1')
# sub2.tick_params(which='both', axis='y', colors='C1')

# plt.show()

x = np.linspace(0, 1, 101)
y = np.cos(2 * np.pi * x)

fig = plt.figure()
sub = fig.add_subplot(1, 1, 1)
sub.plot(x, y)
# sub.axvspan(0.25, 0.75, color='yellow',
#             alpha=0.5, label='$y\leq 0$')  # 添加陰影區域 axvspan:縱向, axhspan:橫向
# sub.legend()

x1 = np.linspace(0.25, 0.75, 100)
y1 = np.cos(2 * np.pi * x1)
y2 = y1-0.25
# sub.fill_between([0.25, 0.75], [-1.2, -1.2],
#                  [1.2, 1.2], color='yellow', alpha=0.5)
# sub.fill_between(x1, y1, y2, color='yellow', alpha=0.5)

sub.text(0.5, 0.5, r'$y=\cos (2 \pi X)$', fontsize=15,
         horizontalalignment='center',
         verticalalignment='center',
         transform=sub.transAxes,
         bbox=dict(edgecolor='green', facecolor='green', alpha=0.5))
sub.axhline(y=0, color='k', linewidth=0.5)

sub.set_ylim([-1.2, 1.2])
sub.set_xlabel(r'$x$', fontsize=15)
sub.set_ylabel(r'$y$', fontsize=15)

plt.show()
