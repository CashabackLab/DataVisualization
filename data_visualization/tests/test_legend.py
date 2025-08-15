from data_visualization.legend import legend
import matplotlib.pyplot as plt
import numpy as np

fake_data1 = np.arange(0, 3, 1)
fake_data2 = np.arange(3, 6, 1)
fake_data3 = np.arange(6, 9, 1)
colors = ["blue", "orange", "green", "red"]
fig, ax = plt.subplots()

ax.bar(0, fake_data1, color=colors[0])
ax.bar(1, fake_data2, color=colors[1])
ax.bar(2, fake_data3, color=colors[2])
ax.bar(3, fake_data3, color=colors[3])

leg = legend(
    ax,
    labels=["Bar1", "Bar2", "Bar3", "Bar4"],
    colors=colors,
    handlestyle=["bar", "o", "x", "hollow_circle"],
)

plt.show()
