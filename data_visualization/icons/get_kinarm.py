import matplotlib.pyplot as plt
import os 
from PIL import Image
import PIL

def get_kinarm(color = "light", robot = "endpoint", cropped = False, cropped_width = (.15, .1)):
    
    if color not in ["light", "dark"]:
        raise ValueError("Color must be either light or dark.")
    if robot not in ["exo", "endpoint"]:
        raise ValueError("Robot must be either exo or endpoint.")
        
    fig = plt.figure(dpi = 300, figsize = (2, 2))
    ax = plt.gca()
    ax.set_position([0,0,1,1])
    
    fig.patch.set_color("none")
    ax.patch.set_color("none")
    
    head, tail = os.path.split(os.path.abspath(__file__))
    filename = f"{robot}_{color}.png"
    
    img = Image.open(os.path.join(head, "images", filename))
    img = img.convert("RGBA")
    ax_img = ax.imshow(img)
    
    data = np.array(img)
    
    if cropped:
        ax.set_xlim(cropped_width[0] * data.shape[1], data.shape[1] * (1-cropped_width[1]))
    
    ax.axis("off")
    
    fig.canvas.draw() #draws the figure to create the renderer object
    
    #convert to Image object
    img = PIL.Image.frombytes('RGBA',
                              fig.canvas.get_width_height(),
                              np.asarray(fig.canvas.buffer_rgba()).take([0, 1, 2, 3], axis=2).tobytes())

    plt.close()
    return img
