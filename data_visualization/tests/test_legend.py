from data_visualization.legend import legend
import matplotlib.pyplot as plt
import numpy as np

fake_data1 = np.arange(0,3,1)
fake_data2 = np.arange(3,6,1)
fake_data3 = np.arange(6,9,1)

fig,ax = plt.subplots()

ax.bar(0, fake_data1)
ax.bar(1, fake_data2)
ax.bar(2, fake_data3)

leg = legend(ax, labels=["Bar1", "Bar2", "Bar3"], colors=["blue", "orange", "green"], handlestyle=["bar", "o", "x"])

plt.show()




