# 載入 matplotlib 模組
from numpy.random import randn
import matplotlib.pyplot as plt
import numpy as np

# 基本操作指令
# plt.plot()
# plt.show()

# 創建 figure
fig = plt.figure()  # -->可以在括號內輸入尺寸plt.figure(figsize=[8, 4])
# ax1 = fig.add_subplot(2, 2, 1)  # (行,列,位置)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)

# x = np.linspace(-1, 1, 201)
# y = np.exp(-x**2/2)
# ax1.plot(x, y)

# 保存('路徑'), 保存('路徑',dpi=500)
# fig.savefig('./figure.jpg')

# fig.suptitle('Figure', fontsize=20)  # 添加總標題

# 高級設置
# plt.plot(randn(50).cumsum(), 'k--')  # 'k--': 線條形式
# _ = ax1.hist(randn(100), bins=20, color='k', alpha=0.3)
# ax2.scatter(np.arange(30), np.arange(30) + 3 * randn(30))

# linestyle: 線條形式('-'實線|'--'虛線|':'點線|'-.'虛點線)
# linewidth:線條粗細
# marker: 標出數據點('o'圓點|'s'方塊|'*'星號|'^'三角形), markersize調大小
# color: 顏色

ax = fig.add_subplot(1, 1, 1)
# ax.plot(randn(1000).cumsum())
ticks = ax.set_xticks([0, 250, 500, 750, 1000])  # 設置刻度
labels = ax.set_xticklabels(
    ['one', 'two', 'three', 'four', 'five'], rotation=30, fontsize='small')
ax.set_title('My first matplotlib plot')  # 添加標題
# fig.suptitle('Figure', fontsize=20)  # 添加總標題
ax.set_xlabel('Stages')  # 設置座標軸標籤,fontsize設置字體大小--> ('x',fontsize=14)

ax.plot(randn(1000).cumsum(), 'k', label='one')
ax.plot(randn(1000).cumsum(), 'k--', label='two')
ax.plot(randn(1000).cumsum(), 'k.', label='three')
ax.legend(loc='best')  # 圖例

plt.show()  # 查看
plt.close(fig)  # plt.close('all') 關閉所有
