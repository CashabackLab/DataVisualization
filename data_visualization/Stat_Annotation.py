import matplotlib as mpl
import matplotlib.pyplot as plt

def stat_annotation(ax, x1, x2, y, p_val, effect_size = None, cles = None, cles_first = False, preamble = None, **kwargs):
    """
    Annotate plot to have statistics.
    effect_size is Cohen's D
    cles is Common Language Effect Size
    preamble is any text that goes before the statistics
    
    Optional Arguments:
    color            = kwargs.get("color", "grey")
    h                = kwargs.get("h", 0.1 * y)
    lw               = kwargs.get("lw", .7)
    fontsize         = kwargs.get("fontsize", 6)
    exact_p          = kwargs.get("exact_p", False)
    indicator_length = kwargs.get("indicator_length", 0)
    stacked          = kwargs.get("stacked", False)
    fontweight 
    """
    color = kwargs.get("color", "grey")
    h = kwargs.get("h", 0.1 * y)
    lw = kwargs.get("lw", .7)
    fontsize = kwargs.get("fontsize", 6)
    exact_p = kwargs.get("exact_p", False)
    indicator_length = kwargs.get("indicator_length", 0)
    stacked = kwargs.get("stacked", False)
    
    #Handle P-Value
    if p_val < 0.001 and not exact_p:
        p_text = f"p < 0.001"
    elif p_val >= 0.001 or exact_p:
        p_text = f"p = {p_val:.3f}"
        
    #Handle Effect Size and Common Language Effect Size
    if effect_size != None and cles != None: #if both
        
        if cles_first:
            p_text = p_text + r', $\mathbf{\hat{\theta}}$ = ' + f"{cles:.2f}" + f", d = {effect_size:.2f}" 
        else:
            p_text = p_text + f", d = {effect_size:.2f}, " + r'$\mathbf{\hat{\theta}}$ = ' + f"{cles:.2f}"
            
    elif effect_size != None and cles == None: #if only Cohen D
        p_text = p_text + f", d = {effect_size:.2f}" 
        
    elif effect_size == None and cles != None: #if only CLES
        p_text = p_text + r', $\mathbf{\hat{\theta}}$ = ' + f"{cles:.2f}"

    if preamble != "" and preamble != None: #If Preamble
        if not stacked:
            p_text = preamble + " " + p_text 
        else:
            p_text = preamble + ", " + p_text
            
    #plot the text
    if not stacked:
        ax.plot([x1, x1, x2, x2], [y - indicator_length, y, y, y - indicator_length], lw=lw, c=color)
        ax.text((x1+x2)*.5, y+h , p_text, ha='center', va='bottom', color=color, fontsize = fontsize, weight = "bold")
    else:
        ax.plot([x1, x1, x2, x2], [y - indicator_length, y, y, y - indicator_length], lw=lw, c=color)
        
        split_text = p_text.split(", ")
        stacked_text = "\n".join(split_text)
        
        ax.text((x1+x2)*.5, y+h , stacked_text, ha='center', va='bottom', color=color, fontsize = fontsize, weight = "bold")
    
    
def Stat_Annotation(ax, x1, x2, y, p_val, effect_size = None, h = 0, color = "grey", lw = .7, fontsize = 6, exact_p = False):
    """Legacy code. Use stat_annotation for more functionality"""
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
        
