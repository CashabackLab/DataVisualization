import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


def legend(
    ax,
    labels,
    colors,
    ncol=1,
    fontsize=6,
    linewidth=None,
    framealpha=0,
    loc="best",
    fontweight="bold",
    columnspacing=0,
    linestyle=None,
    lw=None,
    ls=None,
    handlestyle="bar",
    markersize=None,
    hollow_marker=False,
    handletextpad=None,
    handlelength=1,
    **kwargs # to pass to matplotlib legend call
):
    """
    Creates Custom colored legend. Markers can be the custom defined ones or matplotlib defaults. Latex math strings can also
    be used as markers. To use LaTeX use rich text (r"$ $") in math mode. 
    
    Parameters
    **kwargs: Additional keyword arguents to be passed to pyplot.legend()

    Returns a legend object
    """

    legend_count = len(labels)

    if len(colors) != legend_count:
        raise RuntimeError("Number of Labels should match number of Colors.")

    # Set default linewidth
    if lw == None and linewidth == None:
        linewidth = 4
    elif lw != None and linewidth == None:
        linewidth = lw

    # Set Default linestyle
    if ls == None and linestyle == None:
        linestyle = "-"
    elif ls != None and linestyle == None:
        linestyle = ls
    
    # Arg is not a list or array, so make it accordingly
    if not isinstance(linestyle, (list, np.ndarray)):
        linestyle = [linestyle] * legend_count

    if not isinstance(handlestyle, (list, np.ndarray)):
        handlestyle = [handlestyle] * legend_count

    if not isinstance(markersize, (list, np.ndarray)):
        markersize = [markersize] * legend_count

    # If arg was inputted as an array, we need to check the user inputted it correctly
    if len(handlestyle) != legend_count:
        raise RuntimeError("Number of HandleStyles should match number of Labels")
    
    if len(markersize) != legend_count:
        raise RuntimeError("Number of markersizes should match number of Labels")
    
    if len(linestyle) != legend_count:
        raise RuntimeError("Number of linestyles should match number of Labels")

    custom_handles = []

    for i in range(legend_count):

        curr_handle = handlestyle[i]
        curr_color = colors[i]

        # if a hollow marker is desired
        if hollow_marker:
            curr_facecolor = "none"
        else:
            curr_facecolor = curr_color
            
            
        curr_linestyle = linestyle[i]
        curr_markersize = markersize[i]

        if curr_handle in  ["bar","b"] :
            marker_style = None
            curr_markersize = None
            
            curr_linestyle = linestyle[i]
            curr_linecolor = curr_color
            curr_facecolor = "none"
            curr_edgecolor = "none"

            if hollow_marker:
                print("WARNING: Cannot use a hollow bar. Plotting a solid bar in legend.")

        elif curr_handle in ["o","circle"]:
            marker_style = "o"
            curr_linestyle = "none"
            
            curr_linecolor = "none"
            curr_edgecolor = curr_color

        # Legacy, for backwards compatibility
        elif curr_handle == "hollow_circle":
            marker_style = "o"
            curr_linestyle = "none"
            
            curr_linecolor = "none"
            curr_facecolor = "none"
            curr_edgecolor = curr_color
            
        # Legacy, for backwards compatibility   
        elif curr_handle in ["s",'square']:
            marker_style = "s"
            curr_linestyle = "none"
            curr_linecolor = "none"
            
            curr_edgecolor = curr_color
            
        else:
            print("NOTE: Marker not found in data vizualization. Using matplotlib markers.")
            marker_style = curr_handle
            curr_linestyle = "none"
            curr_linecolor = "none"
            
            curr_edgecolor = curr_color
        
        # "Hack": adding our marker by creating a 'non-plotted' artist to use normal matplotlib functionality in the
        # following ax.legend call.
        custom_handles.append(
            Line2D(
                [],
                [],
                color=curr_linecolor,
                marker=marker_style,
                markersize=curr_markersize,
                markerfacecolor=curr_facecolor,
                markeredgecolor=curr_edgecolor,
                ls=curr_linestyle,
                lw=linewidth,
            )
        )
    leg = ax.legend(
        custom_handles,
        labels,
        fontsize=fontsize,
        framealpha=framealpha,
        loc=loc,
        ncol=ncol,
        columnspacing=columnspacing,
        handletextpad=handletextpad,
        handlelength=handlelength,
        **kwargs
    )

    leg_text = leg.get_texts()
    for i, text in enumerate(leg_text):
        text.set_color(colors[i])
        text.set_weight(fontweight)

    return leg
