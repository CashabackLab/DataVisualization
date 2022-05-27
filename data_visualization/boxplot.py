import matplotlib.pyplot as plt

def boxplot(data, **kwargs):
    box_lw       = kwargs.get("box_lw", 1.2)
    box_width    = kwargs.get("box_width", .5)
    whisker_lw   = kwargs.get("whisker_lw", 1.2)

    color = kwargs.get("color",   "#0BB8FD")
    x_pos = kwargs.get("x_pos", 0.25)
    ax = kwargs.get("ax", None)

    #box properties
    box_props   = {"facecolor": "none", "edgecolor" : color, "linewidth": box_lw, "alpha": 1}

    #whisker properties
    whisker_props = {"linewidth" : whisker_lw, "color": color}

    #cap properties
    cap_props = {"linewidth" : whisker_lw, "color": color}

    #median properties
    median_props = {"linewidth" : whisker_lw, "color": color}


    '''Make Box Plots'''
    if ax == None:
        plt.figure(dpi = 600, figsize = (2.25, 2.4))
        ax = plt.gca()
        ax.patch.set_alpha(0)
    else:
        ax.patch.set_alpha(0)
        
    #Left Box
    bp3 = ax.boxplot([data],   positions = [x_pos], patch_artist = True,  showfliers = False, 
                boxprops = box_props  , whiskerprops = whisker_props,
                capprops = cap_props, medianprops = median_props, widths = box_width)
    
    return ax
