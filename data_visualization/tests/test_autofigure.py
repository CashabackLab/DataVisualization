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
    
if __name__ == "__main__":
    test_add_all_letters()