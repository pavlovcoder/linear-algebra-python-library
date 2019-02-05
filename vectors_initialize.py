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
      print(f'Please, enter all coordinates of the {vector_counter}-vector:')
      vector = []
      coordinate_counter = 1
      coordinate_input_control = True
      while coordinate_input_control:
        #print("Please, enter %d-st coordinate:" % coordinate_counter)
        print(f'Please, enter {coordinate_counter}-st coordinate:')
        vector.append(int(input(">>>")))
        if len(vector) == 3:
          #print("You almost entered the maximum number of coordinates on the %d-vector." % vector_counter)
          print(f'You almost entered the maximum number of coordinates on the {vector_counter}-vector. The maximum number of coordinates should be less of equal to 3.')
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
  print('Output 1-th vector:')
  print(vectors[0])

#Default parameters for handling execution loop:
again_exec = True
counter_exec = 0

#Default loop for handling execution:
while again_exec:
  vectors = []
  vectors = vectors_loop_creating()
  vectors_operations_handling(vectors)
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