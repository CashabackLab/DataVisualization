import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def custom_legend(ax, labels: "List[String]", colors : "List of color names", ncol = 1,
                 fontsize = 6, linewidth = 4, framealpha = 0, loc = "best", fontweight = "bold",
                 columnspacing = 0, **kwargs):
    """
    Creates Custom colored legend

    Parameters
    ----------
    ax : MPL Ax Object
    labels : "List[Strings]"
    colors : "List of color names"
    ncol : TYPE, optional
    The default is 1.
    fontsize : TYPE, optional
     The default is 6.
    linewidth : TYPE, optional
     The default is 4.
    framealpha : TYPE, optional
    The default is 0.
    loc : TYPE, optional
    The default is "best".
    fontweight : TYPE, optional
    The default is "bold".
    columnspacing : TYPE, optional
     The default is 0.
    **kwargs: Additional keyword arguents to be passed to pyplot.legend()

    Returns
    -------
    leg : Matplotlib Legend Object
    DESCRIPTION.

    """
    #Alias for Custom_Legend
    return_val = Custom_Legend(ax, labels, colors , ncol = ncol, fontsize = fontsize, \
                           linewidth = linewidth, framealpha = framealpha, loc = loc, \
                           fontweight = fontweight, columnspacing = columnspacing, **kwargs)
    return return_val
  
def customlegend(ax, labels: "List[String]", colors : "List of color names", ncol = 1,
                 fontsize = 6, linewidth = 4, framealpha = 0, loc = "best", fontweight = "bold",
                 columnspacing = 0, **kwargs):
    """
    Creates Custom colored legend

    Parameters
    ----------
    ax : MPL Ax Object
    labels : "List[Strings]"
    colors : "List of color names"
    ncol : TYPE, optional
    The default is 1.
    fontsize : TYPE, optional
     The default is 6.
    linewidth : TYPE, optional
     The default is 4.
    framealpha : TYPE, optional
    The default is 0.
    loc : TYPE, optional
    The default is "best".
    fontweight : TYPE, optional
    The default is "bold".
    columnspacing : TYPE, optional
     The default is 0.
    **kwargs: Additional keyword arguents to be passed to pyplot.legend()

    Returns
    -------
    leg : Matplotlib Legend Object
    DESCRIPTION.

    """
    #Alias for Custom_Legend
    return_val = Custom_Legend(ax, labels, colors , ncol = ncol, fontsize = fontsize, \
                           linewidth = linewidth, framealpha = framealpha, loc = loc, \
                           fontweight = fontweight, columnspacing = columnspacing, **kwargs)
    return return_val
  
def Custom_Legend(ax, labels: "List[String]", colors : "List of color names", ncol = 1,
                 fontsize = 6, linewidth = 4, framealpha = 0, loc = "best", fontweight = "bold",
                 columnspacing = 0, **kwargs):
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
    **kwargs: Additional keyword arguents to be passed to pyplot.legend()

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
             framealpha = framealpha, loc = loc, ncol = ncol, columnspacing = columnspacing, **kwargs)
    
    leg_text = leg.get_texts()
    for i, text in enumerate(leg_text):
        text.set_color(colors[i])
        text.set_weight(fontweight)
        
    return leg
