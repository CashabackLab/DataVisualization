import matplotlib.pyplot as plt
import numpy as np
import os

def show_styles():
    '''Prints out the names of the currently stored plotting styles that are in the plot_styles
    folder.
    '''
    data_vis_path = os.path.dirname(os.path.realpath(__file__)) # package folder location
    plt_styles_folder_path = os.path.join(data_vis_path, "plot_styles") # folder path that holds our plot styles
    print(os.listdir(plt_styles_folder_path))
    return

def return_styles():
    '''Returns the names of the currently stored plotting styles that are in the plot_styles
    folder.
    '''
    data_vis_path = os.path.dirname(os.path.realpath(__file__)) # package folder location
    plt_styles_folder_path = os.path.join(data_vis_path, "plot_styles") # folder path that holds our plot styles
    return os.listdir(plt_styles_folder_path)

def get_plot_style_path(plot_style):
    '''Helper function for "set_plot_style". Take a plot style name (a *.mplstyle file), and returns the file path. 
    For later usage.
    Inputs:
        plot_style, .mplstyle file
    Outputs:
        plot_style_path, absolute path of the plot_style file
    '''
    data_vis_path = os.path.dirname(os.path.realpath(__file__)) # package folder location
    plt_styles_folder_path = os.path.join(data_vis_path, "plot_styles")

    # Testing if "plot_style" is a string and a valid option
    if not isinstance(plot_style, str):
        show_styles()
        raise TypeError("plot_style must be a string. Review the valid plot styles.")
    elif plot_style not in os.listdir(plt_styles_folder_path):
        print("Please select a valid option for plot_style: ")
        show_styles()
    else:
        plot_style_path = os.path.join(plt_styles_folder_path, plot_style)
        
    return plot_style_path

def set_plot_style(style):
    '''Take a valid string plot style
    '''
    plot_path = get_plot_style_path(style)
    plt.style.use(plot_path)
    print(f"Successfully changed to {style}")
    
    return























