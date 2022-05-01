# 載入 matplotlib 模組
import matplotlib.pyplot as plt
import numpy as np
import datetime as date

# datetime 基礎操作
# dt = date.datetime(2020, 5, 9, 15, 51)
# dt0 = date.datetime(2020, 1, 1, 0, 0)
# dt1 = date.datetime(2020, 6, 9, 15, 51)
# # delta_t = dt-dt0

# # print(delta_t)
# # print(delta_t.total_seconds)

# delta_t = date.timedelta(hours=3, minutes=5, seconds=45)
# delta_t1 = date.timedelta(hours=3, minutes=5, seconds=45, microseconds=10)

# str_dt = dt.strftime('%Y/%m/%d %H:%M:%S')
# dt_str = '05/10/20--20:45:51.010000'
# dt2 = date.datetime.strptime(dt_str, '%m/%d/%y--%H:%M:%S.%f')

# # print(dt + delta_t)
# # print(dt > dt1)
# # print(delta_t1 > delta_t)
# # print(str_dt)
# print(dt2)

x = np.sin(2*np.pi * np.arange(0, 25)/25)

dt0 = date.datetime(2020, 5, 10, 0, 30)
dt1 = dt0 + date.timedelta(days=1, minutes=1)

dt_arr = (np.arange(dt0, dt1,
                    date.timedelta(hours=1))).astype(object)

fig = plt.figure()
sub = fig.add_subplot(1, 1, 1)
sub.plot(dt_arr, x)
sub.set_xlabel('time', fontsize=15)
sub.set_ylabel(r'$x$', fontsize=15)

xticks = (np.arange(dt0, dt1, date.timedelta(hours=6))).astype(object)
sub.set_xticks(xticks)

xticks_minor = (np.arange(dt0, dt1, date.timedelta(hours=1))).astype(object)
sub.set_xticks(xticks_minor, minor=True)

xticklabels = np.zeros(len(xticks), dtype=object)
for i in range(len(xticks)):
    xticklabels[i] = xticks[i].strftime('%H:%M')

sub.set_xticklabels(xticklabels)

sub.set_title(r'Teperatre on ' + dt0.strftime('%Y-%m-%d'), fontsize=15)

plt.show()
