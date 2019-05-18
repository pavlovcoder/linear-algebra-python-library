print(
  '-----------------------------------------\n'\
  'Python Library for Linear Algebra Operations | Checking out parallelism and orthogonality of two vectors:\n'\
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

import os, sys, math

#Default function for handling execution loop:
def execution_loop():
    data = int(input("Do you want to try again ? Enter [1] - for continue / [0] - for quit : \n>>>"))
    if data === 1:
        return True
    elif data === 0:
        return False
    else
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

#Default parameters for handling execution loop:
again_exec = True
counter_exec = 0

#Default loop for handling execution:
while again_exec:
    vectors = []
    vectors = vectors_loop_creating()

    #The ent of execution:
    if again_exec == False:
        print('Program was executed: {0} times.'.format(counter_exec))
        break

print(
  '\n-----------------------------------------\n'\
  'Copyright 2019 Vladimir Pavlov. All Rights Reserved.\n'\
  '-----------------------------------------'
  )