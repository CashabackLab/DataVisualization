import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import spearmanr
from matplotlib.lines import Line2D
from tqdm.notebook import tqdm
from PIL import Image

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

def Stat_Annotation(ax, x1, x2, y, p_val, effect_size = None, h = 0, color = "grey", lw = .7, fontsize = 6, exact_p = False):
    if p_val < 0.001 and not exact_p:
    
        if effect_size != None:
            ax.plot([x1, x1, x2, x2], [y, y, y, y], lw=lw, c=color)
            ax.text((x1+x2)*.5, y+h , f"p < 0.001, d = {abs(effect_size):.2f}", ha='center', va='bottom', color=color, fontsize = fontsize, weight = "bold")
        else:
            ax.plot([x1, x1, x2, x2], [y, y, y, y], lw=lw, c=color)
            ax.text((x1+x2)*.5, y+h , "p < 0.001", ha='center', va='bottom', color=color, fontsize = fontsize, weight = "bold")
            
    elif p_val > 0.001 or exact_p:
        if effect_size != None:
            ax.plot([x1, x1, x2, x2], [y, y, y, y], lw=lw, c=color)
            ax.text((x1+x2)*.5, y+h , f"p = {p_val:.3f}, d = {abs(effect_size):.2f}", ha='center', va='bottom', color=color, fontsize = fontsize, weight = "bold")
        else:
            ax.plot([x1, x1, x2, x2], [y, y, y, y], lw=lw, c=color)
            ax.text((x1+x2)*.5, y+h , f"p = {p_val:.3f}", ha='center', va='bottom', color=color, fontsize = fontsize, weight = "bold")
        
def set_Axes_Color(ax, color, **kwargs):
    '''
    Change axes color and set background to transparent
    if remove_spines = True, removes right and top spine
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
        

def gen_frame(path):
    """
    Input: path to image
    Generates the single frame of a gif from an image
    """
    im = Image.open(path)
    alpha = im.getchannel('A')

    # Convert the image into P mode but only use 255 colors in the palette out of 256
    im = im.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)

    # Set all pixel values below 128 to 255 , and the rest to 0
    mask = Image.eval(alpha, lambda a: 255 if a <=128 else 0)

    # Paste the color of index 255 and use alpha as a mask
    im.paste(255, mask)

    # The transparency index is 255
    im.info['transparency'] = 255

    return im

def Create_GIF(filename, path, num_images, duration = 66, loop = None):
    """
    Temporary files must have the same name with a number indicating frame number
    example: "filename_0.png"
    Parameters
    ----------
    filename : TYPE
        Name of temporary files to stitch together.
    path : TYPE
        path to temporary files.
    num_images : TYPE
        number of files to stitch together.
    duration : TYPE, optional
        GIF duration in milliseconds. The default is 66.
    loop : TYPE, optional
        Number of loops in the GIF. loop = 0 is infinite. The default is None (no loops).

    Returns
    -------
    None.

    """    
    frames = []
    
    print("Genrating Frame Data")
    for i in tqdm(range(num_images)):
        frames.append(gen_frame(path + f"{filename}_{i}.png"))
        
    print("Saving gif...")
    if loop is not None:
        frames[0].save(path + f"{filename}_Gif" + '.gif', save_all=True, append_images=frames[1:], loop=loop, duration=duration)
    else:
        frames[0].save(path + f"{filename}_Gif" + '.gif', save_all=True, append_images=frames[1:], duration=duration)
        
    print("Done.")
    
def plot_inset_image(ax, x_pos, y_pos, filename, img_height = 1, img_width = -1, format = "png", ignore_aspect = False):
    """
    Plot specified image on the given axis. 
    Only img_height or img_width is needed. img_width superceeds img_height
    Set ignore_aspect = True to use both
    Returns the inset axes image is plotted on
    """
    #read file in
    with mpl.cbook.get_sample_data(filename) as file:
        arr_image = plt.imread(file, format=format)
        
    #get aspect ratio
    aspect_ratio = arr_image.shape[1] / arr_image.shape[0]

    #if width and height are both positive and ignoring the aspect ratio
    if ignore_aspect and img_width > 0:
        axin = ax.inset_axes([x_pos, y_pos, img_width, img_height], transform=ax.transData)    # create new inset axes in data coordinates
        axin.imshow(arr_image, aspect = "auto")
        
    #If trying to ignore aspect ratio but no width is given
    elif ignore_aspect and img_width < 0:
        raise ValueError("Must specify img_width.")
    
    else:
        #If only height is given
        if img_width < 0:
            axin = ax.inset_axes([x_pos, y_pos, img_height * aspect_ratio, img_height], transform=ax.transData)    # create new inset axes in data coordinates
            axin.imshow(arr_image, aspect = "auto")
        #if width is given
        else:
            axin = ax.inset_axes([x_pos, y_pos, img_width, img_width / aspect_ratio], transform=ax.transData)    # create new inset axes in data coordinates
            axin.imshow(arr_image, aspect = "auto")
            
    return axin

def Pair_Plot(parameter_array, labels, **kwargs):
    """
    Plots distribution of parameters, with marginal distributions on the diagonal and joint
    distributions everywhere else.
    #optional parameters
        box_color          = kwargs.get("box_color", 'black')
        dot_color          = kwargs.get("dot_color", '#B2B1B3') #light grey
        cumulative_color   = kwargs.get("cumulative_color", "#218421") #dark green
        marginal_color     = kwargs.get("marginal_color", "#33cc33") #green
        legend_color       = kwargs.get("legend_color", "#218421") #dark green
        significance_color = kwargs.get("significance_color", '#33cc33') #green

        labelcolor       = kwargs.get("labelcolor", box_color)
        confidence_color = kwargs.get("confidence_color", '#727273') #dark grey

        show_cumulative   = kwargs.get("show_cumulative", True)
        show_significance = kwargs.get("show_significance", False)

        figsize = kwargs.get("figsize", (6, 6))
        dpi     = kwargs.get("dpi", 300)
        hspace  = kwargs.get("hspace", .1)
        wspace  = kwargs.get("wspace", .1)

        bins          = kwargs.get("bins", 25)
        tick_size     = kwargs.get("tick_size", 8)
        cumulative_lw = kwargs.get("cumulative_lw", 1.5)

        dot_alpha      = kwargs.get("dot_alpha", 1)
        marginal_alpha = kwargs.get("marginal_alpha", 1)
    """
    num_params = parameter_array.shape[1]

    #optional parameters
    box_color          = kwargs.get("box_color", 'black') 
    dot_color          = kwargs.get("dot_color", '#B2B1B3') #light grey
    cumulative_color   = kwargs.get("cumulative_color", "#218421") #dark green
    marginal_color     = kwargs.get("marginal_color", "#33cc33") #green
    legend_color       = kwargs.get("legend_color", "#218421") #dark green
    significance_color = kwargs.get("significance_color", '#33cc33') #green

    labelcolor       = kwargs.get("labelcolor", box_color)
    confidence_color = kwargs.get("confidence_color", '#727273')#dark grey

    show_cumulative   = kwargs.get("show_cumulative", True)
    show_significance = kwargs.get("show_significance", False)

    figsize = kwargs.get("figsize", (6, 6))
    dpi     = kwargs.get("dpi", 300)
    hspace  = kwargs.get("hspace", .1)
    wspace  = kwargs.get("wspace", .1)

    bins          = kwargs.get("bins", 25)
    tick_size     = kwargs.get("tick_size", 8)
    cumulative_lw = kwargs.get("cumulative_lw", 1.5)

    dot_alpha      = kwargs.get("dot_alpha", 1)
    marginal_alpha = kwargs.get("marginal_alpha", 1)
    
    if kwargs.get("black_background", False):
      dot_color = "w"
      box_color = "w"
      labelcolor = "w"
      confidence_color = "w"
    
    fontdict = dict(fontsize = tick_size, color = labelcolor)
    
    fig, ax = plt.subplots(nrows = num_params , ncols = num_params, dpi = dpi, figsize = figsize, gridspec_kw = dict(hspace = hspace, wspace = wspace))

    for row in range(num_params):
      for col in range(num_params):
          max_val = np.max(parameter_array[:, col])
          min_val = np.min(parameter_array[:, col])

          max_val += 0.005*max_val
          min_val -= 0.005*min_val

          ymax_val = np.max(parameter_array[:, row])
          ymin_val = np.min(parameter_array[:, row]) 

          ymax_val += 0.005*ymax_val
          ymin_val -= 0.005*ymin_val
        
          #Plot Marginal Distribution at the bottom of the figure
          if row == col:
              #Marginal
              values, base, tmp = ax[row, col].hist(parameter_array[:, col], bins = bins, density = True, color = marginal_color, zorder = 0, alpha = marginal_alpha)

              if show_cumulative:
                  #Plot cumulative behind the marginal
                  axin = ax[row, col].inset_axes([0, 0, 1, 1], zorder = 5)    # create new inset axes in axes coordinates
                  #evaluate the cumulative
                  cumulative = np.cumsum(values)
                  # plot the cumulative function
                  axin.plot(base[:-1], cumulative, c= cumulative_color, lw = cumulative_lw)
                  axin.patch.set_alpha(0)
                  axin.axis("off")
                  axin.set_xlim(min(base[:-1]), max(base[:-1]))
                  axin.set_ylim(min(cumulative), 1.025*max(cumulative) )

              #Plot 95% intervals
              sorted_arr = np.sort(parameter_array[:, col]) 
              low_end = sorted_arr[int(0.025 * sorted_arr.shape[0])]
              high_end = sorted_arr[int(0.975 * sorted_arr.shape[0])]
              ax[row, col].axvline(low_end, color = confidence_color, lw = cumulative_lw)
              ax[row, col].axvline(high_end, color = confidence_color, lw = cumulative_lw)
              #Set Border color
              set_Axes_Color(ax[row, col], box_color, remove_spines = True)

              ax[row, col].set_xlim(min_val, max_val)
            
          #Plot Joint Distributions
          else:
              #get rho and p_val
              rho, p_val = spearmanr(parameter_array[:, col], parameter_array[:, row])
              #If significant, color dots green and display stats
              if p_val < 0.05 :
                  ax[row, col].scatter(parameter_array[:, col], parameter_array[:, row], s = 1, lw = 0, color = dot_color, label = fr'$\rho = {rho:.3f}$', alpha = dot_alpha)
                  ax[row, col].set_xlim(min_val, max_val)

                  if p_val < 0.001: p_string = "p < 0.001"
                  else: p_string = f"p = {p_val:.3f}"
                    
                  if show_significance:
                    if row == col:
                        Custom_Legend(ax[row, col], [p_string, r'$\mathbf{\rho = }$' + f'{rho:.3f}'], [legend_color, legend_color], linewidth = 0, fontsize = 6,loc = "upper left", handlelength = 0, handletextpad = 0)
                    else:
                        Custom_Legend(ax[row, col], [p_string, r'$\mathbf{\rho = }$' + f'{rho:.3f}'], [legend_color, legend_color], linewidth = 0, fontsize = 6,loc = 0, handlelength = 0, handletextpad = -0)

                  set_Axes_Color(ax[row, col], box_color, remove_spines = True)
              #If not significant, grey out the dots
              else:
                  ax[row, col].scatter(parameter_array[:, col], parameter_array[:, row], s = 1, lw = 0, color = dot_color, alpha = dot_alpha)
                  ax[row, col].set_xlim(min_val, max_val)

                  set_Axes_Color(ax[row, col], box_color, remove_spines = True)

              xlims = ax[row, col].get_xlim()
              ylims = ax[row, col].get_ylim()

              ax[row, col].set_xlim(min_val, max_val)
              ax[row, col].set_ylim(ymin_val, ymax_val)

    ###############################################################################################################
    #Set labels and ticks
    for row in range(num_params):
      for col in range(num_params):

          #Set ylabels and ticks
          if col == 0 and row != 0: #Want to handle plot [0, 0] special later on
              ax[row, col].set_ylabel(labels[row], fontsize = 10, color = labelcolor)

              y_lims = ax[row, row].get_xlim()
              ax[row, col].set_ylim(y_lims)
              #setting yticklabels to 20% and 80% of limits
              ax[row, col].set_yticks([y_lims[0] + .2 * abs(y_lims[1] - y_lims[0]), y_lims[0] + .8*abs(y_lims[1] - y_lims[0])], fontsize = tick_size, fontcolor = "k")
              ax[row, col].set_yticklabels([f"{y_lims[0] + .2 * abs(y_lims[1] - y_lims[0]):.3f}", f"{y_lims[0] + .8*abs(y_lims[1] - y_lims[0]):.3f}"], fontdict = fontdict)

          else:
              ax[row, col].set_yticks([])

          #Set xlabels and ticks
          if row == num_params-1:
              ax[row, col].set_xlabel(labels[col], fontsize = 10, color = labelcolor)

              x_lims = ax[row, col].get_xlim()

              ax[row, col].set_xticks([x_lims[0] + .2 * abs(x_lims[1] - x_lims[0]), x_lims[0] + .8*abs(x_lims[1] - x_lims[0])], size = tick_size, fontcolor = "k")
              ax[row, col].set_xticklabels([f"{x_lims[0] + .2 * abs(x_lims[1] - x_lims[0]):.3f}", f"{x_lims[0] + .8*abs(x_lims[1] - x_lims[0]):.3f}"], fontdict = fontdict)

          else:
              ax[row, col].set_xticks([])


          #If at the bottom row, adjust the marginal distribution at [0, 0]
          if row == num_params-1 and col == 0:
              ax[0, 0].set_ylabel(labels[0], fontsize = 10, color = labelcolor)

              y_lims = ax[0, 0].get_ylim()
              new_ylims = ax[0, 1].get_ylim()

              ax[0, 0].set_yticks([y_lims[0] + .2 * abs(y_lims[1] - y_lims[0]), y_lims[0] + .8*abs(y_lims[1] - y_lims[0])])
              ax[0, 0].set_yticklabels([f"{new_ylims[0] + .2 * abs(new_ylims[1] - new_ylims[0]):.3f}", f"{new_ylims[0] + .8*abs(new_ylims[1] - new_ylims[0]):.3f}"], fontdict = fontdict)
    return fig, ax

