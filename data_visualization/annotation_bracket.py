import matplotlib.pyplot as plt
import numpy as np

def square_brace(fig, ax, p1, p2, depth, c = 'black', padding = 0.15, **kwargs):
    '''Draws a square brace on axes in data coordinates. WILL WARP if aspect ratio of plot is off. 
    To show an unwarped bracket plot on an inset axes of a specified size in axes coordinates on 
    the desired axes, with a set aspect ratio, e.g.:

    x, y = 0.2, .5 # Note that coordinates aren't necessarily the center of the object
    size = 0.5
    inset = ax.inset_axes([x, y, size, size], transform = ax.transAxes)
    dv.square_brace(fig, inset,[.3, .5],[.6, .4], 0.1, linewidth = 2.5)
    inset.set_aspect("equal")
    inset.axis("off")
      
    
    Place a first and second prong of a specified depth.
        ax, axes to be plotted on
        p1, (x,y), first prong
        p2, (x,y), second prong
        depth, depth of the prongs, default is to "pull out" bracket to the left
        c, color
        padding, amount of padding around our bracket (wide line widths may be cropped)
        kwargs, dictionary to pass to plot calls'''

    # Doing some geometry to keep bracing lines perpendicular to the displacement line
    dx_d = abs(p1[0] - p2[0])
    dy_d = abs(p1[1] - p2[1])
    theta1 = np.arctan2(dx_d,dy_d)
    theta2 = abs(np.pi/2 - theta1)
    dx_1 = depth*np.sin(theta2)
    dy_1 = depth*np.cos(theta2)
    # getting the signs right on dx_1 and dx_2; geometry was done assuming 
    # x1<x2 and y1>y2, so here we correct for the cases when this isn't true
    if p1[0] > p2[0]:
        dy_1 = dy_1*-1
    if p1[1] < p2[1]:
        dy_1 = dy_1*-1


    ax.plot((p1[0], p1[0] - dx_1), (p1[1], p1[1] - dy_1), transform = ax.transData, color = c, **kwargs)
    ax.plot((p2[0], p2[0] - dx_1), (p2[1], p2[1] - dy_1), transform = ax.transData, color = c, **kwargs)
    ax.plot((p1[0] - dx_1, p2[0] - dx_1), (p1[1] - dy_1, p2[1] - dy_1), transform = ax.transData, color = c, **kwargs)

    y_big = np.max([p1[1], p2[1]])
    y_small = np.min([p1[1], p2[1]])
    x_big = np.max([p1[0], p2[0]])
    x_small = np.min([p1[0], p2[0]])
    ax.set_ylim(y_small- padding, y_big + padding)
    ax.set_xlim(x_small- padding, x_big + padding)
    ax.margins(0)

    return
