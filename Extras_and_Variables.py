#includes extra functions and variables, including those used in test files
import pandas as pd
import random as rand
from Functions import Ref_Functions as rf
from Classes import Cube_Class as cc

# makes a list of all possible turns and what their outputs are
function_list = [rf.front_clock, rf.front_counter,
                 rf.right_clock, rf.right_counter,
                 rf.back_clock, rf.back_counter,
                 rf.left_clock, rf.left_counter,
                 rf.upper_clock, rf.upper_counter,
                 rf.lower_clock, rf.lower_counter]
function_dict = {rf.front_clock: "F", rf.front_counter: "F'",
                 rf.right_clock: "R", rf.right_counter: "R'",
                 rf.back_clock: "B", rf.back_counter: "B'",
                 rf.left_clock: "L", rf.left_counter: "L'",
                 rf.upper_clock: "U", rf.upper_counter: "U'",
                 rf.lower_clock: "D", rf.lower_counter: "D'"}


def randomize_functions(cube):
    
    '''
    does a single random turn on a cube

    Parameters
    ----------
    cube: DataFrame
        input cube

    Returns
    -------
    cube: DataFrame
        cube after random turn

    str(function_dict[choice]) : string
        the name of the random function used
    '''
    
    choice = rand.choice(function_list)
    cube = choice(cube)
    return cube, str(function_dict[choice])


# a refrence for a solved cube, used in test files and functions
solved_cube = pd.DataFrame({'top left': {'front': 'g',
  'right': 'r',
  'back': 'b',
  'left': 'o',
  'top': 'w',
  'bottom': 'y'},
 'top middle': {'front': 'g',
  'right': 'r',
  'back': 'b',
  'left': 'o',
  'top': 'w',
  'bottom': 'y'},
 'top right': {'front': 'g',
  'right': 'r',
  'back': 'b',
  'left': 'o',
  'top': 'w',
  'bottom': 'y'},
 'middle left': {'front': 'g',
  'right': 'r',
  'back': 'b',
  'left': 'o',
  'top': 'w',
  'bottom': 'y'},
 'middle middle': {'front': 'g',
  'right': 'r',
  'back': 'b',
  'left': 'o',
  'top': 'w',
  'bottom': 'y'},
 'middle right': {'front': 'g',
  'right': 'r',
  'back': 'b',
  'left': 'o',
  'top': 'w',
  'bottom': 'y'},
 'bottom left': {'front': 'g',
  'right': 'r',
  'back': 'b',
  'left': 'o',
  'top': 'w',
  'bottom': 'y'},
 'bottom middle': {'front': 'g',
  'right': 'r',
  'back': 'b',
  'left': 'o',
  'top': 'w',
  'bottom': 'y'},
 'bottom right': {'front': 'g',
  'right': 'r',
  'back': 'b',
  'left': 'o',
  'top': 'w',
  'bottom': 'y'},
 'base_color': {'front': 'g',
  'right': 'r',
  'back': 'b',
  'left': 'o',
  'top': 'w',
  'bottom': 'y'}})


# makes a random cube, used in test files
def random_cube(turns = 50):
    
    '''
    makes a random cube, used in test files

    Parameters
    ----------
    turns: int
        number of random moves the cube should have

    Returns
    -------
    randcube: DataFrame
        a random cube, with turns number of random turns from a solved cube
    '''

    randcube = cc.Cube(solved_cube)
    randcube = randcube.randomize(turns)
    return randcube


#makes sure the output cube matches the solved cube. used in test files
def test_1(test):
    
    '''
    makes sure the output cube matches the solved cube. used in test files.

    Parameters
    ----------
    test: DataFrame
        the output cube from running the solve_cube function

    Returns
    -------
    Boolean
        whether or not the input cube is actually solved
    '''

    for thing in test.loc['front', ['top left', 'top middle', 'top right',
                               'middle left', 'middle middle', 'middle right',
                               'bottom left', 'bottom middle', 'bottom right']]:
            if thing != test['base_color']['front']:
                return False
        
    for thing in test.loc['right', ['top left', 'top middle', 'top right',
                               'middle left', 'middle middle', 'middle right',
                               'bottom left', 'bottom middle', 'bottom right']]:
            if thing != test['base_color']['right']:
                return False

    for thing in test.loc['back', ['top left', 'top middle', 'top right',
                               'middle left', 'middle middle', 'middle right',
                               'bottom left', 'bottom middle', 'bottom right']]:
            if thing != test['base_color']['back']:
                return False
        
    for thing in test.loc['left', ['top left', 'top middle', 'top right',
                               'middle left', 'middle middle', 'middle right',
                               'bottom left', 'bottom middle', 'bottom right']]:
            if thing != test['base_color']['left']:
                return False

    for thing in test.loc['top', ['top left', 'top middle', 'top right',
                               'middle left', 'middle middle', 'middle right',
                               'bottom left', 'bottom middle', 'bottom right']]:
            if thing != test['base_color']['top']:
                return False
        
    for thing in test.loc['bottom', ['top left', 'top middle', 'top right',
                               'middle left', 'middle middle', 'middle right',
                               'bottom left', 'bottom middle', 'bottom right']]:
            if thing != test['base_color']['bottom']:
                return False
    return True


def test_2(string, cube):
    
    '''
    makes sure the output string gives the correct instructions to get to the output cube. used in test files

    Parameters
    ----------
    string: String
        list of instructions to solve a cube

    cube: DataFrame
        unsolved cube

    Returns
    -------
    test_1(cube): Boolean
        whether or not the instructions, when applied to the inputed cube, will solve the cube
    '''
    
    x = 0
    y = 1
    while y < len(string):
        if string[y] == "'":
            pull = string[x] + string[y]
            fun = function_list[list(function_dict.values()).index(pull)]
            cube = fun(cube)
            y += 3
            x += 3
        else:
            fun = function_list[list(function_dict.values()).index(string[x])]
            cube = fun(cube)
            y += 2
            x += 2
    return test_1(cube)
            
                
