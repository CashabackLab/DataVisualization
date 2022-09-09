import matplotlib.pyplot as plt

def transparent_plot(ax):
  """
  Removes background patch of plot
  """
  
  ax.get_figure().set_color("none")
  ax.patch.set_color("none")
