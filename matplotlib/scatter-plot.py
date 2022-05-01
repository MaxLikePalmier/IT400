from cmath import pi
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

data_LA = pd.read_csv('LATemperature2019.csv')
data_NY = pd.read_csv('NYTemperature2019.csv')

# process LA data
date_LA_str = data_LA['DATE'].to_numpy()
TAVG_LA = data_LA['TAVG'].to_numpy()

nrec = len(TAVG_LA)

date_LA = np.zeros(nrec, dtype=object)

for i in range(nrec):
    date_LA[i] = datetime.strptime(date_LA_str[i], '%Y-%m-%d')

doy_LA = np.zeros(nrec)
for i in range(nrec):
    # if i == 0:
    #     print(date_LA[i].timetuple())
    doy_LA[i] = date_LA[i].timetuple().tm_yday

# sort the data according to time
argsort_idx = np.argsort(doy_LA)

doy_LA = doy_LA[argsort_idx]
TAVG_LA = TAVG_LA[argsort_idx]

# process NY data
date_NY_str = data_NY['DATE'].to_numpy()
TAVG_NY = data_NY['TAVG'].to_numpy()

nrec = len(TAVG_NY)

date_NY = np.zeros(nrec, dtype=object)

for i in range(nrec):
    date_NY[i] = datetime.strptime(date_NY_str[i], '%Y-%m-%d')

doy_NY = np.zeros(nrec)
for i in range(nrec):
    # if i == 0:
    #     print(date_NY[i].timetuple())
    doy_NY[i] = date_NY[i].timetuple().tm_yday

# sort the data according to time
argsort_idx = np.argsort(doy_NY)

doy_NY = doy_NY[argsort_idx]
TAVG_NY = TAVG_NY[argsort_idx]

# plot----------------
fig = plt.figure()
sub = fig.add_subplot(1, 1, 1)

# directly plot
# sub.plot(TAVG_LA, TAVG_NY, linestyle='none', marker='o')

# use scatter
scat = sub.scatter(TAVG_LA, TAVG_NY, marker='o', c=doy_NY, cmap='twilight',
                   s=1 + 12 * np.sin(np.pi * np.linspace(0, 1, len(TAVG_NY))))

cb = fig.colorbar(scat, shrink=0.75, aspect=12, ticks=np.arange(0, 365, 30,dtype=int))
cb.ax.set_ylabel('day of year', fontsize=15)

sub.set_xlabel(r'Temperature LA', fontsize=15)
sub.set_ylabel(r'Temperature NY', fontsize=15)
sub.set_xlim([5, 30])
sub.set_ylim([-15, 35])

plt.show()
