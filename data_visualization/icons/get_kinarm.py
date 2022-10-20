import matplotlib.pyplot as plt
import os 
from PIL import Image
import PIL
import numpy as np

def get_kinarm(color = "light", robot = "endpoint", cropped_width = (0, 0), cropped_height = (0, 0)):
    """
    Returns kinarm exo or endpoint image
    color : {"light", "dark"}
    robot : {"exo", "endpoint"}
    cropped_width : tuple of percentages to crop image width
        ex: (.15, .1) removes 15% from left and 10% from right (recommended)
    cropped_height : tuple of percentages to crop image height
        ex: (0, .2) removes 0% from bottom and 20% from top (recommended)
    """
        
    if color not in ["light", "dark"]:
        raise ValueError("Color must be either light or dark.")
    if robot not in ["exo", "endpoint"]:
        raise ValueError("Robot must be either exo or endpoint.")
        
    fig = plt.figure(dpi = 300, figsize = (2, 2))
    ax = plt.gca()
    ax.set_position([0,0,1,1])
    
    fig.patch.set_color("none")
    ax.patch.set_color("none")
    
    head, tail = os.path.split(os.path.dirname(os.path.abspath(__file__)))
    filename = f"{robot}_{color}.png"
    
    img = Image.open(os.path.join(head, "images", filename))
    img = img.convert("RGBA")
    ax_img = ax.imshow(img)
        
    data = np.array(img)
    ax.set_xlim(cropped_width[0] * data.shape[1], data.shape[1] * (1-cropped_width[1]))
    ax.set_ylim(data.shape[0] * (1-cropped_height[0]), cropped_height[1] * data.shape[0])
    
    ax.axis("off")
    
    fig.canvas.draw() #draws the figure to create the renderer object
    
    #convert to Image object
    img = PIL.Image.frombytes('RGBA',
                              fig.canvas.get_width_height(),
                              np.asarray(fig.canvas.buffer_rgba()).take([0, 1, 2, 3], axis=2).tobytes())

    plt.close()
    return img
