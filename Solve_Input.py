from Functions import Step_Functions as sf
from Classes import Cube_Class as cc
from Functions import Solve_a_Cube as sac

def solve_input():
    
    '''
    uses the solve_cube function from the Solve_a_Cube file so that the user uses the option to input the color of each square on
    the cube individually

    Parameters
    ----------
    none

    Returns
    -------
    mac.cube: DataFrame
        solved cube
    '''
    
    print('''Welcome to Rubik's Cube solver (not affiliated with the Rubik's Cube brand at all in any way whatsoever)! This cube
    solver will give you a solution to your cube, but not the perfect solution. To start off, input the colors of each square on
    your cube. You don't need to use the full color names. You will have a chance to fix the names if you mess up, so don't worry 
    too much about it.''')
          
    mac = cc.Cube()

    print(mac.cube)

    print(''' if any part of this cube looks incorrect, make sure to type 'no' below. If your cube is incorrect, not only will
    the output be incorrect, it could get the code stuck.''')
    
    mac.fix_cube()

    sac.solve_cube(mac.cube)