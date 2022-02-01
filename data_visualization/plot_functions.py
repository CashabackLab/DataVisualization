import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from tqdm.notebook import tqdm
from PIL import Image

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
        
def set_Axes_Color(ax, color, remove_spines = False):
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
    ax.set_xticklabels(xticks)
    xticklabels = ax.xaxis.get_ticklabels() 
    ax.xaxis.set_ticklabels(xticklabels, color = color)
    
    #change ylabel color
    ylabel = ax.get_ylabel()
    ax.set_ylabel(ylabel, color = color)
    
    #change ytick label color
    yticks = ax.get_yticks()
    ax.set_yticklabels(yticks)
    yticklabels = ax.yaxis.get_ticklabels() 
    ax.yaxis.set_ticklabels(yticklabels, color = color)
    
    #set title color
    title = ax.get_title()
    ax.set_title(title, color = color)
    
    #set transparency
    ax.patch.set_alpha(0)
    
    #set axes colors
    for spine in spines: ax.spines[spine].set_color(color)
    
    #remove spines
    if remove_spines:
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
