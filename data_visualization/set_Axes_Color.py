import matplotlib as mpl
import matplotlib.pyplot as plt
        
def set_axes_color(ax, color, **kwargs):
    '''
    Change axes color and set background to transparent
    if remove_spines = True, removes right and top spine
    
    Kwargs
    kwargs.setdefault("default_xticklabels", False)
    kwargs.setdefault("leave_xticklabel_colors", False)
    kwargs.setdefault("default_yticklabels", False)
    kwargs.setdefault("leave_yticklabel_colors", False)
    '''
    
    return set_Axes_Color(ax, color, **kwargs)

def set_Axes_Color(ax, color, **kwargs):
    '''
    Change axes color and set background to transparent
    if remove_spines = True, removes right and top spine
    
    Kwargs
    kwargs.setdefault("default_xticklabels", False)
    kwargs.setdefault("leave_xticklabel_colors", False)
    kwargs.setdefault("default_yticklabels", False)
    kwargs.setdefault("leave_yticklabel_colors", False)
    '''
    spines = ["left", "bottom", "right", "top"]

    #Change xlabel color
    ax.tick_params(color = color)
    xlabel = ax.get_xlabel()
    ax.set_xlabel(xlabel, color = color)
    
    #change xtick label color
    xticks = ax.get_xticks()
    xticklabels = ax.xaxis.get_ticklabels()

    if kwargs.setdefault("default_xticklabels", False):
        xticklabels = [str(x) for x in xticks]
        
    if not kwargs.setdefault("leave_xticklabel_colors", False):
        ax.set_xticks(xticks, labels = xticklabels, color = color)
    else:
        ax.set_xticks(xticks, labels = xticklabels)
    
    #change ylabel color
    ylabel = ax.get_ylabel()
    ax.set_ylabel(ylabel, color = color)
    
    #change ytick label color
    yticks = ax.get_yticks()
    yticklabels = ax.get_yticklabels()
    
    if kwargs.setdefault("default_yticklabels", False):
        yticklabels = [str(y) for y in yticks]
            
    if not kwargs.setdefault("leave_yticklabel_colors", False):
        ax.set_yticks(yticks, labels = yticklabels, color = color)
    else:
        ax.set_yticks(yticks, labels = yticklabels)
    
    #set title color
    title = ax.get_title()
    ax.set_title(title, color = color)
    
    #set transparency
    ax.patch.set_alpha(0)
    
    #set axes colors
    for spine in spines: ax.spines[spine].set_color(color)
    
    #remove spines
    if kwargs.setdefault("remove_spines", False):
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        



