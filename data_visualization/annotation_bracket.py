import matplotlib.pyplot as plt
import numpy as np

def square_brace(fig, ax, p1, p2, depth, c = 'black', **kwargs):
    '''Draws a square brace in physical coordinates (e.g. inches, to maintain geometry) between the first 
    and second prong of a specified depth. The figure will warp if we plotted in axes coordinates because the figure
    itself could be, say, rectangular. Plotting in axes coordinates to avoid warping from changing limits:
        ax, axes to be plotted on
        p1, (x,y), first prong
        p2, (x,y), second prong
        depth, depth of the prongs, default is to "pull out" bracket to the left
        c, color
        kwargs, dictionary to pass to plot calls'''

    # Doing some geometry to keep bracing lines perpendicular to the displacement line
    dx_d = abs(p1[0] - p2[0])
    dy_d = abs(p1[1] - p2[1])
    theta1 = np.arctan2(dx_d,dy_d)
    # theta1 = np.arctan(dx_d/dy_d)
    theta2 = abs(np.pi/2 - theta1)
    dx_1 = depth*np.sin(theta2)
    dy_1 = depth*np.cos(theta2)
    # getting the signs right on dx_1 and dx_2; geometry was done assuming 
    # x1<x2 and y1>y2, so here we correct for the cases when this isn't true
    if p1[0] > p2[0]:
        dy_1 = dy_1*-1
    if p1[1] < p2[1]:
        dy_1 = dy_1*-1
        
    ax.plot((p1[0], p1[0] - dx_1), (p1[1], p1[1] - dy_1), transform = fig.dpi_scale_trans, color = c, **kwargs)
    ax.plot((p2[0], p2[0] - dx_1), (p2[1], p2[1] - dy_1), transform = fig.dpi_scale_trans, color = c, **kwargs)
    ax.plot((p1[0] - dx_1, p2[0] - dx_1), (p1[1] - dy_1, p2[1] - dy_1), transform = fig.dpi_scale_trans, color = c, **kwargs)

    # # plotting the dx and dy for testing:
    # ax.plot((p2[0], p2[0]), (p2[1], p2[1] - dy_1), color = 'orange', transform = fig.dpi_scale_trans, linewidth = 0.5) # from bottom point
    # ax.plot((p2[0], p2[0] - dx_1), (p2[1]- dy_1, p2[1]- dy_1), color = 'orange', transform = fig.dpi_scale_trans, linewidth = 0.5) # from bottom point

    
    return
