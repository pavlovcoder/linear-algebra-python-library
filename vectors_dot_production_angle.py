print(
  '-----------------------------------------\n'\
  'Python Library for Linear Algebra Operations | Calculating dot productions and angles for entered vectors:\n'\
  '-----------------------------------------\n'
  )

print(
  'Task:\n'\
  '-----------------------------------------\n'\
  'Write a simple Python module for calculating dot productions and angles on the radians and degrees between two entered user\'s vectors (V) and (W):\n'
  )

print(
  'Solution:\n'\
  '-----------------------------------------'\
  )

import math

#Default function for handling execution loop:
def execution_loop():
  data = int(input("Do you want to try again ? Enter [1] - for continue / [0] - for quit :\n>>>"))
  if data == 1:
    return True
  elif data == 0:
    return False
  else:
    print('Error, you entered incorrect command. Please, try again...')
    execution_loop()

#Default parameters for handling execution loop:
again_exec = True
counter_exec = 0

#Default loop for handling execution:
while again_exec:

  again_exec = execution_loop()
  counter_exec = counter_exec + 1

  #The end of execution:
  if again_exec == False:
    print("Program was executed: ", counter_exec, ' times.')
    break

print(
  '\n-----------------------------------------\n'\
  'Copyright 2019 Vladimir Pavlov. All Rights Reserved.\n'\
  '-----------------------------------------'
  )