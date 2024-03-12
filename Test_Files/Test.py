
from Test_Files import Extras_and_Variables as eav
from Functions import Solve_a_Cube as sac
from Functions import Ref_Functions as rf
import pandas as pd

test = eav.random_cube()
save = test.copy(deep = True)
test = sac.solve_cube(save)
assert eav.test_1(test[0])
print("test passed")
assert eav.test_2(test[1], save)
print("test passed")

test = eav.solved_cube
save = test.copy(deep = True)
test = sac.solve_cube(save)
assert eav.test_1(test[0])
print("test passed")
assert eav.test_2(test[1], save)
print("test passed")
test = pd.DataFrame(
{'top left': {'front': 'w',
  'right': 'r',
  'back': 'b',
  'left': 'o',
  'top': 'b',
  'bottom': 'g'},
 'top middle': {'front': 'g',
  'right': 'r',
  'back': 'b',
  'left': 'o',
  'top': 'w',
  'bottom': 'y'},
 'top right': {'front': 'g',
  'right': 'r',
  'back': 'y',
  'left': 'o',
  'top': 'w',
  'bottom': 'y'},
 'middle left': {'front': 'w',
  'right': 'r',
  'back': 'b',
  'left': 'o',
  'top': 'b',
  'bottom': 'g'},
 'middle middle': {'front': 'g',
  'right': 'r',
  'back': 'b',
  'left': 'o',
  'top': 'w',
  'bottom': 'y'},
 'middle right': {'front': 'g',
  'right': 'r',
  'back': 'y',
  'left': 'o',
  'top': 'w',
  'bottom': 'y'},
 'bottom left': {'front': 'w',
  'right': 'r',
  'back': 'b',
  'left': 'o',
  'top': 'b',
  'bottom': 'g'},
 'bottom middle': {'front': 'g',
  'right': 'r',
  'back': 'b',
  'left': 'o',
  'top': 'w',
  'bottom': 'y'},
 'bottom right': {'front': 'g',
  'right': 'r',
  'back': 'y',
  'left': 'o',
  'top': 'w',
  'bottom': 'y'},
 'base_color': {'front': 'g',
  'right': 'r',
  'back': 'b',
  'left': 'o',
  'top': 'w',
  'bottom': 'y'}})

assert eav.test_1(rf.left_counter(test))
print("test passed")
