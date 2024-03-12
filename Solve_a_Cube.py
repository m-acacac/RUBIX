from Functions import Ref_Functions as rf
from Classes import Cube_Class as cc
from Functions import Step_Functions as sf
import random
from Test_Files import Extras_and_Variables as eav


def solve_cube(cube):
    
    '''
    key function that combines the steps for solving an entire cube from start to finish

    Parameters
    ----------
    cube: DataFrame
        input (scrambled) cube, to be solved

    Returns
    -------
    cube: DataFrame
        solved cube

    output: String
        list of moves needed to solve the cube
    '''

    print("Loading" , end = '')
    save_cube = cube.copy(deep = True)
    go_again = True
    sf.master_list = []
    while go_again == True:
        x = 1
        
        #runs step functions in order
        while x == 1:
            cube = sf.daisy(cube)
            print ('.', end = '')
            cube = sf.white_cross(cube)
            print ('.', end = '')
            cube = sf.top_layer(cube)
            print ('.', end = '')
            cube = sf.edges(cube)
            print ('.', end = '')
            cross = sf.yellow_cross(cube)
            cube = cross[0]
            yellow_fucker = cross[1]
            
            #fixes a bug that occurs during the yellow cross step
            if yellow_fucker:
                sf.master_list = []
                cube = save_cube.copy(deep = True)
                rand = eav.randomize_functions(cube)
                cube = rand[0]
                sf.master_list.append(rand[1])
                rand = eav.randomize_functions(cube)
                cube = rand[0]
                sf.master_list.append(rand[1])
                rand = eav.randomize_functions(cube)
                cube = rand[0]
                sf.master_list.append(rand[1])
                rand = eav.randomize_functions(cube)
                cube = rand[0]
                sf.master_list.append(rand[1])
                go_again = True
                break
            print ('.', end = '')
            cube = sf.yellow_edges(cube)
            print ('.', end = '')
            cube = sf.yellow_corners(cube)
            print ('.', end = '')
            cube = sf.final(cube)
            print ('.', end = '')
            cube = sf.final_touches(cube)
            print ('.', end = '')
            go_again = False
            break

    #the following steps simplify the output (get rid of the majority of repetative moves)
    working_list_1 = []
    working_list_2 = []
    working_list_3 = []
    output = ""

    w = 0
    x = 1
    y = 2
    z = 3

    while z < len(sf.master_list):
        if (sf.master_list[w] == sf.master_list[x] and
            sf.master_list[x] == sf.master_list[y] and
            sf.master_list[y] == sf.master_list[z]):
            w += 4
            x += 4
            y += 4
            z += 4
        elif (sf.master_list[w] == sf.master_list[x] and
              sf.master_list[x] == sf.master_list[y]):
            if "'" in sf.master_list[w]:
                working_list_1.append(str((sf.master_list[w])[0]))
                w += 3
                x += 3
                y += 3
                z += 3
            else:
                working_list_1.append(str(sf.master_list[w] + "'"))
                w += 3
                x += 3
                y += 3
                z += 3
        elif (sf.master_list[w] == sf.master_list[x] + "'" or
              sf.master_list[x] == sf.master_list[w] + "'"):
            w += 2
            x += 2
            y += 2
            z += 2
        else:
            working_list_1.append(sf.master_list[w])
            w += 1
            x += 1
            y += 1
            z += 1
            
    print ('.', end = '')
    while w <len(sf.master_list):
        working_list_1.append(sf.master_list[w])
        w = w +1


    w = 0
    x = 1
    y = 2
    z = 3

    while z < len(working_list_1):
        if (working_list_1[w] == working_list_1[x] and
            working_list_1[x] == working_list_1[y] and
            working_list_1[y] == working_list_1[z]):
            w += 4
            x += 4
            y += 4
            z += 4
        elif (working_list_1[w] == working_list_1[x] and
              working_list_1[x] == working_list_1[y]):
            if "'" in working_list_1[w]:
                working_list_3.append(str((working_list_1[w])[0]))
                w += 3
                x += 3
                y += 3
                z += 3
            else:
                working_list_3.append(str(working_list_1[w] + "'"))
                w += 3
                x += 3
                y += 3
                z += 3
        elif (working_list_1[w] == working_list_1[x] + "'" or
              working_list_1[x] == working_list_1[w] + "'"):
            w += 2
            x += 2
            y += 2
            z += 2
        else:
            working_list_3.append(working_list_1[w])
            w += 1
            x += 1
            y += 1
            z += 1
    while w <len(working_list_1):
        working_list_3.append(working_list_1[w])
        w = w +1

        
    w = 0
    x = 1
    y = 2
    z = 3

    print ('.', end = '')
    while z < len(working_list_3):
        if (working_list_3[w] == working_list_3[x] and
            working_list_3[x] == working_list_3[y] and
            working_list_3[y] == working_list_3[z]):
            w += 4
            x += 4
            y += 4
            z += 4
        elif (working_list_3[w] == working_list_3[x] and
              working_list_3[x] == working_list_3[y]):
            if "'" in working_list_3[w]:
                working_list_2.append(str((working_list_3[w])[0]))
                w += 3
                x += 3
                y += 3
                z += 3
            else:
                working_list_2.append(str(working_list_3[w] + "'"))
                w += 3
                x += 3
                y += 3
                z += 3
        elif (working_list_3[w] == working_list_3[x] + "'" or
              working_list_3[x] == working_list_3[w] + "'"):
            w += 2
            x += 2
            y += 2
            z += 2
        else:
            working_list_2.append(working_list_3[w])
            w += 1
            x += 1
            y += 1
            z += 1
    while w <len(working_list_3):
        working_list_2.append(working_list_3[w])
        w = w +1
        
        
        
    w = 0
    x = 1
    y = 2
    z = 3

    print ('.', end = '')
    while z < len(working_list_2):
        if (working_list_2[w] == working_list_2[x] and
            working_list_2[x] == working_list_2[y] and
            working_list_2[y] == working_list_2[z]):
            w += 4
            x += 4
            y += 4
            z += 4
        elif (working_list_2[w] == working_list_2[x] and
              working_list_2[x] == working_list_2[y]):
            if "'" in working_list_2[w]:
                output += (str((working_list_2[w])[0])) + ' '
                w += 3
                x += 3
                y += 3
                z += 3
            else:
                output += (str(working_list_1[w] + "'")) + ' '
                w += 3
                x += 3
                y += 3
                z += 3

        elif (working_list_2[w] == working_list_2[x] + "'" or
              working_list_2[x] == working_list_2[w] + "'"):
            w += 2
            x += 2
            y += 2
            z += 2
        else:
            output += working_list_2[w] + " "
            w += 1
            x += 1
            y += 1
            z += 1
    while w <len(working_list_2):
        output += working_list_2[w] + " "
        w = w +1


    print('')
    print('')
    print(output)
    print("solution complete")
    return cube, output
