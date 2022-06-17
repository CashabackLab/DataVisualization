from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import PIL
import numpy as np
from .RotatingRectangle import RotatingRectangle

def get_short_rectangle(color, arrow_direction, height = 2, width = .9, arr_width = 0.2, figsize = (2, 2),
                        edge_width = 2, edge_color = "#727273", dim_len = 6.3, **kwargs):
    """
    Returns a short rectangle target PIL Image.
    Plottable using plt.imshow()
    
    Kwargs:
    rect_x = kwargs.get("rect_x", 0)
    rect_y = kwargs.get("rect_y", -1)
    """
    rect_x = kwargs.get("rect_x", 0)
    rect_y = kwargs.get("rect_y", -1)
    
    fig, ax = plt.subplots(figsize = figsize, dpi = 300)
    ax.set_aspect('equal')
    ax.set_position([0,0,1,1])

    ax.set_xlim([-dim_len, dim_len])
    ax.set_ylim([-dim_len, dim_len])
    ax.patch.set_alpha(0)
    point_of_rotation = np.array([width/2, height/2])  # B

    #Make the target
    r1 = RotatingRectangle((rect_x, rect_y), width=width, height=height, rel_point_of_rot=point_of_rotation,
                            angle=45, facecolor="white", alpha=1,
                           edgecolor = edge_color, linewidth = edge_width)
    ax.add_patch(r1)
    coords = r1.get_patch_transform().transform(r1.get_path().vertices[:-1])

    #make the arrow
    arr_color = color
    
    if arrow_direction.lower() == "extent":
        index1 = 2 # top right corner
        index2 = 1 #bottom right corner
        arr_shift = width * .75

        dx, dy = -coords[index2][0] + coords[index1][0], -coords[index2][1] + coords[index1][1]
        plt.arrow(coords[index2][0]+ arr_shift, coords[index2][1]+ arr_shift, dx, dy,
                   facecolor = arr_color, edgecolor = arr_color, width = arr_width)
        plt.arrow(coords[index1][0]+ arr_shift, coords[index1][1]+ arr_shift, -dx, -dy,
                   facecolor = arr_color, edgecolor = arr_color, width = arr_width)

    elif arrow_direction.lower() == "aim":
        index1 = 2 # top right corner
        index2 = 3 #bottom right corner
        
        arr_shift = width * .75

        dx, dy = -coords[index2][0] + coords[index1][0], -coords[index2][1] + coords[index1][1]
        plt.arrow(coords[index2][0] - arr_shift, coords[index2][1]+ arr_shift, dx, dy,
                   facecolor = arr_color, edgecolor = arr_color, width = arr_width)
        plt.arrow(coords[index1][0]- arr_shift, coords[index1][1]+ arr_shift, -dx, -dy,
                   facecolor = arr_color, edgecolor = arr_color, width = arr_width)

    else:
        pass
    
    plt.axis("off")
    
    fig.canvas.draw() #draws the figure to create the renderer object
    
    #convert to Image object
    img = PIL.Image.frombytes('RGB', fig.canvas.get_width_height(),fig.canvas.tostring_rgb())
    plt.close() #close figure
    
    return img
