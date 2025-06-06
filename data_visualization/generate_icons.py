from PIL import Image
import os

def hex_to_rgb( hex_code, normalize = False):
        """
        Input: Hex String
        Output: integer RGB values
        """
        hex_code = hex_code.lstrip("#")
        RGB_vals = tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))
        
        if normalize: 
            RGB_vals = (RGB_vals[0] / 255, RGB_vals[1] / 255, RGB_vals[2] / 255)
        
        return RGB_vals
    
def blend_colors(colorRGBA1, colorRGBA2):
    """
    Blends two RGBA tuples evenly
    """
    red   = (colorRGBA1[0] * (255 - 128) + colorRGBA2[0] * 128) / 255
    green = (colorRGBA1[1] * (255 - 128) + colorRGBA2[1] * 128) / 255
    blue  = (colorRGBA1[2] * (255 - 128) + colorRGBA2[2] * 128) / 255
    return (int(red), int(green), int(blue), 255)

def get_healthy_icon(color = "#000000"):
    fileName = "Young"
    pic_format = "png"
    new_color = color #change this to desired color
    
    path = os.path.dirname(os.path.realpath(__file__)) # getting full parent directory (no wildcards) of current module (file)
    filepath = os.path.join(path, "images", fileName)
    img = Image.open(filepath + '.' + pic_format)
    img = img.convert("RGBA")
    datas = img.getdata()

    new_color = hex_to_rgb(new_color)

    newData = []

    for i, item in enumerate(datas):
        if item[3] < 0.1:
            newData.append((255, 255, 255, 0))
        else:
            newData.append((new_color[0], new_color[1], new_color[2], 255))

    img.putdata(newData)
    return img

def get_elderly_icon(color = "#000000"):
    fileName = "Elderly"
    pic_format = "png"
    new_color = color #change this to desired color

    path = os.path.dirname(os.path.realpath(__file__)) # getting full parent directory (no wildcards) of current module (file)
    filepath = os.path.join(path, "images", fileName)
    img = Image.open(filepath + '.' + pic_format)
    img = img.convert("RGBA")
    datas = img.getdata()

    new_color = hex_to_rgb(new_color)

    newData = []

    for i, item in enumerate(datas):
        if item[3] < 0.1:
            newData.append((255, 255, 255, 0))
        else:
            newData.append((new_color[0], new_color[1], new_color[2], 255))

    img.putdata(newData)
    return img

def get_foot_icon(color = "#000000", filled = False):
    if not filled: fileName = "Barefoot_2"
    else: fileName = "Barefoot_Solid"
    pic_format = "png"
    new_color = color #change this to desired color

    path = os.path.dirname(os.path.realpath(__file__)) # getting full parent directory (no wildcards) of current module (file)
    filepath = os.path.join(path, "images", fileName)
    img = Image.open(filepath + '.' + pic_format)
    img = img.convert("RGBA")
    datas = img.getdata()

    new_color = hex_to_rgb(new_color)

    newData = []

    for i, item in enumerate(datas):
        if item[0] >= 230 and item[1] >= 230 and item[2] >= 230:
            newData.append((255, 255, 255, 0))
        else:
            newData.append((new_color[0], new_color[1], new_color[2], 255))

    img.putdata(newData)
    return img

def get_walking_icon(color = "#000000"):
    fileName = "Man_Walking"
    pic_format = "png"
    new_color = color #change this to desired color

    path = os.path.dirname(os.path.realpath(__file__)) # getting full parent directory (no wildcards) of current module (file)
    filepath = os.path.join(path, "images", fileName)
    img = Image.open(filepath + '.' + pic_format)
    img = img.convert("RGBA")
    datas = img.getdata()

    new_color = hex_to_rgb(new_color)

    newData = []

    for i, item in enumerate(datas):
        if item[0] >= 245 and item[1] >= 245 and item[2] >= 245:
            newData.append((255, 255, 255, 0))
        else:
            newData.append((new_color[0], new_color[1], new_color[2], 255))

    img.putdata(newData)
    return img

def get_open_hand_icon(color = "#000000"):
    fileName = "Open_Hand"
    pic_format = "png"
    new_color = color #change this to desired color

    path = os.path.dirname(os.path.realpath(__file__)) # getting full parent directory (no wildcards) of current module (file)
    filepath = os.path.join(path, "images", fileName)
    img = Image.open(filepath + '.' + pic_format)
    img = img.convert("RGBA")
    datas = img.getdata()

    new_color = hex_to_rgb(new_color)

    newData = []

    for i, item in enumerate(datas):
        if item[0] >= 245 and item[1] >= 245 and item[2] >= 245 or item[3] < 1:
            newData.append((255, 255, 255, 0))
        else:
            newData.append((new_color[0], new_color[1], new_color[2], 255))

    img.putdata(newData)
    return img

def get_hand_icon(color = "#000000", filled = False):
    if not filled: fileName = "Hand_icon"
    else: fileName = "Hand_icon_filled"
    pic_format = "png"
    new_color = color #change this to desired color

    path = os.path.dirname(os.path.realpath(__file__)) # getting full parent directory (no wildcards) of current module (file)
    filepath = os.path.join(path, "images", fileName)
    img = Image.open(filepath + '.' + pic_format)
    img = img.convert("RGBA")
    datas = img.getdata()

    new_color = hex_to_rgb(new_color)

    newData = []

    for i, item in enumerate(datas):
        if item[0] >= 245 and item[1] >= 245 and item[2] >= 245 or item[3] < 1:
            newData.append((255, 255, 255, 0))
        else:
            newData.append((new_color[0], new_color[1], new_color[2], 255))

    img.putdata(newData)
    return img

def get_sight_icon(color = "#000000"):
    """
    Returns a Sight icon image in the given color.
    Color must be in Hex Code
    """
    
    fileName = "Sight"
    pic_format = "png"
    new_color = color #change this to desired color

    path = os.path.dirname(os.path.realpath(__file__)) # getting full parent directory (no wildcards) of current module (file)
    filepath = os.path.join(path, "images", fileName)
    img = Image.open(filepath + '.' + pic_format)
    img = img.convert("RGBA")
    datas = img.getdata()

    new_color = hex_to_rgb(new_color)

    newData = []

    for i, item in enumerate(datas):
        if item[0] >= 245 and item[1] >= 245 and item[2] >= 245:
            newData.append((255, 255, 255, 0))
        else:
            newData.append((new_color[0], new_color[1], new_color[2], 255))

    img.putdata(newData)
    return img

def get_curlybrace_icon(color = "#000000"):
    """
    Color must be in Hex Code
    """
    
    fileName = "CurlyBrace"
    pic_format = "png"
    new_color = color #change this to desired color

    path = os.path.dirname(os.path.realpath(__file__)) # getting full parent directory (no wildcards) of current module (file)
    filepath = os.path.join(path, "images", fileName)
    img = Image.open(filepath + '.' + pic_format)
    img = img.convert("RGBA")
    datas = img.getdata()

    new_color = hex_to_rgb(new_color)

    newData = []

    for i, item in enumerate(datas):
        if item[0] >= 245 and item[1] >= 245 and item[2] >= 245:
            newData.append((255, 255, 255, 0))
        else:
            newData.append((new_color[0], new_color[1], new_color[2], 255))

    img.putdata(newData)
    return img

def get_reward_icon(color = "#000000"):
    """
    Returns a Reward Sound Icon in the given color.
    Color must be in hex code.
    """
    
    fileName = "Reward_Sound"
    pic_format = "png"
    new_color = color #change this to desired color

    path = os.path.dirname(os.path.realpath(__file__)) # getting full parent directory (no wildcards) of current module (file)
    filepath = os.path.join(path, "images", fileName)
    img = Image.open(filepath + '.' + pic_format)
    img = img.convert("RGBA")
    datas = img.getdata()

    new_color = hex_to_rgb(new_color)

    newData = []

    for i, item in enumerate(datas):
        if item[0] >= 245 and item[1] >= 245 and item[2] >= 245:
            newData.append((255, 255, 255, 0))
        elif item[0] < 132:
            newData.append((new_color[0], new_color[1], new_color[2], 255))
        else:
            newData.append(blend_colors(new_color, (255, 255, 255)))

    img.putdata(newData)
    return img

def get_punishment_icon(color = "#000000"):
    """
    Returns a Punishment Sound Icon in the given color.
    Color must be in hex code. Defaults new color to black: #000000. Removes 
    """
    
    fileName = "Punishment_Sound"
    pic_format = "png"
    new_color = color #change this to desired color

    path = os.path.dirname(os.path.realpath(__file__)) # getting full parent directory (no wildcards) of current module (file)
    filepath = os.path.join(path, "images", fileName)
    img = Image.open(filepath + '.' + pic_format)
    img = img.convert("RGBA")
    datas = img.getdata()

    new_color = hex_to_rgb(new_color)

    newData = []

    for i, item in enumerate(datas):
        # If close to white, sets to white, and then makes that value
        # "transparent".
        if item[0] >= 245 and item[1] >= 245 and item[2] >= 245:
            newData.append((255, 255, 255, 0))
        # If the R value is "darker" will completely replace with new color
        elif item[0] < 132: # fidget value (found by trial and error)
            newData.append((new_color[0], new_color[1], new_color[2], 255))
        # Blends new color with white (for interior of speaker)
        else:
            newData.append(blend_colors(new_color, (255, 255, 255)))

    img.putdata(newData)
    return img


