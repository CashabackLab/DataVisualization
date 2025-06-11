import matplotlib.pyplot as plt
import numpy as np
from string import ascii_uppercase
class AutoFigure:
    def __init__(self, mosaic, figsize = (6.5,4), dpi=150, layout="constrained", sharex=False,sharey=False,
                 hspace = None, wspace = None, height_ratios=None, width_ratios=None):
        
        self.fig, self.axes = plt.subplot_mosaic(mosaic, 
                                                 dpi=dpi,
                                                layout=layout,
                                                figsize=figsize,
                                                sharex=sharex,
                                                sharey=sharey,
                                                gridspec_kw={'wspace':wspace,"hspace":hspace},
                                                height_ratios=height_ratios,
                                                width_ratios=width_ratios,
                                                )
        self.num_axes = len(self.axes.values())
        self.figw,self.figh = self.fig.get_size_inches()
        # Create axmain box for visualization of the bounds and coordinates
        self.axmain  = self.fig.add_axes((0,0,1,1))
        self.axmain.set_xlim(0,self.figw)
        self.axmain.set_ylim(0,self.figh)
        for spine in ['top','right','bottom','left']:
            self.axmain.spines[spine].set_visible(True)
        self.axmain.set_xlim(0,figsize[0])
        self.axmain.set_ylim(0,figsize[1])
        
        self.axmain.patch.set_alpha(0) # Needs to be transparent otherwise it'll cover everything
                
        self.letters = []
        
    def fig_data_to_axis_transform(self,ax):
        '''
        Transformation for figure data coordinates (aka axmain) to ax coordinates desired
        '''
        return self.axmain.transData + ax.transAxes.inverted()
    
    def axis_to_fig_data_transform(self,ax):
        return ax.transAxes + self.axmain.transData.inverted()
                
    def pad_fig(self, w_pad, h_pad, w_space, h_space):
        self.fig.get_layout_engine().set(w_pad=w_pad/self.figw, 
                                         h_pad=h_pad/self.figh, 
                                         wspace=w_space/self.figw,
                                         hspace=h_space/self.figh)
    def ax_dim(self,ax):
        bbox = ax.get_window_extent().transformed(self.fig.dpi_scale_trans.inverted())
        return bbox.width, bbox.height
    
    def ax_loc(self,ax):
        bbox = ax.get_window_extent().transformed(self.fig.dpi_scale_trans.inverted())
        return bbox.x0,bbox.y0
        
    def set_position(self, ax, loc):
        self.fig.canvas.draw()
        x,y = loc
        w,h = self.ax_dim(ax)
        self.fig.set_layout_engine('none')

        ax.set_position((x/self.figw, y/self.figh, w/self.figw, h/self.figh))

    def adjust_position(self, ax, adjustment):
        self.fig.canvas.draw()

        dx,dy = adjustment
        w,h = self.ax_dim(ax)
        x,y = self.ax_loc(ax)
        self.fig.set_layout_engine('none')
        ax.set_position(((x+dx)/self.figw, (y+dy)/self.figh, w/self.figw, h/self.figh))
        
    def set_size(self, ax, size):
        self.fig.canvas.draw()
        w,h = size
        x,y = self.ax_loc(ax)
        self.fig.set_layout_engine('none')
        ax.set_position((x/self.figw, y/self.figh, w/self.figw, h/self.figh))
        
    def adjust_size(self, ax, adjustment):
        self.fig.canvas.draw()
        dw,dh = adjustment
        w,h = self.ax_dim(ax)
        x,y = self.ax_loc(ax)
        self.fig.set_layout_engine('none')
        ax.set_position((x/self.figw, y/self.figh, (w+dw)/self.figw, (h+dh)/self.figh))
            
    def add_all_letters(self, fontsize=12,
                        va="top",ha='left',fontfamily="sans-serif",fontweight="bold",
                        verticalshift=0, horizontalshift=0):
        default_start = (-0,1.0)
        if not isinstance(verticalshift, list):
            verticalshift = np.array([verticalshift]*self.num_axes)
        if not isinstance(horizontalshift, list):
            horizontalshift = np.array([horizontalshift]*self.num_axes)
        
        shift = np.vstack((horizontalshift, verticalshift))
        
        for i,(label, ax) in enumerate(self.axes.items()):
            transfig_loc = self.axis_to_fig_data_transform(ax).transform(default_start) + shift[:,i]
            transax_loc = self.fig_data_to_axis_transform(ax).transform(transfig_loc)
            # label physical distance in and down:
            letter = ascii_uppercase[i]
            trans = self.fig_data_to_axis_transform(ax)
            ax.text(transax_loc[0], transax_loc[1], letter, transform=ax.transAxes,
                    fontsize=fontsize, verticalalignment=va, ha=ha,
                    fontfamily=fontfamily, fontweight=fontweight,
            )
                   
            
    def add_letter(self, ax, x, y, letter = None, fontsize = 12, 
                   ha = "left", va = "top", color = "black", zorder = 20, transform = None):
        if letter == None:
            letter_to_add = ascii_uppercase[len(self.letters)]
        else:
            letter_to_add = letter
        if transform is None:
            transform = ax.transAxes
        
        self.letters.append(letter_to_add)
        ax.text(x, y, letter_to_add, ha = ha, va = va, transform=transform,
                fontweight = "bold", color = color, fontsize = fontsize, zorder = zorder)
    
    @property
    def alphabetic_axes(self) -> list:
        sorted_keys = sorted(self.axes)
        return {k:self.axes[k] for k in sorted_keys}
        
        
        
    def remove_figure_borders(self):
        # for spine in ['top','right','bottom','left']:
        self.axmain.axis("off")
        
    def savefig(self,path,dpi=300, transparent = True):
        self.remove_figure_borders()
        self.fig.savefig(path,dpi=dpi,transparent=transparent)
