from pathlib import Path
from data_visualization.AutoFigure import AutoFigure
import matplotlib.pyplot as plt

def test_add_all_letters():

    fig = plt.figure()
    mosaic=[
        ["legende","legende"],
        ['A', 'B'], 
        ['C', 'D']
    ]
    auto_fig = AutoFigure(mosaic=mosaic, figsize=(6, 4), dpi=150)

    # Add letters to the figure
    auto_fig.add_all_letters()

    plt.close(fig)  # Close the figure after testing

def test_save_subplot():

    fig = plt.figure()
    mosaic=[
        ["legend","legend"],
        ['A', 'B'], 
        ['C', 'D']
    ]
    auto_fig = AutoFigure(mosaic=mosaic, figsize=(6, 4), dpi=150)

    auto_fig.axes['A'].set_title("Title for A")
    auto_fig.axes['B'].set_xlabel("xlabel B")
    auto_fig.axes['B'].set_ylabel("ylabel B")
    
    # Add letters to the figure
    auto_fig.add_all_letters()
    auto_fig.save_subplot(auto_fig.axes['A'], path='./test_save_subplot_a', padx=1.0)
    auto_fig.save_subplot(auto_fig.axes['B'], path='./test_save_subplot_b')

    auto_fig.save_all_subplots('./figpanel', padx=1.0)
    plt.close(fig)  # Close the figure after testing
if __name__ == "__main__":
    test_save_subplot()