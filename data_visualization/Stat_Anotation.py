import matplotlib as mpl
import matplotlib.pyplot as plt

def Stat_Annotation(ax, x1, x2, y, p_val, effect_size = None, h = 0, color = "grey", lw = .7, fontsize = 6, exact_p = False):
    if p_val < 0.001 and not exact_p:
    
        if effect_size != None:
            ax.plot([x1, x1, x2, x2], [y, y, y, y], lw=lw, c=color)
            ax.text((x1+x2)*.5, y+h , f"p < 0.001, d = {abs(effect_size):.2f}", ha='center', va='bottom', color=color, fontsize = fontsize, weight = "bold")
        else:
            ax.plot([x1, x1, x2, x2], [y, y, y, y], lw=lw, c=color)
            ax.text((x1+x2)*.5, y+h , "p < 0.001", ha='center', va='bottom', color=color, fontsize = fontsize, weight = "bold")
            
    elif p_val > 0.001 or exact_p:
        if effect_size != None:
            ax.plot([x1, x1, x2, x2], [y, y, y, y], lw=lw, c=color)
            ax.text((x1+x2)*.5, y+h , f"p = {p_val:.3f}, d = {abs(effect_size):.2f}", ha='center', va='bottom', color=color, fontsize = fontsize, weight = "bold")
        else:
            ax.plot([x1, x1, x2, x2], [y, y, y, y], lw=lw, c=color)
            ax.text((x1+x2)*.5, y+h , f"p = {p_val:.3f}", ha='center', va='bottom', color=color, fontsize = fontsize, weight = "bold")
        
