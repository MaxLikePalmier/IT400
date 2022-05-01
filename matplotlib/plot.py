# 載入 matplotlib 模組
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 100)
y = 10 * x
y2 = 8 * x
y3 = 10 - 5 * x

fig = plt.figure()
sub = fig.add_subplot(1, 1, 1)

line1, = sub.plot(x, y, label=r'$y=10x$')
line2, = sub.plot(x, y2, label=r'$y=8x$')
line3, = sub.plot(x, y3, label=r'$y=10-5x$')

sub.axhline(y=4, color='red')
sub.axvline(x=0.8, color='blue', linestyle='-.')

leg1 = sub.legend(handles=[line1, line3])
sub.add_artist(leg1)
sub.legend(handles=[line2], loc='lower center')

sub.set_xlabel(r'$x$', fontsize=15)
sub.set_ylabel(r'$y$', fontsize=15)

sub.set_xticks([0, 0.5, 1.0])
sub.set_xticks(np.arange(0, 1.01, 0.1), minor=True)
# sub.set_xticklabels(['a', 'b', 'c', ])

sub.grid(linestyle='--', which='both')  # 設置網格 (which='both') 沿主刻度與副刻度畫線
sub.tick_params(axis='x', which='major', direction='inout',
                length=5, pad=10, labelsize=14, colors='C1', rotation=45, grid_alpha=0.5)

plt.show()  # 查看
