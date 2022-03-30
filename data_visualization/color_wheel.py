import matplotlib.colors as mc
import colorsys
import matplotlib.pyplot as plt        

class _dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
    
class ColorWheel(_dotdict):
    """
    ColorWheel object to store common colors used by the CashabackLab
    Can Access colors as a dictionary key or as a class attribute
    """
    def __init__(self):
        #Legacy Names
        self.pred_red        = "#C70808"
        self.prey_blue       = "#23537F"
        self.rak_blue        = "#0BB8FD"
        self.rak_orange      = "#FD8B0B"
        self.rak_red         = "#E35D72"
        self.dark_grey       = "#727273"
        self.light_grey      = "#B2B1B3"
        self.purple          = "#984FDE"
        self.green           = '#33cc33'
        self.prey_blue_light = "#4f7598" #for black backgrounds
        
        self.legacy_list = ["pred_red",       
                            "prey_blue",      
                            "rak_blue",       
                            "rak_orange",     
                            "rak_red",                
                            "prey_blue_light"]

        #Modern names for the same colors above 
        # hc == high contrast
        self.dark_red = "#C70808"
        self.dark_blue = "#23537F"
        self.light_blue = "#0BB8FD"
        self.light_orange = "#FD8B0B"
        self.pink = "#E35D72"
        self.dark_grey = "#727273"
        self.light_grey = "#B2B1B3"
        self.purple = "#984FDE"
        self.green = '#33cc33'
        self.dark_blue_hc = "#4f7598" #for black backgrounds

        #Extras
        self.orange = '#E89D07'
        self.faded_orange = '#FFC859'
        self.burnt_orange = '#F76700'
        self.blue = '#2C19D4'
        self.faded_blue = '#8375FF'
        self.plum_blue = '#881BE0'
        self.sunburst_orange = "#F76700"
        self.burnt_orange = "#CC5500"

        self.teal = '#4d9387'
        self.autumn = '#dd521b'
        
        self.dark_blue2  = "#016b93"

        self.dark_brown  = "#854600"
        self.brown        = "#9e5300"
        self.light_brown = "#c86a00"
        
    def get_color_cycler(self):
        """
        Returns color list for matplotlib's color cycler
        Ex:  mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color= ColorWheelInstance.get_color_cycler())
        """
        return [self.rak_blue, self.rak_orange, self.rak_red, self.green, self.prey_blue, self.pred_red]
    
    def hex_to_rgb(self, hex_code, normalize = False):
        """
        Input: Hex String
        Output: integer RGB values
        """
        hex_code = hex_code.lstrip("#")
        RGB_vals = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
        
        if normalize: 
            RGB_vals = (RGB_vals[0] / 255, RGB_vals[1] / 255, RGB_vals[2] / 255)
        
        return RGB_vals
    
    def rgb_to_hex(self, rgb):
        """
        Input: rgb tuple, ex: (.2, .8, .2) or (40, 185, 40)
        Output: Hex Representation of color
        """
        if rgb[0] < 1:
            int_rgb = (rgb[0] * 255, rgb[1] * 255, rgb[2] * 255)
            int_rgb = [int(x) for x in int_rgb]
            int_rgb = tuple(int_rgb)
        else:
            int_rgb = rgb
            
        return '#%02x%02x%02x' % int_rgb
    
    def lighten_color(self, color, amount = 1, return_rgb = False):
        """
        Lightens the given color by multiplying (1-luminosity) by the given amount.
        Input can be matplotlib color string, hex string, or RGB tuple.
        
        amount must be between 0 and 2
        amount = 1 returns the same color
        amount > 1 returns darker shade
        amount < 1 returns lighter shade
        
        Default return is Hex Code, set return_rgb = True for rgb tuple
        
        Examples:
        >> lighten_color('g', amount = 0.3)
        >> lighten_color('#F034A3', amount = 0.6)
        >> lighten_color((.3,.55,.1), amount = 0.5)
        """

        c = colorsys.rgb_to_hls(*mc.to_rgb(color))
        rgb = colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2])
        
        if return_rgb:
            return rgb
        else:
            return self.rgb_to_hex(rgb)

    def get_hsv(self, hexrgb):
        hexrgb = hexrgb[1]
        hexrgb = hexrgb.lstrip("#")   
        r, g, b = (int(hexrgb[i:i+2], 16) / 255.0 for i in range(0,5,2))
        return colorsys.rgb_to_hsv(r, g, b)

    def demo_colors(self, background = "white", no_legacy = True, fontname = "Dejavu Sans"):
        """
        Shows a plot demo for the available colors.
        Change background to look at colors with different backgrounds
        set no_legacy = True to see legacy color names
        Returns Nothing
        """
        if no_legacy:
            color_keys = [x for x in self.keys() if x != "legacy_list" and x not in self.legacy_list] 
        else:
            color_keys = [x for x in self.keys() if x != "legacy_list"] 
            
        num_colors = len(color_keys)
        #attempt to sort colors by hue
        color_list = [(x, self[x]) for x in color_keys ]
        color_list.sort(key=self.get_hsv)

        plt.figure(dpi = 300, figsize = (4, 7/28 * num_colors))
        ax = plt.gca()
        plt.ylim(0, num_colors*1.3 +1)
        plt.xlim(0, 1.8)
        plt.yticks([])
        plt.xticks([])

        for i, pairing in enumerate(color_list):
            color = pairing[0]
            plt.barh((num_colors - i) *1.3, 1, color = self[color], height = 1)
            plt.text(0.1, 1.3*(num_colors - i) , color, ha = "left", va = "center", color = "w", fontsize = 9, 
                    fontname = fontname)
            plt.text(1.05, 1.3*(num_colors - i) , color, ha = "left", va = "center", color = self[color], fontsize = 9,
                    fontweight = "bold", fontname = fontname)

        ax.spines.right.set_visible(False)
        ax.spines.top.set_visible(False)
        ax.set_facecolor(background)
