from tqdm.notebook import tqdm
from PIL import Image
from .gen_frame import *

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
    
