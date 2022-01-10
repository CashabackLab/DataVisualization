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
