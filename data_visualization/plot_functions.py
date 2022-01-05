import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

def Custom_Legend(ax, labels: "List[String]", colors : "List of color names", ncol = 1,
                 fontsize = 6, linewidth = 4, framealpha = 0, loc = "best", fontweight = "bold",
                 columnspacing = 0):
    """
    Creates Custom colored legend

    Parameters
    ----------
    ax : MPL Ax Object
        DESCRIPTION.
    labels : "List[Strings]"
        DESCRIPTION.
    colors : "List of color names"
        DESCRIPTION.
    ncol : TYPE, optional
        DESCRIPTION. The default is 1.
    fontsize : TYPE, optional
        DESCRIPTION. The default is 6.
    linewidth : TYPE, optional
        DESCRIPTION. The default is 4.
    framealpha : TYPE, optional
        DESCRIPTION. The default is 0.
    loc : TYPE, optional
        DESCRIPTION. The default is "best".
    fontweight : TYPE, optional
        DESCRIPTION. The default is "bold".
    columnspacing : TYPE, optional
        DESCRIPTION. The default is 0.

    Returns
    -------
    leg : Matplotlib Legend Object
        DESCRIPTION.

    """
    
    if len(labels) != len(colors):
        raise RuntimeError("Number of Labels should match number of Colors.") 
        
    custom_lines = []
    for color in colors:
        custom_lines.append(Line2D([0], [0], color=color, lw=linewidth))

    leg = ax.legend(custom_lines, labels, fontsize = fontsize,
             framealpha = framealpha, loc = loc, ncol = ncol, columnspacing = columnspacing)
    
    leg_text = leg.get_texts()
    for i, text in enumerate(leg_text):
        text.set_color(colors[i])
        text.set_weight(fontweight)
        
    return leg

def Stat_Annotation(ax, x1, x2, y, p_val, effect_size = None, h = 0, color = "grey", lw = .7, fontsize = 6):
    if effect_size != None:
        ax.plot([x1, x1, x2, x2], [y, y, y, y], lw=lw, c=color)
        ax.text((x1+x2)*.5, y+h , f"p = {p_val:.3f}, d = {abs(effect_size):.2f}", ha='center', va='bottom', color=color, fontsize = fontsize, weight = "bold")
    else:
        ax.plot([x1, x1, x2, x2], [y, y, y, y], lw=lw, c=color)
        ax.text((x1+x2)*.5, y+h , f"p = {p_val:.3f}", ha='center', va='bottom', color=color, fontsize = fontsize, weight = "bold")
        
def set_mpl_font_defaults(mpl, SMALLEST_SIZE = 6, SMALL_SIZE = 8,  MEDIUM_SIZE = 8,  BIGGER_SIZE = 14):
  """
  EXPERIMENTAL FUNCTION
  Input: Local instance of matplotlib
  Description: sets default plot specifications
  """
  #Set Default Plot Fontsize
  
  mpl.pyplot.rc('font', size        = SMALL_SIZE)          # controls default text sizes
  mpl.pyplot.rc('axes', titlesize   = SMALL_SIZE)     # fontsize of the axes title
  mpl.pyplot.rc('axes', labelsize   = MEDIUM_SIZE)    # fontsize of the x and y labels
  mpl.pyplot.rc('xtick', labelsize  = SMALL_SIZE)    # fontsize of the tick labels
  mpl.pyplot.rc('ytick', labelsize  = SMALL_SIZE)    # fontsize of the tick labels
  mpl.pyplot.rc('legend', fontsize  = SMALL_SIZE)    # legend fontsize
  mpl.pyplot.rc('figure', titlesize = BIGGER_SIZE)  # fontsize of the figure title
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
