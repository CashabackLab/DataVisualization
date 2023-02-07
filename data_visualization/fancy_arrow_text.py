


"""
def fancy_arrow_text(curr_ax,Pos,Delta_Arrow,Text = '',Text_Loc = 'Left',line_dict = {},text_dict_orig = {},return_text = False):
    
    
    # def fancy_arrow_text(curr_ax,Pos,Delta_Arrow,Text = '',Arrow_Loc = 'Left,**kwargs)
    arrow_x_pos = Pos[0]
    arrow_y_pos = Pos[1]
    arrow_delta_x = Delta_Arrow[0]
    arrow_delta_y = Delta_Arrow[1]
    
    arrow_patch = patches.FancyArrow(arrow_x_pos, arrow_y_pos, arrow_delta_x, arrow_delta_y,\
                                     clip_on=False, length_includes_head = True,**line_dict)
    
        
    curr_rotation = math.atan2(arrow_delta_y,arrow_delta_x)
    text_dict = text_dict_orig.copy()
    if Text_Loc ==  'Left':
        if curr_rotation >= np.pi/2:
            text_rotation = curr_rotation
            dir_mult = 1
            
        elif curr_rotation <= -np.pi/2:
            text_rotation = curr_rotation + np.pi
            dir_mult = -1
        elif curr_rotation >= 0 and curr_rotation < np.pi/2:
            dir_mult = 1
            text_rotation = curr_rotation
        else:
            text_rotation = curr_rotation + np.pi
            dir_mult = -1
    elif Text_Loc == 'Right':
        if curr_rotation >= np.pi/2:
            text_rotation = curr_rotation+ np.pi
            dir_mult = -1
            
        elif curr_rotation <= -np.pi/2:
            text_rotation = curr_rotation +np.pi
            dir_mult = 1
        elif curr_rotation >= 0 and curr_rotation < np.pi/2:
            dir_mult = -1
            text_rotation = curr_rotation
        else:
            text_rotation = curr_rotation
            dir_mult = 1
    
    distance_from_arrow_def = text_dict.get('pad',0)
    if type(distance_from_arrow_def) == int or type(distance_from_arrow_def) == float :
        
        distance_from_arrow_perp = line_dict.get('width',.01) + dir_mult* distance_from_arrow_def
        distance_from_arrow_parallel = 0
    else:
        distance_from_arrow_perp = line_dict.get('width',.01) + dir_mult* distance_from_arrow_def[0]
        distance_from_arrow_parallel = distance_from_arrow_def[1]
    # text_dict.pop('pad')

    # distance_from_arrow = .5+ 0
    text_dict.pop('pad','')
    text_dict['color'] = text_dict.get('color',wheel.black)
    # x_distance_from_arrow_perp = distance_from_arrow_perp * np.sin(text_rotation + np.pi)
    # y_distance_from_arrow_perp = distance_from_arrow_perp * np.cos(text_rotation + np.pi)
    
    # x_distance_from_arrow_parallel = distance_from_arrow_parallel * np.sin(text_rotation + np.pi)
    # y_distance_from_arrow_parallel = distance_from_arrow_parallel * np.cos(text_rotation + np.pi)


    arrow_length = np.sqrt(arrow_delta_x**2 + arrow_delta_y**2)
    
    Rot_Matrix = np.array([[np.cos(curr_rotation),-1*np.sin(curr_rotation)],[np.sin(curr_rotation),np.cos(curr_rotation)]],dtype='float') 
    text_new_position = Rot_Matrix @ np.array([[distance_from_arrow_parallel],[distance_from_arrow_perp]])
    
    text_x_pos = arrow_length/2 * np.cos(curr_rotation) + text_new_position[0] + arrow_x_pos
    text_y_pos = arrow_length/2 * np.sin(curr_rotation) + text_new_position[1] + arrow_y_pos
    
    # if rotation > 
    # text_rotation 
        
    va_curr = text_dict.get('va','bottom')
    text_dict.pop('va','')
        
        
    text = curr_ax.text(text_x_pos,text_y_pos,Text,rotation = text_rotation*180/np.pi,rotation_mode = 'anchor',\
                 ha = 'center', va = va_curr,\
                 
                 
                 **text_dict)
   
        
        
        
        
    curr_ax.add_patch(arrow_patch)      
    if return_text:
        return text
"""
