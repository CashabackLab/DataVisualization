import matplotlib.pyplot as plt
import numpy as np

def jitterdata(ax, left_x, right_x, left_data, right_data, noise_scale, **kwargs):
    """
    Plots individual connecting data with a gaussian jitter. 
    noise_scale sets the magnitude of the jitter
    
    Optional Arguments:
    circle_size  = kwargs.get("circle_size", 8)
    circle_alpha = kwargs.get("circle_alpha", .8)
    include_mean = kwargs.get("include_mean", True)
    linewidth    = kwargs.get("linewidth", None) #same as lw
    lw           = kwargs.get("lw", None)        #same as linewidth
    data_color   = kwargs.get("data_color", "grey")
    data_edge_color = kwargs.get("data_edge_color", "grey")
    mean_color   = kwargs.get("mean_color", '#727273')
    mean_edge_color = kwargs.get("mean_edge_color", "#727273")
    circle_lw    = kwargs.get("circle_lw", 0.5)
    """
    circle_size  = kwargs.get("circle_size", 8)
    circle_alpha = kwargs.get("circle_alpha", .8)
    include_mean = kwargs.get("include_mean", True)
    linewidth    = kwargs.get("linewidth", None) #same as lw
    lw           = kwargs.get("lw", None)        #same as linewidth
    data_color   = kwargs.get("data_color", "grey")
    data_edge_color = kwargs.get("data_edge_color", "grey")
    mean_color   = kwargs.get("mean_color", '#727273')
    mean_edge_color = kwargs.get("mean_edge_color", "#727273")
    circle_lw    = kwargs.get("circle_lw", 0.5)

    if linewidth == None and lw == None:
        lw = 0.3
    elif linewidth != None:
        lw = linewidth
    
    #plot individual datapoints
    for i in range(len(left_data)):
        noise = np.random.normal(0, noise_scale)

        ax.plot([left_x + noise, right_x + noise], [left_data[i], right_data[i]],
                 lw = lw, c = data_edge_color, alpha = circle_alpha, zorder = 0)

        ax.scatter([left_x + noise, right_x + noise], [left_data[i], right_data[i]],
                    s = circle_size, zorder = 0, facecolors = 'none',
                   edgecolors=data_color, alpha = circle_alpha, lw = circle_lw)
        
    #Plot mean datapoints
    if include_mean:
        ax.plot([left_x, right_x], [np.nanmean(left_data), np.nanmean(right_data)],
                     lw = 2*lw, c = mean_color, alpha = 1, zorder = 0)

        ax.scatter([left_x , right_x], [np.nanmean(left_data), np.nanmean(right_data)],
                    s = circle_size, zorder = 0, facecolors = mean_color,
                   edgecolors=mean_color, alpha = 1, lw = circle_lw)
