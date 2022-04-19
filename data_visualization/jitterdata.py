import matplotlib.pyplot as plt
import numpy as np

def jitterdata(ax, left_x, right_x, left_data, right_data, noise_scale, **kwargs):
    circle_size  = kwargs.get("circle_size", 8)
    circle_alpha = kwargs.get("circle_alpha", .8)
    
    for i in range(len(left_data)):
        noise = np.random.normal(0, noise_scale)

        ax.plot([left_x + noise, right_x + noise], [left_data[i], right_data[i]],
                 lw = .3, c = "#B2B1B3", alpha = circle_alpha, zorder = 0)

        ax.scatter([left_x + noise, right_x + noise], [left_data[i], right_data[i]],
                    s = circle_size, zorder = 0, facecolors = 'none',
                   edgecolors='grey', alpha = circle_alpha, lw = .5)
