print(
  '-----------------------------------------\n'\
  'Python Library for Linear Algebra Operations | Vectors Initialization:\n'\
  '-----------------------------------------\n'
  )

print(
  'Task:\n'\
  '-----------------------------------------\n'\
  'Write a simple Python module for creating different vectors on the different dimensions.\n'
  )

print(
  'Solution:\n'\
  '-----------------------------------------'\
  )

#Default function for handling execution loop:
def execution_loop():
  #data = input("Do you want to try again ? Enter [1] - for continue / [0] - for quit : ")
  data = int(input("Do you want to try again ? Enter [1] - for continue / [0] - for quit : "))
  if data == 1:
    return True
  elif data == 0:
    return False
  else:
    print("Error: your entered incorrect command. Please, try again...")
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
            raise TypeError('The coordinates must be an iterable')

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
        print("Please, enter all coordinates of the %d vector:" % vector_counter)
        vector = []
        coordinate_counter = 1
        coordinate_input_control = True
        while 
        print("Please, enter %d-st coordinate:" % coordinate_counter)
        vector.append(int(input("")))

        

#Function for handling all operations on the vectors:
def vectors_operations_handling():


#Default parameters for handling execution loop:
again_exec = True
counter_exec = 0

#Default loop for handling execution:
while again_exec:
  vectors = []
  vectors = vectors_loop_creating()
  vectors_operations_handling()
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