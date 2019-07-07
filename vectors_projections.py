print(
  '-----------------------------------------\n'\
  'Python Library for Linear Algebra Operations | Calculating projections of the entered vectors by user\n'\
  '-----------------------------------------\n'
  )

print(
  'Task:\n'\
  '-----------------------------------------\n'\
  'Write a simple Python module for calculating all necessary parameters projections of the entered vectors by user. You should calculate: \n- proj b (V) ;\n- orthogonal vector (V) ;\n- length of vector (V) ;\n'
  )

print(
  'Solution:\n'\
  '-----------------------------------------'\
  )

import os, sys, math

# Module for handling wrong data entered by user, along entering appropriate command:
class UnAcceptedValueError(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)

# Module for creating a simple mathematical vectors on the dimension:
class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinate must be nonempty')

        except TypeError:
            raise ValueError('The coordinates must be an iterable')

    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return math.sqrt(sum(coordinates_squared))

    def normalized(self):
        try:
            magnitude = self.magnitude()
            return [x * (1 / magnitude) for x in self.coordinates]

        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    def __str__(self):
        return 'Vector {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates
    
# Default function for handling execution loop:\
def execution_loop():
    data = int(input("Do you want to try again ? Enter [1] - for continue / [0] - for quit : \n>>>"))
    if data == 1:
        return True
    elif data == 0:
        return False
    else:
        print('Error, you entered incorrect command. Please, try again...')
        execution_loop()

# Function for creating a two vectors for verifying:
def creating_vectors():
    vectors = []
    coordinate_counter = 1
    coordinate_input_control = True
    print('Please, enter all coordinates of the vector A:')
    vectors.append(Vector(coordinate_create('A')))
    print('Please, enter all coordinates of the vector B:')
    vectors.append(Vector(coordinate_create('B', size=vectors[0].dimension)))
    return vectors

# Function for interable creating a next coordinate of the vector:
def vector_loop(index):
    data = int(input("Do you want to add a new {0}-th coordinate ? Enter :\n[2] - for adding a new coordinate;\n[1] - for adding a new vector;\n>>>"))
    if data == 2:
        return 2
    elif data == 1:
        return 1
    else:
        print('Error: you entered incorrect command. Please, try again...')
        vector_loop()

# Function for loop-creating all coordinates of the selected vector:
def coordinate_create(name, **kwargs):
    vector = []
    coordinate_counter = 1
    coordinate_input_control = True
    size = kwargs.get('size', None)
    while coordinate_input_control:
        print('Please, enter {0}-st coordinate:'.format(coordinate_counter))
        break
        if len(vector) == 3:
            print('You almost entered the maximum of coordinates of the {0} vector. The maximum number of coordinates should be less of equal to 3'.format(name))
            break
        elif len(vector) > 1:
            if name == 'A':
                data = vector_loop()
                if data == 2:
                    coordinate_input_control = True
                else:
                    coordinate_input_control = False
                    break
            else:
                if size == 2:
                    coordinate_input_control = False
                    break
                else:
                    coordinate_input_control = True
        coordinate_counter = coordinate_counter + 1
    print('You entered vector {0} with coordinates: {1}'.format(name, vector))
    return vector

# Default loop for handling execution:
again_exec = True
counter_exec = 0

# Default loop for handling execution loop:
while again_exec:
    vectors = []
    vectors = creating_vectors()
    again_exec = execution_loop()
    counter_exec = counter_exec + 1

    # The end of execution:
    if again_exec == False:
        print('Program was executed: {0} times.'.format(counter_exec))
        break

print(
  '\n-----------------------------------------\n'\
  'Copyright 2019 Vladimir Pavlov. All Rights Reserved.\n'\
  '-----------------------------------------'
  )