# includes all functions that manipulate the cube by a single move. 



def replace_value(og, working, rowog, collumnog, rownew, collumnnew):
    
    '''
    used to replace the color of a single cube. Used in all rotate and turn functions

    Parameters
    ----------
    og: DataFrame
        origional cube

    working: DataFrame
        a copy of og (deep deep == true)

    rowog: string
        the location of the square on the cube to be replaced

    collumnog: string
        the face of the cube with the square to be replaced

    rownew: string
        the location of the square that the origional square is being replaced with

    collumnnew: string
        the face of the square the the origional sqare is being replaced with

    Returns
    -------
    working: DataFrame
        the cube after the replace occurs
    '''

    (working[rowog])[collumnog] = (og[rownew])[collumnnew]
    return working


# esentially just the same as the function above, just rewritten to fix some issues later on
def replace_value2(og, working, collumnog, rowog, collumnnew, rownew):
    
    '''
    used to replace the color of a single cube. Used in all rotate and turn functions

    Parameters
    ----------
    og: DataFrame
        origional cube

    working: DataFrame
        a copy of og (deep deep == true)

    rowog: string
        the location of the square on the cube to be replaced

    collumnog: string
        the face of the cube with the square to be replaced

    rownew: string
        the location of the square that the origional square is being replaced with

    collumnnew: string
        the face of the square the the origional sqare is being replaced with

    Returns
    -------
    working: DataFrame
        the cube after the replace occurs
    '''

    (working[rowog])[collumnog] = (og[rownew])[collumnnew]
    return working


def turn(chart, working ,a,b,c,d,e,f,g,h,i,j,k,l,m):
    
    '''
    defines a turn using variables that can be replaced locations on the cube to refer to different faces

    Parameters
    ----------
    chart: DataFrame
        origional cube

    a,b,c,d,e,f,g,h: strings
        location on a cube

    i,j,k,l,m: strings
    faces of a cube

    Returns
    -------
    working: DataFrame
        the cube after the turn occurs
    '''

    working = replace_value(chart,working,a, i, g, i)
    working = replace_value(chart, working, b, i, h, i)
    working = replace_value(chart, working, c, i, a, i)
    working = replace_value(chart, working, d, i, b, i)
    working = replace_value(chart, working, e, i, c, i)
    working = replace_value(chart, working, f, i, d, i)
    working = replace_value(chart, working, g, i, e, i)
    working = replace_value(chart, working, h, i, f, i)
    working = replace_value(chart, working, g, j, e, m)
    working = replace_value(chart, working, f, j, d, m)
    working = replace_value(chart, working, e, j, c, m)
    working = replace_value(chart, working, a, k, g, j)
    working = replace_value(chart, working, h, k, f, j)
    working = replace_value(chart, working, g, k, e, j)
    working = replace_value(chart, working, c, l, a, k)
    working = replace_value(chart, working, b, l, h, k)
    working = replace_value(chart, working, a, l, g, k)
    working = replace_value(chart, working, e, m, c, l)
    working = replace_value(chart, working, d, m, b, l)
    working = replace_value(chart, working, c, m, a, l)
    return working


def rotate_clock(thing):
    
    '''
    rotates the entire cube clockwise. Used to simplify turning functions

    Parameters
    ----------
    thing: DataFrame
        cube before rotation

    Returns
    -------
    working: DataFrame
        cube after rotation
    '''

    working = thing.copy(deep = True)
    working.iloc[0] = thing.iloc[1]
    working.iloc[1] = thing.iloc[2]
    working.iloc[2] = thing.iloc[3]
    working.iloc[3] = thing.iloc[0]

    working = replace_value2(thing, working, 'top', 'top left', 'top', 'bottom left')
    working = replace_value2(thing, working, 'top', 'top middle', 'top', 'middle left')
    working = replace_value2(thing, working, 'top', 'top right', 'top', 'top left')
    working = replace_value2(thing, working, 'top', 'middle right', 'top', 'top middle')
    working = replace_value2(thing, working, 'top', 'bottom right', 'top', 'top right')
    working = replace_value2(thing, working, 'top', 'bottom middle', 'top', 'middle right')
    working = replace_value2(thing, working, 'top', 'bottom left', 'top', 'bottom right')
    working = replace_value2(thing, working, 'top', 'middle left', 'top', 'bottom middle')

    working = replace_value2(thing, working, 'bottom', 'top left', 'bottom', 'top right')
    working = replace_value2(thing, working, 'bottom', 'top middle', 'bottom', 'middle right')
    working = replace_value2(thing, working, 'bottom', 'top right', 'bottom', 'bottom right')
    working = replace_value2(thing, working, 'bottom', 'middle right', 'bottom', 'bottom middle')
    working = replace_value2(thing, working, 'bottom', 'bottom right', 'bottom', 'bottom left')
    working = replace_value2(thing, working, 'bottom', 'bottom middle', 'bottom', 'middle left')
    working = replace_value2(thing, working, 'bottom', 'bottom left', 'bottom', 'top left')
    working = replace_value2(thing, working, 'bottom', 'middle left', 'bottom', 'top middle')
    return working
    
    
def rotate_up(thing):
    
    '''
    rotates the entire cube upwards. Used to simplify turning functions

    Parameters
    ----------
    thing: DataFrame
        cube before rotation

    Returns
    -------
    working: DataFrame
        cube after rotation
    '''
    working = thing.copy(deep = True)
    working.iloc[0] = thing.copy(deep = True).iloc[5]
    working.iloc[4] = thing.copy(deep = True).iloc[0]
    
    working = replace_value2(thing, working, 'bottom', 'top left', 'back', 'bottom right')
    working = replace_value2(thing, working, 'bottom', 'top middle', 'back', 'bottom middle')
    working = replace_value2(thing, working, 'bottom', 'top right', 'back', 'bottom left')
    working = replace_value2(thing, working, 'bottom', 'middle right', 'back', 'middle left')
    working = replace_value2(thing, working, 'bottom', 'bottom right', 'back', 'top left')
    working = replace_value2(thing, working, 'bottom', 'bottom middle', 'back', 'top middle')
    working = replace_value2(thing, working, 'bottom', 'bottom left', 'back', 'top right')
    working = replace_value2(thing, working, 'bottom', 'middle left', 'back', 'middle right')
    working = replace_value2(thing, working, 'bottom', 'middle middle', 'back', 'middle middle')
    working = replace_value2(thing, working, 'bottom', 'base_color', 'back', 'base_color')
    
    working = replace_value2(thing, working, 'back', 'top left', 'top', 'bottom right')
    working = replace_value2(thing, working, 'back', 'top middle', 'top', 'bottom middle')
    working = replace_value2(thing, working, 'back', 'top right', 'top', 'bottom left')
    working = replace_value2(thing, working, 'back', 'middle right', 'top', 'middle left')
    working = replace_value2(thing, working, 'back', 'bottom right', 'top', 'top left')
    working = replace_value2(thing, working, 'back', 'bottom middle', 'top', 'top middle')
    working = replace_value2(thing, working, 'back', 'bottom left', 'top', 'top right')
    working = replace_value2(thing, working, 'back', 'middle left', 'top', 'middle right')
    working = replace_value2(thing, working, 'back', 'middle middle', 'top', 'middle middle')
    working = replace_value2(thing, working, 'back', 'base_color', 'top', 'base_color')
    
    working = replace_value2(thing, working, 'right', 'top left', 'right', 'bottom left')
    working = replace_value2(thing, working, 'right', 'top middle', 'right', 'middle left')
    working = replace_value2(thing, working, 'right', 'top right', 'right', 'top left')
    working = replace_value2(thing, working, 'right', 'middle right', 'right', 'top middle')
    working = replace_value2(thing, working, 'right', 'bottom right', 'right', 'top right')
    working = replace_value2(thing, working, 'right', 'bottom middle', 'right', 'middle right')
    working = replace_value2(thing, working, 'right', 'bottom left', 'right', 'bottom right')
    working = replace_value2(thing, working, 'right', 'middle left', 'right', 'bottom middle')

    working = replace_value2(thing, working, 'left', 'top left', 'left', 'top right')
    working = replace_value2(thing, working, 'left', 'top middle', 'left', 'middle right')
    working = replace_value2(thing, working, 'left', 'top right', 'left', 'bottom right')
    working = replace_value2(thing, working, 'left', 'middle right', 'left', 'bottom middle')
    working = replace_value2(thing, working, 'left', 'bottom right', 'left', 'bottom left')
    working = replace_value2(thing, working, 'left', 'bottom middle', 'left', 'middle left')
    working = replace_value2(thing, working, 'left', 'bottom left', 'left', 'top left')
    working = replace_value2(thing, working, 'left', 'middle left', 'left', 'top middle')
    return working


#turning functions (two for each face of the cube: clockwise and counterclockwise)
def front_clock(thing):
    
    '''
    rotates the front face of the cube clockwise

    Parameters
    ----------
    thing: DataFrame
        input cube before turn

    Returns
    -------
    output: DataFrame
        cube after turn
    '''

    working = thing.copy(deep = True)
    output = turn(thing,working,'top left', 'top middle', 'top right', 'middle right', 'bottom right',
                  'bottom middle', 'bottom left', 'middle left', 'front', 'top', 'right', 'bottom', 'left')
    return output


def front_counter(thing):
    
    '''
    rotates the front face of the cube counterclockwise

    Parameters
    ----------
    thing: DataFrame
        input cube before turn

    Returns
    -------
    three: DataFrame
        cube after turn
    '''
    
    one = front_clock(thing)
    two = front_clock(one)
    three = front_clock(two)
    return three


def right_clock(thing):
    
    '''
    rotates the right face of the cube clockwise

    Parameters
    ----------
    thing: DataFrame
        input cube before turn

    Returns
    -------
    thing: DataFrame
        cube after turn
    '''

    thing = rotate_clock(thing)
    thing = front_clock(thing)
    thing = rotate_clock(thing)
    thing = rotate_clock(thing)
    thing = rotate_clock(thing)
    return thing


def right_counter(thing):
    
    '''
    rotates the front face of the cube counterclockwise

    Parameters
    ----------
    thing: DataFrame
        input cube before turn

    Returns
    -------
    thing: DataFrame
        cube after turn
    '''

    thing = rotate_clock(thing)
    thing = front_counter(thing)
    thing = rotate_clock(thing)
    thing = rotate_clock(thing)
    thing = rotate_clock(thing)
    return thing


def back_clock(thing):
    
    '''
    rotates the back face of the cube clockwise

    Parameters
    ----------
    thing: DataFrame
        input cube before turn

    Returns
    -------
    thing: DataFrame
        cube after turn
    '''

    thing = rotate_clock(thing)
    thing = rotate_clock(thing)
    thing = front_clock(thing)
    thing = rotate_clock(thing)
    thing = rotate_clock(thing)
    return thing


def back_counter(thing):
    
    '''
    rotates the back face of the cube counterclockwise

    Parameters
    ----------
    thing: DataFrame
        input cube before turn

    Returns
    -------
    thing: DataFrame
        cube after turn
    '''

    thing = rotate_clock(thing)
    thing = rotate_clock(thing)
    thing = front_counter(thing)
    thing = rotate_clock(thing)
    thing = rotate_clock(thing)
    return thing


def left_clock(thing):
    
    '''
    rotates the left face of the cube clockwise

    Parameters
    ----------
    thing: DataFrame
        input cube before turn

    Returns
    -------
    thing: DataFrame
        cube after turn
    '''

    thing = rotate_clock(thing)
    thing = rotate_clock(thing)
    thing = rotate_clock(thing)
    thing = front_clock(thing)
    thing = rotate_clock(thing)
    return thing


def left_counter(thing):
    
    '''
    rotates the left face of the cube counterclockwise

    Parameters
    ----------
    thing: DataFrame
        input cube before turn

    Returns
    -------
    thing: DataFrame
        cube after turn
    '''

    thing = rotate_clock(thing)
    thing = rotate_clock(thing)
    thing = rotate_clock(thing)
    thing = front_counter(thing)
    thing = rotate_clock(thing)
    return thing


def lower_clock(thing):
    
    '''
    rotates the bottoom face of the cube clockwise

    Parameters
    ----------
    thing: DataFrame
        input cube before turn

    Returns
    -------
    thing: DataFrame
        cube after turn
    '''

    thing = rotate_up(thing)
    thing = front_clock(thing)
    thing = rotate_up(thing)
    thing = rotate_up(thing)
    thing = rotate_up(thing)
    return thing


def lower_counter(thing):
    
    '''
    rotates the bottom face of the cube counterclockwise

    Parameters
    ----------
    thing: DataFrame
        input cube before turn

    Returns
    -------
    thing: DataFrame
        cube after turn
    '''

    thing = rotate_up(thing)
    thing = front_counter(thing)
    thing = rotate_up(thing)
    thing = rotate_up(thing)
    thing = rotate_up(thing)
    return thing


def upper_clock(thing):
    
    '''
    rotates the upper face of the cube clockwise

    Parameters
    ----------
    thing: DataFrame
        input cube before turn

    Returns
    -------
    thing: DataFrame
        cube after turn
    '''

    thing = rotate_up(thing)
    thing = rotate_up(thing)
    thing = rotate_up(thing)
    thing = front_clock(thing)
    thing = rotate_up(thing)
    return thing


def upper_counter(thing):
    
    '''
    rotates the upper face of the cube counterclockwise

    Parameters
    ----------
    thing: DataFrame
        input cube before turn

    Returns
    -------
    thing: DataFrame
        cube after turn
    '''
    thing = rotate_up(thing)
    thing = rotate_up(thing)
    thing = rotate_up(thing)
    thing = front_counter(thing)
    thing = rotate_up(thing)
    return thing
