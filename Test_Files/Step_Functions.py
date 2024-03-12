# uses turning functions to define each step of solving a cube. These steps follow the basic Rubik's cube instructions that can
# be found here: https://ruwix.com/the-rubiks-cube/how-to-solve-the-rubiks-cube-beginners-method/

# a note: white and yellow are usually the top and bottom colors, respectively, but the code takes input from any color #combination

from Functions import Ref_Functions as rf

master_list = []


def daisy(cube):
    
    '''
    sets up a white cross around the yellow center piece

    Parameters
    ----------
    cube: DataFrame
        input cube, set up to form daisy

    Returns
    -------
    cube: DataFrame
        the cube once the daisy is formed
    '''

    base = cube['base_color']['top']
    while not (cube['middle right']['bottom'] == base and
               cube['middle left']['bottom'] == base and
               cube['top middle']['bottom'] == base and
               cube['bottom middle']['bottom'] == base):
        
        if cube['middle right']['front'] == base:
            while cube['middle right']['bottom'] == base:
                cube = rf.lower_clock(cube)
                master_list.append("D")
            cube = rf.right_counter(cube)
            master_list.append("R'")

        if cube['middle left']['front'] == base:
            while cube['middle left']['bottom'] == base:
                cube = rf.lower_clock(cube)
                master_list.append("D")
            cube = rf.left_clock(cube)
            master_list.append("L")

        if cube['middle right']['right'] == base:
            while cube['bottom middle']['bottom'] == base:
                cube = rf.lower_clock(cube)
                master_list.append("D")
            cube = rf.back_counter(cube)
            master_list.append("B'")

        if cube['middle left']['right'] == base:
            while cube['top middle']['bottom'] == base:
                cube = rf.lower_clock(cube)
                master_list.append("D")
            cube = rf.front_clock(cube)
            master_list.append("F")

        if cube['middle right']['left'] == base:
            while cube['top middle']['bottom'] == base:
                cube = rf.lower_clock(cube)
                master_list.append("D")
            cube = rf.front_counter(cube)
            master_list.append("F'")

        if cube['middle left']['left'] == base:
            while cube['bottom middle']['bottom'] == base:
                cube = rf.lower_clock(cube)
                master_list.append("D")
            cube = rf.back_clock(cube)
            master_list.append("B")

        if cube['middle right']['back'] == base:
            while cube['middle left']['bottom'] == base:
                cube = rf.lower_clock(cube)
                master_list.append("D")
            cube = rf.left_counter(cube)
            master_list.append("L'")

        if cube['middle left']['back'] == base:
            while cube['middle right']['bottom'] == base:
                cube = rf.lower_clock(cube)
                master_list.append("D")
            cube = rf.right_clock(cube)
            master_list.append("R")

        if cube['middle right']['top'] == base:
            while cube['middle right']['bottom'] == base:
                cube = rf.lower_clock(cube)
                master_list.append("D")
            cube = rf.right_clock(cube)
            cube = rf.right_clock(cube)
            master_list.append("R")
            master_list.append("R")

        if cube['middle left']['top'] == base:
            while cube['middle left']['bottom'] == base:
                cube = rf.lower_clock(cube)
                master_list.append("D")
            cube = rf.left_clock(cube)
            cube = rf.left_clock(cube)
            master_list.append("L")
            master_list.append("L")

        if cube['top middle']['top'] == base:
            while cube['bottom middle']['bottom'] == base:
                cube = rf.lower_clock(cube)
                master_list.append("D")
            cube = rf.back_clock(cube)
            cube = rf.back_clock(cube)
            master_list.append("B")
            master_list.append("B")

        if cube['bottom middle']['top'] == base:
            while cube['top middle']['bottom'] == base:
                cube = rf.lower_clock(cube)
                master_list.append("D")
            cube = rf.front_clock(cube)
            cube = rf.front_clock(cube)
            master_list.append("F")
            master_list.append("F")
 
        
        if cube['top middle']['back'] == base:
            while cube['bottom middle']['bottom'] == base:
                cube = rf.lower_clock(cube)
                master_list.append("D")
            cube = rf.back_clock(cube)
            master_list.append("B")
            
        if cube['bottom middle']['back'] == base:
            while cube['bottom middle']['bottom'] == base:
                cube = rf.lower_clock(cube)
                master_list.append("D")
            cube = rf.back_clock(cube)
            master_list.append("B")
            
        if cube['bottom middle']['right'] == base:
            while cube['middle right']['bottom'] == base:
                cube = rf.lower_clock(cube)
                master_list.append("D")
            cube = rf.right_clock(cube)
            master_list.append("R")
            
        if cube['top middle']['right'] == base:
            while cube['middle right']['bottom'] == base:
                cube = rf.lower_clock(cube)
                master_list.append("D")
            cube = rf.right_clock(cube)
            master_list.append("R")
            
        if cube['top middle']['front'] == base:
            while cube['top middle']['bottom'] == base:
                cube = rf.lower_clock(cube)
                master_list.append("D")
            cube = rf.front_clock(cube)
            master_list.append("F")
            
        if cube['bottom middle']['front'] == base:
            while cube['top middle']['bottom'] == base:
                cube = rf.lower_clock(cube)
                master_list.append("D")
            cube = rf.front_clock(cube)
            master_list.append("F")
            
        if cube['top middle']['left'] == base:
            while cube['middle left']['bottom'] == base:
                cube = rf.lower_clock(cube)
                master_list.append("D")
            cube = rf.left_clock(cube)
            master_list.append("L")
            
        if cube['bottom middle']['left'] == base:
            while cube['middle left']['bottom'] == base:
                cube = rf.lower_clock(cube)
                master_list.append("D")
            cube = rf.left_clock(cube)
            master_list.append("L")
          
     
    return cube

def white_cross(cube):
    
    '''
    builds the white cross on the cube

    Parameters
    ----------
    cube: DataFrame
        input cube, set up to form the white cross

    Returns
    -------
    cube: DataFrame
        the cube once the white cross is formed
    '''

    while (cube['bottom middle']['right'] != cube ['middle middle']['right']
           or cube['middle right']['bottom'] != cube['middle middle']['top']):
        cube = rf.lower_clock(cube)
        master_list.append("D")
    cube = rf.right_clock(cube)
    cube = rf.right_clock(cube)
    master_list.append("R")
    master_list.append("R")
    
    while (cube['bottom middle']['front'] != cube ['middle middle']['front']
           or cube['top middle']['bottom'] != cube['middle middle']['top']):
        cube = rf.lower_clock(cube)
        master_list.append("D")
    cube = rf.front_clock(cube)
    cube = rf.front_clock(cube)
    master_list.append("F")
    master_list.append("F")
    
    while (cube['bottom middle']['left'] != cube ['middle middle']['left']
           or cube['middle left']['bottom'] != cube['middle middle']['top']):
        cube = rf.lower_clock(cube)
        master_list.append("D")
    cube = rf.left_clock(cube)
    cube = rf.left_clock(cube)
    master_list.append("L")
    master_list.append("L")
    
    while (cube['bottom middle']['back'] != cube ['middle middle']['back'] 
           or cube['bottom middle']['bottom'] != cube['middle middle']['top']):
        cube = rf.lower_clock(cube)
        master_list.append("D")
    cube = rf.back_clock(cube)
    cube = rf.back_clock(cube)
    master_list.append("B")
    master_list.append("B")
    
    return cube
    
    
def top_layer(cube):
    
    '''
    orients the white corners

    Parameters
    ----------
    cube: DataFrame
        input cube, set up to orient the white corners

    Returns
    -------
    cube: DataFrame
        the cube once the white corners are oriented
    '''

    white = cube['base_color']['top']
    stop = False
    while stop == False:
        turn = True
        
        if cube['bottom right']['front'] == white and cube['top right']['bottom'] == cube['base_color']['front']:
            cube = rf.lower_counter(cube)
            master_list.append("D'")
            cube = rf.right_counter(cube)
            master_list.append("R'")
            cube = rf.lower_clock(cube)
            master_list.append("D")
            cube = rf.right_clock(cube)
            master_list.append("R")
            turn = False
        
        if cube['bottom right']['right'] == white and cube['bottom right']['bottom'] == cube['base_color']['right']:
            cube = rf.lower_counter(cube)
            master_list.append("D'")
            cube = rf.back_counter(cube)
            master_list.append("B'")
            cube = rf.lower_clock(cube)
            master_list.append("D")
            cube = rf.back_clock(cube)
            master_list.append("B")
            turn = False
            
        if cube['bottom right']['back'] == white and cube['bottom left']['bottom'] == cube['base_color']['back']:
            cube = rf.lower_counter(cube)
            master_list.append("D'")
            cube = rf.left_counter(cube)
            master_list.append("L'")
            cube = rf.lower_clock(cube)
            master_list.append("D")
            cube = rf.left_clock(cube)
            master_list.append("L")
            turn = False
            
        if cube['bottom right']['left'] == white and cube['top left']['bottom'] == cube['base_color']['left']:
            cube = rf.lower_counter(cube)
            master_list.append("D'")
            cube = rf.front_counter(cube)
            master_list.append("F'")
            cube = rf.lower_clock(cube)
            master_list.append("D")
            cube = rf.front_clock(cube)
            master_list.append("F")
            turn = False
            
        if cube['bottom left']['front'] == white and cube['bottom right']['left'] == cube['base_color']['left']:
            cube = rf.front_counter(cube)
            master_list.append("F'")
            cube = rf.lower_counter(cube)
            master_list.append("D'")
            cube = rf.front_clock(cube)
            master_list.append("F")
            turn = False
            
        if cube['bottom left']['left'] == white and cube['bottom right']['back'] == cube['base_color']['back']:
            cube = rf.left_counter(cube)
            master_list.append("L'")
            cube = rf.lower_counter(cube)
            master_list.append("D'")
            cube = rf.left_clock(cube)
            master_list.append("L")
            turn = False
            
        if cube['bottom left']['back'] == white and cube['bottom right']['right'] == cube['base_color']['right']:
            cube = rf.back_counter(cube)
            master_list.append("B'")
            cube = rf.lower_counter(cube)
            master_list.append("D'")
            cube = rf.back_clock(cube)
            master_list.append("B")
            turn = False
            
        if cube['bottom left']['right'] == white and cube['bottom right']['front'] == cube['base_color']['front']:
            cube = rf.right_counter(cube)
            master_list.append("R'")
            cube = rf.lower_counter(cube)
            master_list.append("D'")
            cube = rf.right_clock(cube)
            master_list.append("R")
            turn = False
            
        if cube['top right']['bottom'] == white and cube['bottom right']['front'] == cube['base_color']['right']:
            cube = rf.front_clock(cube)
            master_list.append("F")
            cube = rf.left_clock(cube)
            master_list.append("L")
            cube = rf.lower_clock(cube)
            master_list.append("D")
            cube = rf.lower_clock(cube)
            master_list.append("D")
            cube = rf.left_counter(cube)
            master_list.append("L'")
            cube = rf.front_counter(cube)
            master_list.append("F'")
            turn = False
            
        if cube['top left']['bottom'] == white and cube['bottom right']['left'] == cube['base_color']['front']:
            cube = rf.left_clock(cube)
            master_list.append("L")
            cube = rf.back_clock(cube)
            master_list.append("B")
            cube = rf.lower_clock(cube)
            master_list.append("D")
            cube = rf.lower_clock(cube)
            master_list.append("D")
            cube = rf.back_counter(cube)
            master_list.append("B'")
            cube = rf.left_counter(cube)
            master_list.append("L'")
            turn = False
            
        if cube['bottom left']['bottom'] == white and cube['bottom right']['back'] == cube['base_color']['left']:
            cube = rf.back_clock(cube)
            master_list.append("B")
            cube = rf.right_clock(cube)
            master_list.append("R")
            cube = rf.lower_clock(cube)
            master_list.append("D")
            cube = rf.lower_clock(cube)
            master_list.append("D")
            cube = rf.right_counter(cube)
            master_list.append("R'")
            cube = rf.back_counter(cube)
            master_list.append("B'")
            turn = False
        
        if cube['bottom right']['bottom'] == white and cube['bottom right']['right'] == cube['base_color']['back']:
            cube = rf.right_clock(cube)
            master_list.append("R")
            cube = rf.front_clock(cube)
            master_list.append("F")
            cube = rf.lower_clock(cube)
            master_list.append("D")
            cube = rf.lower_clock(cube)
            master_list.append("D")
            cube = rf.front_counter(cube)
            master_list.append("F'")
            cube = rf.right_counter(cube)
            master_list.append("R'")
            turn = False
            
        if ((cube['bottom right']['top'] == white and cube['top right']['front'] != cube['base_color']['front']) or
            cube['top right']['front'] == white or cube['top left']['right'] == white):
            cube = rf.right_counter(cube)
            master_list.append("R'")
            cube = rf.lower_counter(cube)
            master_list.append("D'")
            cube = rf.right_clock(cube)
            master_list.append("R")
            turn = False
            
        if ((cube['bottom left']['top'] == white and cube['top left']['front'] != cube['base_color']['front']) or
            cube['top left']['front'] == white or cube['top right']['left'] == white):
            cube = rf.front_counter(cube)
            master_list.append("F'")
            cube = rf.lower_counter(cube)
            master_list.append("D'")
            cube = rf.front_clock(cube)
            master_list.append("F")
            turn = False
            
        if ((cube['top left']['top'] == white and cube['top left']['left'] != cube['base_color']['left']) or
            cube['top left']['left'] == white or cube['top right']['back'] == white):
            cube = rf.left_counter(cube)
            master_list.append("L'")
            cube = rf.lower_counter(cube)
            master_list.append("D'")
            cube = rf.left_clock(cube)
            master_list.append("L")
            turn = False
            
        if ((cube['top right']['top'] == white and cube['top left']['back'] != cube['base_color']['back']) or
            cube['top left']['back'] == white or cube['top right']['right'] == white):
            cube = rf.back_counter(cube)
            master_list.append("B'")
            cube = rf.lower_counter(cube)
            master_list.append("D'")
            cube = rf.back_clock(cube)
            master_list.append("B")
            turn = False
        
        if turn == True:
            cube = rf.lower_clock(cube)
            master_list.append("D")
        
        for item in cube.iloc[4]:
            if item != white:
                stop = False
                break
            else:
                stop = True
                
        for thing in cube.loc['front', ['top middle','top right', 'top left']]:
            if thing != cube['base_color']['front']:
                stop = False
                break
        for thing in cube.loc['right', ['top middle','top right', 'top left']]:
            if thing != cube['base_color']['right']:
                stop = False
                break
        for thing in cube.loc['back', ['top middle','top right', 'top left']]:
            if thing != cube['base_color']['back']:
                stop = False
                break
        for thing in cube.loc['left', ['top middle','top right', 'top left']]:
            if thing != cube['base_color']['left']:
                stop = False
                break

     
    return cube


def edges(cube):
    
    '''
    completes the second row of the cube

    Parameters
    ----------
    cube: DataFrame
        input cube, set up to orient the second row edges

    Returns
    -------
    cube: DataFrame
        the cube once the second row edges are oriented
    '''
    
    yellow = cube['base_color']['bottom']
    
    # puts all edge pieces with yellow where the edge pieces without yellow should be (makes the following step easier)
    if cube['middle right']['front']!= yellow and cube['middle left']['right']!= yellow:
        while cube['bottom middle']['front'] != yellow and cube['top middle']['bottom'] != yellow:
            cube = rf.lower_clock(cube)
            master_list.append("D")
        cube = rf.lower_counter(cube)
        master_list.append("D'")
        cube = rf.right_counter(cube)
        master_list.append("R'")
        cube = rf.lower_clock(cube)
        master_list.append("D")
        cube = rf.right_clock(cube)
        master_list.append("R")
        cube = rf.lower_clock(cube)
        master_list.append("D")
        cube = rf.front_clock(cube)
        master_list.append("F")
        cube = rf.lower_counter(cube)
        master_list.append("D'")
        cube = rf.front_counter(cube)
        master_list.append("F'")

    if cube['middle right']['right']!= yellow and cube['middle left']['back']!= yellow:
        while cube['bottom middle']['right'] != yellow and cube['middle right']['bottom'] != yellow:
            cube = rf.lower_clock(cube)
            master_list.append("D")
        cube = rf.lower_counter(cube)
        master_list.append("D'")
        cube = rf.back_counter(cube)
        master_list.append("B'")
        cube = rf.lower_clock(cube)
        master_list.append("D")
        cube = rf.back_clock(cube)
        master_list.append("B")
        cube = rf.lower_clock(cube)
        master_list.append("D")
        cube = rf.right_clock(cube)
        master_list.append("R")
        cube = rf.lower_counter(cube)
        master_list.append("D'")
        cube = rf.right_counter(cube)
        master_list.append("R'")

    if cube['middle right']['back']!= yellow and cube['middle left']['left']!= yellow:
        while cube['bottom middle']['back'] != yellow and cube['bottom middle']['bottom'] != yellow:
            cube = rf.lower_clock(cube)
            master_list.append("D")
        cube = rf.lower_counter(cube)
        master_list.append("D'")
        cube = rf.left_counter(cube)
        master_list.append("L'")
        cube = rf.lower_clock(cube)
        master_list.append("D")
        cube = rf.left_clock(cube)
        master_list.append("L")
        cube = rf.lower_clock(cube)
        master_list.append("D")
        cube = rf.back_clock(cube)
        master_list.append("B")
        cube = rf.lower_counter(cube)
        master_list.append("D'")
        cube = rf.back_counter(cube)
        master_list.append("B'")
            
    if cube['middle right']['left']!= yellow and cube['middle left']['front']!= yellow:
        while cube['bottom middle']['left'] != yellow and cube['middle left']['bottom'] != yellow:
            cube = rf.lower_clock(cube)
            master_list.append("D")
        cube = rf.lower_counter(cube)
        master_list.append("D'")
        cube = rf.front_counter(cube)
        master_list.append("F'")
        cube = rf.lower_clock(cube)
        master_list.append("D")
        cube = rf.front_clock(cube)
        master_list.append("F")
        cube = rf.lower_clock(cube)
        master_list.append("D")
        cube = rf.left_clock(cube)
        master_list.append("L")
        cube = rf.lower_counter(cube)
        master_list.append("D'")
        cube = rf.left_counter(cube)
        master_list.append("L'")
            
    # put the (non-yellow) edge pieces in the correct place
    x = 0
    while x <4:
        if ((cube['base_color']['front'] == cube['bottom middle']['right'] and cube['middle right']['bottom']!= yellow) or
            (cube['base_color']['front'] == cube['bottom middle']['back'] and cube['bottom middle']['bottom']!= yellow) or
            (cube['base_color']['front'] == cube['bottom middle']['left'] and cube['middle left']['bottom']!= yellow) or
            (cube['base_color']['front'] == cube['bottom middle']['front'] and cube['top middle']['bottom']!= yellow)):

            while cube['bottom middle']['front'] != cube['base_color']['front'] and cube['top middle']['bottom']!= yellow:
                cube = rf.lower_clock(cube)
                master_list.append("D")
            if cube['top middle']['bottom'] == cube['base_color']['right']:
                cube = rf.lower_counter(cube)
                master_list.append("D'")
                cube = rf.right_counter(cube)
                master_list.append("R'")
                cube = rf.lower_clock(cube)
                master_list.append("D")
                cube = rf.right_clock(cube)
                master_list.append("R")
                cube = rf.lower_clock(cube)
                master_list.append("D")
                cube = rf.front_clock(cube)
                master_list.append("F")
                cube = rf.lower_counter(cube)
                master_list.append("D'")
                cube = rf.front_counter(cube)
                master_list.append("F'")
            else:
                cube = rf.lower_clock(cube)
                master_list.append("D")
                cube = rf.left_clock(cube)
                master_list.append("L")
                cube = rf.lower_counter(cube)
                master_list.append("D'")
                cube = rf.left_counter(cube)
                master_list.append("L'")
                cube = rf.lower_counter(cube)
                master_list.append("D'")
                cube = rf.front_counter(cube)
                master_list.append("F'")
                cube = rf.lower_clock(cube)
                master_list.append("D")
                cube = rf.front_clock(cube)
                master_list.append("F")
        
        if ((cube['base_color']['right'] == cube['bottom middle']['right'] and cube['middle right']['bottom']!= yellow) or
            (cube['base_color']['right'] == cube['bottom middle']['back'] and cube['bottom middle']['bottom']!= yellow) or
            (cube['base_color']['right'] == cube['bottom middle']['left'] and cube['middle left']['bottom']!= yellow) or
            (cube['base_color']['right'] == cube['bottom middle']['front'] and cube['top middle']['bottom']!= yellow)):

            while cube['bottom middle']['right'] != cube['base_color']['right'] and cube['middle right']['bottom']!= yellow:
                cube = rf.lower_clock(cube)
                master_list.append("D")
            if cube['middle right']['bottom'] == cube['base_color']['back']:
                cube = rf.lower_counter(cube)
                master_list.append("D'")
                cube = rf.back_counter(cube)
                master_list.append("B'")
                cube = rf.lower_clock(cube)
                master_list.append("D")
                cube = rf.back_clock(cube)
                master_list.append("B")
                cube = rf.lower_clock(cube)
                master_list.append("D")
                cube = rf.right_clock(cube)
                master_list.append("R")
                cube = rf.lower_counter(cube)
                master_list.append("D'")
                cube = rf.right_counter(cube)
                master_list.append("R'")
            else:
                cube = rf.lower_clock(cube)
                master_list.append("D")
                cube = rf.front_clock(cube)
                master_list.append("F")
                cube = rf.lower_counter(cube)
                master_list.append("D'")
                cube = rf.front_counter(cube)
                master_list.append("F'")
                cube = rf.lower_counter(cube)
                master_list.append("D'")
                cube = rf.right_counter(cube)
                master_list.append("R'")
                cube = rf.lower_clock(cube)
                master_list.append("D")
                cube = rf.right_clock(cube)
                master_list.append("R")
                
        if ((cube['base_color']['back'] == cube['bottom middle']['right'] and cube['middle right']['bottom']!= yellow) or
            (cube['base_color']['back'] == cube['bottom middle']['back'] and cube['bottom middle']['bottom']!= yellow) or
            (cube['base_color']['back'] == cube['bottom middle']['left'] and cube['middle left']['bottom']!= yellow) or
            (cube['base_color']['back'] == cube['bottom middle']['front'] and cube['top middle']['bottom']!= yellow)):

            while cube['bottom middle']['back'] != cube['base_color']['back'] and cube['bottom middle']['bottom']!= yellow:
                cube = rf.lower_clock(cube)
                master_list.append("D")
            if cube['bottom middle']['bottom'] == cube['base_color']['left']:
                cube = rf.lower_counter(cube)
                master_list.append("D'")
                cube = rf.left_counter(cube)
                master_list.append("L'")
                cube = rf.lower_clock(cube)
                master_list.append("D")
                cube = rf.left_clock(cube)
                master_list.append("L")
                cube = rf.lower_clock(cube)
                master_list.append("D")
                cube = rf.back_clock(cube)
                master_list.append("B")
                cube = rf.lower_counter(cube)
                master_list.append("D'")
                cube = rf.back_counter(cube)
                master_list.append("B'")
            else:
                cube = rf.lower_clock(cube)
                master_list.append("D")
                cube = rf.right_clock(cube)
                master_list.append("R")
                cube = rf.lower_counter(cube)
                master_list.append("D'")
                cube = rf.right_counter(cube)
                master_list.append("R'")
                cube = rf.lower_counter(cube)
                master_list.append("D'")
                cube = rf.back_counter(cube)
                master_list.append("B'")
                cube = rf.lower_clock(cube)
                master_list.append("D")
                cube = rf.back_clock(cube)
                master_list.append("B")
                
        if ((cube['base_color']['left'] == cube['bottom middle']['right'] and cube['middle right']['bottom']!= yellow) or
            (cube['base_color']['left'] == cube['bottom middle']['back'] and cube['bottom middle']['bottom']!= yellow) or
            (cube['base_color']['left'] == cube['bottom middle']['left'] and cube['middle left']['bottom']!= yellow) or
            (cube['base_color']['left'] == cube['bottom middle']['front'] and cube['top middle']['bottom']!= yellow)):

            while cube['bottom middle']['left'] != cube['base_color']['left'] and cube['middle left']['bottom']!= yellow:
                cube = rf.lower_clock(cube)
                master_list.append("D")
            if cube['middle left']['bottom'] == cube['base_color']['front']:
                cube = rf.lower_counter(cube)
                master_list.append("D'")
                cube = rf.front_counter(cube)
                master_list.append("F'")
                cube = rf.lower_clock(cube)
                master_list.append("D")
                cube = rf.front_clock(cube)
                master_list.append("F")
                cube = rf.lower_clock(cube)
                master_list.append("D")
                cube = rf.left_clock(cube)
                master_list.append("L")
                cube = rf.lower_counter(cube)
                master_list.append("D'")
                cube = rf.left_counter(cube)
                master_list.append("L'")
            else:
                cube = rf.lower_clock(cube)
                master_list.append("D")
                cube = rf.back_clock(cube)
                master_list.append("B")
                cube = rf.lower_counter(cube)
                master_list.append("D'")
                cube = rf.back_counter(cube)
                master_list.append("B'")
                cube = rf.lower_counter(cube)
                master_list.append("D'")
                cube = rf.left_counter(cube)
                master_list.append("L'")
                cube = rf.lower_clock(cube)
                master_list.append("D")
                cube = rf.left_clock(cube)
                master_list.append("L")
        x = x +1
        
    return cube


counter = 0

# a variable used to fix a bug. basically, if this section runs for too long, it will reset the entire cube and change a few 
#steps at the begining so it goes into this step differently. 
yellow_fucker = False


def yellow_cross(cube):
    
    '''
    makes the "yellow cross" on the cube. the edges don't need to be properly oriented during this step.

    Parameters
    ----------
    cube: DataFrame
        input cube, set up to form the yellow cross

    Returns
    -------
    cube: DataFrame
        the cube once the yellow cross is formed

    yellow_fucker: Boolean
        whether or not counter went to high, in which case entire code resets with slight changes to prevent an infinite loop
    '''

    yellow = cube['base_color']['bottom']
    end = False
    counter = 0
    yellow_fucker = False
    while end == False:
        if counter > 50:
            yellow_fucker = True
            break
        if (cube['top middle']['bottom'] == yellow and
            cube['bottom middle']['bottom'] == yellow and
            cube['middle right']['bottom'] == yellow and
            cube['middle left']['bottom'] == yellow):
            end = True
        elif ((cube['top middle']['bottom'] == yellow and
            cube['bottom middle']['bottom'] == yellow) or
            (cube['middle right']['bottom'] == yellow and
            cube['middle left']['bottom'] == yellow)):
            if (cube['top middle']['bottom'] == yellow and
            cube['bottom middle']['bottom'] == yellow):
                cube = rf.lower_clock(cube)
                master_list.append("D")
            cube = rf.front_clock(cube)
            master_list.append("F")
            cube = rf.left_clock(cube)
            master_list.append("L")
            cube = rf.lower_clock(cube)
            master_list.append("D")
            cube = rf.left_counter(cube)
            master_list.append("L'")
            cube = rf.lower_counter(cube)
            master_list.append("D'")
            cube = rf.front_counter(cube)
            master_list.append("F'")

        elif ((cube['top middle']['bottom'] == yellow and
               cube['middle right']['bottom'] == yellow) or
              (cube['bottom middle']['bottom'] == yellow and
               cube['middle left']['bottom'] == yellow) or
              (cube['top middle']['bottom'] == yellow and
               cube['middle left']['bottom'] == yellow) or
              (cube['middle right']['bottom'] == yellow and
               cube['bottom middle']['bottom'] == yellow)):
            while (not (cube['top middle']['bottom'] == yellow and
                     cube['middle left']['bottom'] == yellow)):
                cube = rf.lower_clock(cube)
                master_list.append("D")
            cube = rf.front_clock(cube)
            master_list.append("F")
            cube = rf.left_clock(cube)
            master_list.append("L")
            cube = rf.lower_clock(cube)
            master_list.append("D")
            cube = rf.left_counter(cube)
            master_list.append("L'")
            cube = rf.lower_counter(cube)
            master_list.append("D'")
            cube = rf.front_counter(cube)
            master_list.append("F'")

        else:
            cube = rf.front_clock(cube)
            master_list.append("F")
            cube = rf.left_clock(cube)
            master_list.append("L")
            cube = rf.lower_clock(cube)
            master_list.append("D")
            cube = rf.left_counter(cube)
            master_list.append("L'")
            cube = rf.lower_counter(cube)
            master_list.append("D'")
            cube = rf.front_counter(cube)
            master_list.append("F'")
        counter = counter +1
            
     
    return cube, yellow_fucker


def yellow_edges(cube):
    
    '''
    orients the cube's yellow edges

    Parameters
    ----------
    cube: DataFrame
        input cube, set up to orient the yellow edges

    Returns
    -------
    cube: DataFrame
        the cube once the yellow edges are oriented
    '''

    while cube['bottom middle']['front'] != cube['base_color']['front']:
            cube = rf.lower_clock(cube)
            master_list.append("D")
    x = 0
    while(not (cube['bottom middle']['front'] == cube['base_color']['front'] and
             cube['bottom middle']['right'] == cube['base_color']['right']and
             cube['bottom middle']['back'] == cube['base_color']['back'] and
             cube['bottom middle']['left'] == cube['base_color']['left'])):
        
        while cube['bottom middle']['front'] == cube['base_color']['front']:
            cube = rf.lower_clock(cube)
            master_list.append("D")
        y = 0
        while y < x:
            cube = rf.lower_clock(cube)
            master_list.append("D")
            y = y +1
            
        cube = rf.left_clock(cube)
        master_list.append("L")
        cube = rf.lower_clock(cube)
        master_list.append("D")
        cube = rf.left_counter(cube)
        master_list.append("L'")
        cube = rf.lower_clock(cube)
        master_list.append("D")
        cube = rf.left_clock(cube)
        master_list.append("L")
        cube = rf.lower_clock(cube)
        master_list.append("D")
        cube = rf.lower_clock(cube)
        master_list.append("D")
        cube = rf.left_counter(cube)
        master_list.append("L'")
        cube = rf.lower_clock(cube)
        master_list.append("D")
        x +=1
        
        while cube['bottom middle']['front'] != cube['base_color']['front']:
            cube = rf.lower_clock(cube)
            master_list.append("D")
        
    while cube['bottom middle']['front'] != cube['base_color']['front']:
        cube = rf.lower_clock(cube)
        master_list.append("D")
      
     
    return cube


def yellow_corners(cube):
    
    '''
    puts yellow corners in the right place, but not nescessarily properly oriented

    Parameters
    ----------
    cube: DataFrame
        input cube, set up to reorder the yellow corners

    Returns
    -------
    cube: DataFrame
        the cube once the yellow corners are properly reordered
    '''

    while (not(((cube['top right']['bottom'] == cube['bottom middle']['front'] or
               cube['bottom right']['front'] == cube['bottom middle']['front'] or
               cube['bottom left']['right'] == cube['bottom middle']['front'])and
              (cube['top right']['bottom'] == cube['bottom middle']['right'] or
               cube['bottom right']['front'] == cube['bottom middle']['right'] or
               cube['bottom left']['right'] == cube['bottom middle']['right']))and
               
              ((cube['bottom left']['bottom'] == cube['bottom middle']['back'] or
               cube['bottom right']['back'] == cube['bottom middle']['back'] or
               cube['bottom left']['left'] == cube['bottom middle']['back'])and
              (cube['bottom left']['bottom'] == cube['bottom middle']['left'] or
               cube['bottom right']['back'] == cube['bottom middle']['left'] or
               cube['bottom left']['left'] == cube['bottom middle']['left']))and
               
              ((cube['top left']['bottom'] == cube['bottom middle']['front'] or
               cube['bottom left']['front'] == cube['bottom middle']['front'] or
               cube['bottom right']['left'] == cube['bottom middle']['front'])and
              (cube['top left']['bottom'] == cube['bottom middle']['left'] or
               cube['bottom left']['front'] == cube['bottom middle']['left'] or
               cube['bottom right']['left'] == cube['bottom middle']['left']))and
               
              ((cube['bottom right']['bottom'] == cube['bottom middle']['back'] or
               cube['bottom left']['back'] == cube['bottom middle']['back'] or
               cube['bottom right']['right'] == cube['bottom middle']['back'])and
              (cube['bottom right']['bottom'] == cube['bottom middle']['right'] or
               cube['bottom left']['back'] == cube['bottom middle']['right'] or
               cube['bottom right']['right'] == cube['bottom middle']['right'])))):
        x = 0
        while x <4:
            if((cube['top left']['bottom'] == cube['bottom middle']['front'] or
               cube['bottom left']['front'] == cube['bottom middle']['front'] or
               cube['bottom right']['left'] == cube['bottom middle']['front'])and
              (cube['top left']['bottom'] == cube['bottom middle']['left'] or
               cube['bottom left']['front'] == cube['bottom middle']['left'] or
               cube['bottom right']['left'] == cube['bottom middle']['left'])):
                break
            master_list.append("D")
            cube = rf.lower_clock(cube)
            x +=1
            
        cube = rf.lower_clock(cube)
        master_list.append("D")
        cube = rf.left_clock(cube)
        master_list.append("L")
        cube = rf.lower_counter(cube)
        master_list.append("D'")
        cube = rf.right_counter(cube)
        master_list.append("R'")
        cube = rf.lower_clock(cube)
        master_list.append("D")
        cube = rf.left_counter(cube)
        master_list.append("L'")
        cube = rf.lower_counter(cube)
        master_list.append("D'")
        cube = rf.right_clock(cube)
        master_list.append("R")
        
    while cube['bottom middle']['front'] != cube['middle middle']['front']:
        cube = rf.lower_clock(cube)
        master_list.append("D")
     
        
    return cube


def final(cube):
     
    '''
    the technical last step of cube solving, which orients the yellow corners

    Parameters
    ----------
    cube: DataFrame
        input cube, set up to orient the yellow corners

    Returns
    -------
    cube: DataFrame
        the cube once the yellow corners are properly oriented
    '''

    x = 0
    done = False
    while done == False:
        done = True
        if (cube['top right']['bottom'] != cube['base_color']['bottom'] or
            cube['top left']['bottom'] != cube['base_color']['bottom'] or
            cube['top middle']['bottom'] != cube['base_color']['bottom'] or
            cube['bottom right']['bottom'] != cube['base_color']['bottom'] or
            cube['middle right']['bottom'] != cube['base_color']['bottom'] or
            cube['bottom left']['bottom'] != cube['base_color']['bottom'] or
            cube['middle left']['bottom'] != cube['base_color']['bottom'] or
            cube['bottom middle']['bottom'] != cube['base_color']['bottom']):
                done = False
        if done == True:
             
            return cube
        else:
            if x == 0:
                if cube['top left']['bottom'] != cube['base_color']['bottom']:
                    x = 1
                elif cube['top right']['bottom'] != cube['base_color']['bottom']:
                    x = 2
                elif cube['bottom right']['bottom'] != cube['base_color']['bottom']:
                    x = 3
                else:
                    x = 4
            
            elif x == 1:
                while cube['top left']['bottom'] == cube['base_color']['bottom']:
                    cube = rf.lower_clock(cube)
                    master_list.append("D")
                while cube['top left']['bottom'] != cube['base_color']['bottom']:
                    cube = rf.left_counter(cube)
                    master_list.append("L'")
                    cube = rf.upper_counter(cube)
                    master_list.append("U'")
                    cube = rf.left_clock(cube)
                    master_list.append("L")
                    cube = rf.upper_clock(cube)
                    master_list.append("U")

            elif x == 2:
                while cube['top right']['bottom'] == cube['base_color']['bottom']:
                    cube = rf.lower_clock(cube)
                    master_list.append("D")
                while cube['top right']['bottom'] != cube['base_color']['bottom']:
                    cube = rf.front_counter(cube)
                    master_list.append("F'")
                    cube = rf.upper_counter(cube)
                    master_list.append("U'")
                    cube = rf.front_clock(cube)
                    master_list.append("F")
                    cube = rf.upper_clock(cube)
                    master_list.append("U")

            elif x == 3:
                while cube['bottom right']['bottom'] == cube['base_color']['bottom']:
                    cube = rf.lower_clock(cube)
                    master_list.append("D")
                while cube['bottom right']['bottom'] != cube['base_color']['bottom']:
                    cube = rf.right_counter(cube)
                    master_list.append("R'")
                    cube = rf.upper_counter(cube)
                    master_list.append("U'")
                    cube = rf.right_clock(cube)
                    master_list.append("R")
                    cube = rf.upper_clock(cube)
                    master_list.append("U")
                        
            else:
                while cube['bottom left']['bottom'] == cube['base_color']['bottom']:
                    cube = rf.lower_clock(cube)
                    master_list.append("D")
                while cube['bottom left']['bottom'] != cube['base_color']['bottom']:
                    cube = rf.back_counter(cube)
                    master_list.append("B'")
                    cube = rf.upper_counter(cube)
                    master_list.append("U'")
                    cube = rf.back_clock(cube)
                    master_list.append("B")
                    cube = rf.upper_clock(cube)
                    master_list.append("U")
                    
    return cube


def final_touches(cube):
    
    '''
    the actual last step, which rotates the top and bottom of the cube until it is fully solved

    Parameters
    ----------
    cube: DataFrame
        input cube, set up for the final step

    Returns
    -------
    cube: DataFrame
        the fully solved cube
    '''
    
    while cube['top middle']['front'] != cube['base_color']['front']:
        cube = rf.upper_clock(cube)
        master_list.append("U")
    while cube['bottom middle']['front'] != cube['base_color']['front']:
        cube = rf.lower_clock(cube)
        master_list.append("D")
    return cube
