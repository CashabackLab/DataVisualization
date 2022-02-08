import matplotlib.colors as mc
import colorsys
        
class ColorWheel():
    """
    ColorWheel object to store common colors used by the CashabackLab
    """
    def __init__(self):
        #Legacy Names
        self.pred_red = "#C70808"
        self.prey_blue = "#23537F"
        self.rak_blue = "#0BB8FD"
        self.rak_orange = "#FD8B0B"
        self.rak_red = "#E35D72"
        self.dark_grey = "#727273"
        self.light_grey = "#B2B1B3"
        self.purple = "#984FDE"
        self.green = '#33cc33'
        self.prey_blue_light = "#4f7598" #for black backgrounds
        
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
        self.orange_sat = '#EF9F00'
        self.faded_orange_sat = '#FFC859'
        self.burnt_orange = '#F76700'
        self.blue_sat = '#1800ED'
        self.faded_blue_sat = '#8274FF'

        self.teal = '#4d9387'
        self.autumn = '#dd521b'
        
    def get_color_cycler(self):
        """
        Returns color list for matplotlib's color cycler
        Ex:  mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color= ColorWheelInstance.get_color_cycler())
        """
        return [self.rak_blue, self.rak_orange, self.rak_red, self.green, self.prey_blue, self.pred_red]
    
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