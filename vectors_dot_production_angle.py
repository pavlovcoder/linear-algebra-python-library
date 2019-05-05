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

import os, sys
import math
import random

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

#Module for handling wrong data entered by user, along entering appropriate command:
class UnAcceptedValueError(Exception):
  def __init__(self, data):
    self.data = data
  def __str__(self):
    return repr(self.data)

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
    return self.coordinates == v.coordinates

V_length = 0
vector = []
#Function for loop creating new vectors using users data:
def vector_creating(name, prev_len):
  #print('Please, enter all coordinates for %d-vector:\n' % name)
  print('Please, enter all coordinates for vector: ', name)
  coordinate_input_control = True
  coordinate_counter = 1
  if (name == 'V'):  
    while coordinate_input_control:
      vector_coordinate_input(coordinate_counter)
      #vector.append(vector_coordinate_input(coordinate_counter))
      if (vector_input_handler() == 1):
        coordinate_counter = coordinate_counter + 1
        print('Vector after coordinate creating:')
        print(vector)
      else:
        coordinate_input_control = False
        V_length = len(vector)
        print('You entered vector: {0} with {1} coordinates.'.format(vector, V_length))
  else:
    print('Function for creating coordinates for the W-vector was called!')
    for coordinate in range(prev_len):
      vector_coordinate_input(coordinate_counter)
      print('Vector after coordinate creating:')
      print(vector)
      if (prev_len - coordinate_counter) != 0:
        print('You should still enter {0} coordinates.'.format(prev_len - coordinate_counter)) 
      coordinate_counter = coordinate_counter + 1
  return vector

  '''
  else:
    print('Vector')
    print('Size of the previous vector = %d' % prev_len)
  '''

def vector_input_handler():
  print('Please, enter an appropriate command number for continuing:')
  print('[1] - for adding a new coordinate to the vector;')
  print('[2] - for complete adding new elements and start creating a new vector;')
  try:
    user_handle = int(input(">>>"))
    if (user_handle == 1):
      return 1
    elif (user_handle == 2):
      return 2
    else:
      raise UnAcceptedValueError('You entered command number is out of range. Please try again...')
      vector_input_handler()
  except SyntaxError:
    print('You cannot leave command field empty. Please, try again...')
    vector_input_handler()
  except KeyboardInterrupt:
    print('You cannot quit the program here. Please, try again...')
    vector_input_handler()
  except UnAcceptedValueError as e:
    print(e.data)
    vector_input_handler()
  except:
    print('Command should be only a number. Please, try again...')
    vector_input_handler()

def vector_coordinate_input(coordinate_counter):
  c_counter = coordinate_counter
  print('Please, enter a %d-coordinate for vector:' % c_counter)
  try:
    user_coordinate = float(input(">>>"))
    vector.append(user_coordinate)
  except SyntaxError:
    print('You cannot leave coordinate-field empty. Please, try enter any number... ')
    vector_coordinate_input(c_counter)
  except KeyboardInterrupt:
    print('You cannot quit from the program here. Please, try enter any number...')
    vector_coordinate_input(c_counter)
  except:
    print('Coordinate of the vector should be only number. Please, try enter any number...')
    vector_coordinate_input(c_counter)

def vectors_production(V, W, size):
  v_production = []
  for index in range(size):
    v_production.append(V.coordinates[index] * W.coordinates[index])
  return sum(v_production)

#Default parameters for handling execution loop:
again_exec = True
counter_exec = 0

#Default loop for handling execution:
while again_exec:
  V = vector_creating('V', 0)
  vector = []
  vector_length = len(V)
  W = vector_creating('W', vector_length)
  V = Vector(V)
  W = Vector(W)
  v_production = vectors_production(V, W, vector_length)
  #math_statement = v_production / (V.magnitude() * W.magnitude())
  math_statement = round((v_production / (V.magnitude() * W.magnitude())), 3)
  try:
    #angle = math.acos(math_statement)
    angle = round(math.acos(math_statement), 3)
  except:
    print('Sorry, but your entered coordinates of vectors are too large...')
  print('1. V * W = {0}'.format(v_production))
  print('2. Angle between vectors V and W: {0} (rad) and {1} (degree)'.format(angle, round(math.degrees(angle), 3)))
  #Temporal data for testing a few lines of syntax on the Python:
  '''
  n_points = 10
  split = int(0.75*n_points)
  print('split = {0}'.format(split))
  grade = [random.random() for ii in range(0, n_points)]
  bumpy = [random.random() for ii in range(0, n_points)]
  X = [[gg, ss] for gg, ss in zip(grade, bumpy)]
  X_train = X[0:split]
  X_test = X[split:]
  print('X_train:')
  print(X_train)
  print('X_test:')
  print(X_test)
  '''
  vector = []
  V = []
  W = []
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