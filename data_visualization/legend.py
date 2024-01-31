import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

def legend(ax, labels, colors, ncol = 1,
            fontsize = 6, linewidth = None, 
            framealpha = 0, loc = "best", fontweight = "bold",
            columnspacing = 0, linestyle = None, lw = None, 
            ls = None, handlestyle="bar", markersize=None, **kwargs):
    """
    Creates Custom colored legend
    Parameters
    **kwargs: Additional keyword arguents to be passed to pyplot.legend()
    
    Returns a legend object
    """
    
    if len(labels) != len(colors):
        raise RuntimeError("Number of Labels should match number of Colors.")
        
    if lw == None and linewidth == None:
        linewidth = 4
    elif lw != None and linewidth == None:
        linewidth = lw
        
    if ls == None and linestyle == None:
        linestyle = "-"
    elif ls != None and linestyle == None:
        linestyle = ls
        
    if not isinstance(linestyle,(list, np.ndarray)):
        linestyle = [linestyle]*len(colors)        
    
    custom_handles = []            
    if handlestyle == "bar":
        for i,color in enumerate(colors):
            custom_handles.append(Line2D([0], [0], color=color, 
                                         lw=linewidth, ls = linestyle[i]))
    elif handlestyle == "circle":
        for i,color in enumerate(colors):
            custom_handles.append(Line2D([], [], marker='o', markersize=markersize, 
                                         markerfacecolor=color, markeredgecolor=color, 
                                         ls="none", lw=linewidth))
            
    leg = ax.legend(custom_handles, labels, fontsize = fontsize,
             framealpha = framealpha, loc = loc, ncol = ncol, 
             columnspacing = columnspacing, **kwargs)
    
    leg_text = leg.get_texts()
    for i, text in enumerate(leg_text):
        text.set_color(colors[i])
        text.set_weight(fontweight)
        
    return leg
