import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

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
            #width, height of generated figure
            fig_dimensions = (img_height * aspect_ratio, img_height)
        #if width is given
        else:
            axin = ax.inset_axes([x_pos, y_pos, img_width, img_width / aspect_ratio], transform=ax.transData)    # create new inset axes in data coordinates
            axin.imshow(arr_image, aspect = "auto")
            #width, height of generated figure
            fig_dimensions = (img_width, img_width / aspect_ratio)
    
    return axin, fig_dimensions
