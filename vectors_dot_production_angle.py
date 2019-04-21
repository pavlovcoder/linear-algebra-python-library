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

#Module for creating a simple mathematical vectors on the dimension:
class Vector(object):
  def __init__(self, coordinates):
    try:
      if not coordinates:
        raise ValueError
      self.coordinates = tuple(coordinates)
      self.dimension = len(coordinates)

    except ValueError:
      raise ValueError('The coordinates must be nonempty')

    except TypeError:
      raise ValueError('The coordinate must be an iterable')

  def magnitude(self):
    coordinates_squared = [x**2 for x in self.coordinates]
    return math.sqrt(sum(coordinates_squared))

  def normalized(self):
    try:
      magnitude = self.magnitude()
      return [x * (1 / magnitude) for x in self.coordinates]

    except ZeroDivisionError:
      raise Exception('Cannot normalize the zero vector.')

  def __str__(self):
    return 'Vector {}'.format(self.coordinates)

  def __eq__(self, v):
    return self.coordinates = v.coordinates

#Function for loop-creating new vectors using users data:
def vector_creating(name):
  print('Please, enter all coordinates for %d-vector:\n' % name)
  vector = []
  coordinate_input_control = True
  coordinate_counter = 1
  if (name == 'V'):  
    while coordinate_input_control:
      print('Please, enter %d-st coordinate:' % coordinate_counter)
      vector.append(vector_coordinate_input(coordinate_counter))
      try:
        user_handle = int(input(">>>"))
      except ValueError:
        print("You should enter a number [1] or [2] for handling. Please, try again...")
  else:
    print('Vector')

    

def vector_coordinate_input(coordinate_counter):
  c_counter = coordinate_counter
  try:
    user_coordinate = float(input(">>>"))
  except ValueError:
    print("Coordinate of the vector, must be only a number. Please, try again...")
    vector_coordinate_input(c_counter)
  except SyntaxError:
    print("Coordinate of the vector shouldn't be empty. Please, try again...")
    vector_coordinate_input(c_counter)
  return user_coordinate


#Default parameters for handling execution loop:
again_exec = True
counter_exec = 0

#Default loop for handling execution:
while again_exec:

  V = vector_creating('V')
  W = vector_creating('W')
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