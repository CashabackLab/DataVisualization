import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

def legend(ax, labels, colors, ncol = 1,
            fontsize = 6, linewidth = None, 
            framealpha = 0, loc = "best", fontweight = "bold",
            columnspacing = 0, linestyle = None, lw = None, 
            ls = None, handlestyle="bar", markersize=None, handletextpad=None, **kwargs):
    """
    Creates Custom colored legend
    Parameters
    **kwargs: Additional keyword arguents to be passed to pyplot.legend()
    
    Returns a legend object
    """
        
    legend_count = len(labels)
                        
    if len(colors) != legend_count:
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
        linestyle = [linestyle]*legend_count
    
    if not isinstance(handlestyle,(list,np.ndarray)):
        handlestyle = [handlestyle]*legend_count
    
    if len(handlestyle) != legend_count:
        raise RuntimeError("Number of HandleStyles should match number of Labels")
        
    if not isinstance(markersize,(list,np.ndarray)):
        markersize = [markersize]*legend_count

    if len(markersize) != legend_count:
        raise RuntimeError("Number of markersizes should match number of Labels")
                
    print(markersize)
    custom_handles = []            
    
    for i in range(legend_count):
        
        
        curr_handle = handlestyle[i]
        curr_color = colors[i]
        curr_linestyle = linestyle[i]
        curr_markersize = markersize[i]
        
        
        if curr_handle == "bar":
            marker_style = None
            curr_markersize = None
            curr_linestyle = linestyle[i]
            
            curr_linecolor = curr_color
            curr_facecolor = None
            curr_edgecolor = None

        elif curr_handle == "o":
            marker_style = "o"
            if handletextpad is None:
                handletextpad = 0
            curr_linestyle = "none"
            
            curr_linecolor = "none"
            curr_facecolor = curr_color
            curr_edgecolor = curr_color
            
        elif curr_handle == "circle":
            marker_style = "o"
            if handletextpad is None:
                handletextpad = 0
            curr_linestyle = "none"

            curr_linecolor = "none"
            curr_facecolor = curr_color
            curr_edgecolor = curr_color

        elif curr_handle == "x":
            marker_style = "x"
            if handletextpad is None:
                handletextpad = 0
            curr_linestyle = "none"

            curr_linecolor = "none"
            curr_facecolor = curr_color
            curr_edgecolor = curr_color
            
        elif  curr_handle == "hollow circle":
            
            marker_style = "o"
            if handletextpad is None:
                handletextpad = 0
            curr_linestyle = "none"
            
            curr_linecolor = "none"
            curr_facecolor = "none"
            curr_edgecolor = curr_color

        custom_handles.append(Line2D([], [], marker=marker_style, markersize=curr_markersize, 
                                     markerfacecolor=curr_facecolor, markeredgecolor=curr_edgecolor, 
                                     ls=curr_linestyle, lw=linewidth))
        
        
            
    leg = ax.legend(custom_handles, labels, fontsize = fontsize,
             framealpha = framealpha, loc = loc, ncol = ncol, 
             columnspacing = columnspacing, handletextpad=handletextpad, **kwargs)
    
    leg_text = leg.get_texts()
    for i, text in enumerate(leg_text):
        text.set_color(colors[i])
        text.set_weight(fontweight)
        
    return leg
