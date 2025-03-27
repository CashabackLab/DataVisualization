from .color_wheel import *
from .gen_frame import *
from .Create_GIF import *
from .set_Axes_Color import *
from .plot_inset_image import *
from .Custom_Legend import *
from .legend import legend
from .Pair_Plot import *
from .Stat_Annotation import *
from .jitterdata import jitterdata
from .boxplot import boxplot
from .AutoFigure import AutoFigure


from .generate_icons import (
    get_sight_icon, 
    get_reward_icon, 
    get_punishment_icon, 
    get_hand_icon, 
    get_open_hand_icon, 
    get_foot_icon, 
    get_walking_icon)

from .generate_icons import get_elderly_icon, get_healthy_icon

from .RotatingRectangle import *
from .generate_rectangle_icons import *

from .jitter_array import jitter_array
from .set_transparent import set_transparent
from .figure_panel import figure_panel
from .Figure import Figure

import data_visualization.icons 

from .plot_styles import *

import matplotlib as mpl
mpl.rcParams["axes.facecolor"]   = "none"
mpl.rcParams["figure.facecolor"] = "none"

__version__ = "0.11.2"
