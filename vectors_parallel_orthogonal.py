print(
  '-----------------------------------------\n'\
  'Python Library for Linear Algebra Operations | Checking out parallelism and orthogonality of two vectors:\n'\
  '-----------------------------------------\n'
  )

print(
  'Task:\n'\
  '-----------------------------------------\n'\
  'Write a simple Python module for checking out parallelism or orthogonality of two entered vectors:\n'
  )

print(
  'Solution:\n'\
  '-----------------------------------------'\
  )

import os, sys, math

#Default function for handling execution loop:
def execution_loop():
    data = int(input("Do you want to try again ? Enter [1] - for continue / [0] - for quit : \n>>>"))
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

def vector_loop():
    data = int(input("Do you want to add a new coordinate ? Enter:\n[2] - for adding a new coordinate;\n[1] - for adding a new vector;\n>>>"))
    if data == 2:
        return 2
    elif data == 1:
        return 1
    else:
        print("Error: you entered incorrect command. Please, try again...")
        vector_loop()

def vector_loop_max():
    data = int(input("Do you want to add a new vector ? Enter: \n[1] - for adding a new vector;\n[0] - for exit\n>>>"))
    if data == 1:
        return 1
    elif data == 0:
        return 0
    else:
        print("Error: you entered incorrect command. Please, try again...")
        vector_loop_max()

# Function for creating a two vectors for verifying:
def creating_vectors():
    vectors = []
    coordinate_counter = 1
    coordinate_input_control = True
    print('Please, enter all coordinates of the vector A:')
    vectors.append(Vector(coordinate_create('A')))
    # I finished here (23.06.2019)
    # I should use length of the previous vector A for limit a user for entering coordinate of the next vector B with the same length...
    # print('Size of the previus vector: {0}'.format(len(Vector[0])))
    print('Please, enter all coordinates of the vector B:')
    vectors.append(Vector(coordinate_create('B')))
    print('You entered vectors:')
    print(vectors)
    return vectors

# Function for loop-creating all coordinates of the selected vector:
def coordinate_create(name):
    vector = []
    coordinate_counter = 1
    coordinate_input_control = True
    while coordinate_input_control:
        print("Please, enter {0}-st coordinate:".format(coordinate_counter))
        vector.append(float(input(">>>")))
        if len(vector) == 3:
            print("You almost entered the maximum number of coordinates of the {0} vector. The maximum number of coordinates should be less of equal to 3.".format(name))
            break
        data = vector_loop()
        if data == 2:
            coordinate_input_control = True
        else:
            coordinate_input_control = False
            break
        coordinate_counter = coordinate_counter + 1
    print("You entered vector {0} with coordinates: ".format(name))
    return vector

#Default parameters for handling execution loop:
again_exec = True
counter_exec = 0

#Default loop for handling execution:
while again_exec:
    vectors = []
    vectors = creating_vectors()
    again_exec = execution_loop()
    counter_exec = counter_exec + 1

    #The end of execution:
    if again_exec == False:
        print('Program was executed: {0} times.'.format(counter_exec))
        break

print(
  '\n-----------------------------------------\n'\
  'Copyright 2019 Vladimir Pavlov. All Rights Reserved.\n'\
  '-----------------------------------------'
  )