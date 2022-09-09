import matplotlib.pyplot as plt

def set_transparent(ax):
  """
  Removes background patch of plot
  """
  
  ax.get_figure().set_color("none")
  ax.get_figure().set_alpha(0)
  
  ax.patch.set_color("none")
  ax.patch.set_alpha(0)
