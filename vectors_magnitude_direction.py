print(
  '-----------------------------------------\n'\
  'Python Library for Linear Algebra Operations | Calculating Vector\'s parameters:\n'\
  '-----------------------------------------\n'
  )

print(
  'Task:\n'\
  '-----------------------------------------\n'\
  'Write a simple Python module for calculating magnitude and directions of entered user\'s  vectors:\n'
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
    print("Error: you entered incorrect command. Please, try again...")
    execution_loop()

def vector_loop():
  data = int(input("Do you want to add a new coordinate ? Enter:\n[2] - for adding a new coordinate;\n[1] - for adding a new vector;\n[0] - for open operations panel\n>>>"))
  if data == 2:
    return 2
  elif data == 1:
    return 1
  elif data == 0:
    return 0
  else:
    print("Error: you entered incorrect command. Please, try again...")
    vector_loop()

def vector_loop_max():
  data = int(input("Do you want to add a new vector ? Enter:\n[1] - for adding a new vector;\n[0] - for open operations panel\n>>>"))
  if data == 1:
    return 1
  elif data == 0:
    return 0
  else:
    print("Error: you entered incorrect command. Please, try again...")
    vector_loop_max()

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
            raise TypeError('The coordinates must be an iterable')

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

#Function for loop-creating new vectors using user's data:
def vectors_loop_creating():
    vectors = []
    vector_counter = 1
    coordinate_counter = 1
    vector_input_control = True
    while vector_input_control:
      #print("Please, enter all coordinates of the %d vector:" % vector_counter)
      #print(f'Please, enter all coordinates of the {vector_counter}-vector:')
      #print(f"Please, enter all coordinates of the {vector_counter}-vector:")
      print("Please, enter all coordinates of the %d-vector" % vector_counter)
      vector = []
      coordinate_counter = 1
      coordinate_input_control = True
      while coordinate_input_control:
        #print("Please, enter %d-st coordinate:" % coordinate_counter)
        #print(f'Please, enter {coordinate_counter}-st coordinate:')
        print("Please, enter %d-st coordinate:" % coordinate_counter)
        vector.append(float(input(">>>")))
        if len(vector) == 3:
          #print("You almost entered the maximum number of coordinates on the %d-vector." % vector_counter)
          #print(f'You almost entered the maximum number of coordinates on the {vector_counter}-vector. The maximum number of coordinates should be less of equal to 3.')
          print("You almost entered the maximum number of coordinates on the %d-vector. The maximum number of coordinates should be less of equal to 3." % vector_counter)
          coordinate_input_control = False
          data = vector_loop_max()
          if data == 1:
            vector_input_control = True
          else:
            vector_input_control = False
          break
        data = vector_loop()
        if data == 2:
          coordinate_input_control = True
        elif data == 1:
          coordinate_input_control = False
          break
        else:
          coordinate_input_control = False
          vector_input_control = False
          break
        coordinate_counter = coordinate_counter + 1
      vector_counter = vector_counter + 1
      print("You entered vector with coordinates: ", vector)
      vectors.append(Vector(vector))
    return vectors

#Function for handling all operations on the vectors:
def vectors_operations_handling(vectors):
  print("You entered vectors with coordinates:")
  v_counter = 0
  for vector in vectors:
    print('{0}: '.format(v_counter + 1))
    print(vector)
    v_counter = v_counter + 1

#Function for calculating magnitude of entered vectors:
def vectors_magnitude_calc(vectors):
  index = 1
  for vector in vectors:
    print('Calculations for vector-{0}:\nMagnitude = {1}\nNormalization = {2}'.format(index, vector.magnitude(), vector.normalized()))
    index += 1

#Function for calculating dot production 
'''
def vectors_magnitude_calc(vectors):
  magnitudes = []
  directions = []
  c_sum = 0
  for vector in vectors:
    for coord in vector.coordinates:
      c_sum += math.pow(coord, 2)
    magnitudes.append(math.sqrt(c_sum))
    direction = []
    for coord in vector.coordinates:
      direction.append(coord / math.sqrt(c_sum))
    directions.append(direction)
    c_sum = 0
  print('Calculated magnitudes of vectors:')
  print(magnitudes)
  print('Calculated directions of vectors:')
  print(directions)

'''

#Default parameters for handling execution loop:
again_exec = True
counter_exec = 0

#Default loop for handling execution:
while again_exec:
  vectors = []
  vectors = vectors_loop_creating()
  vectors_operations_handling(vectors)
  vectors_magnitude_calc(vectors)
  again_exec = execution_loop()
  counter_exec = counter_exec + 1

  #The end of execution:
  if again_exec == False:
    print("Program was executed: ",counter_exec, ' times.')
    break


print(
  '\n-----------------------------------------\n'\
  'Copyright 2019 Vladimir Pavlov. All Rights Reserved.\n'\
  '-----------------------------------------'
  )