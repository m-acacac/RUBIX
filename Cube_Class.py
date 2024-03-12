from Test_Files import Extras_and_Variables as eav
import pandas as pd
class Cube:
    
    ''' 
    This class allows a user to input a dataframe of a cube or be prompted inputs to build a cube themselves. This is the basis
    for the entire code, as it creates the cube that the computer stores internally

    Parameters
    ----------
    insert : DataFrame, optional(default = empty DataFrame)
        a cube with the specific color values for the complete object. If inputed as empty, user is asked to individualy input
        the color value for each cube location

    Methods
    -------
    fix_cube:
        allows a user to fix mistakes with their inputed cube without re-inputing the entire cube

    randomize:
        moves self.cube a specified number of random turns  
    '''
    
    def __init__(self, insert = pd.DataFrame()):
        
        if not insert.empty:
            self.cube = insert.copy(deep = True)
         
        # allows a user to individually input the colors for each side of a cube
        else:
            face1 = {}
            face2 = {}
            face3 = {}
            face4 = {}
            face5 = {}
            face6 = {}
            faces = [face1, face2, face3, face4, face5, face6]
            locations = ['front', 'right', 'back', 'left', 'top', 'bottom']

            for item,name in zip(faces, locations):
                print('')
                print(name)
                item['top left'] = input('top left: ')
                item['top middle'] = input('top middle: ')
                item['top right'] = input('top right: ')
                item['middle left'] = input('middle left: ')
                item['middle middle'] = input('middle middle: ')
                item['middle right'] = input('middle right: ')
                item['bottom left'] = input('bottom left: ')
                item['bottom middle'] = input('bottom middle: ')
                item['bottom right'] = input('bottom right: ')
                item['base_color'] = item['middle middle']

            self.cube = pd.DataFrame(faces, locations)
            
    # used when a user manually inputs their cube to allow them to fix the cube without entirely restarting the program
    def fix_cube(self):
        fix = input("Does this look right? ")
        if fix != 'yes':
            keep_asking = True
            while keep_asking:
                position = input("Position: ")
                face = input("Face: ")
                color = input("New Color: ")
                self.cube[position][face] = color
                print (self.cube)
                fix = input("Are you finished fixing the cube? ")
                if fix != 'yes':
                    keep_asking = True
                else:
                    keep_asking = False
        else:
            keep_asking = False
            
            
    # randomly does x moves (rotations) on the cube. Used for tests. 
    def randomize(self, rotations = 50):
        x = 0
        while x < rotations:
            self.cube = eav.randomize_functions(self.cube)[0]
            x = x +1
        return self.cube
        
