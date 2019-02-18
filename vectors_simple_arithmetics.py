print(
  '-----------------------------------------\n'\
  'Python Library for Linear Algebra Operations | Vectors Initialization:\n'\
  '-----------------------------------------\n'
  )

print(
  'Task:\n'\
  '-----------------------------------------\n'\
  'Write a simple Python module for adding, substract and scalar multiply few default vectors.\n'
  )

print(
  'Solution:\n'\
  '-----------------------------------------'\
  )

#Vector module for defining a new vector on the system:
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
        return 'Vector: {}'.format(self.coordinates)
    
    def __eq__(self, v):
        return self.coordinates == v.coordinates

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

#Default parameters for handling execution loop:
again_exec = True
counter_exec = 0

#Default loop for handling execution:
while again_exec:
  A = Vector([8.218, -9.341])
  B = Vector([-1.129, 2.111])
  print('Adding vectors: {0} + {1}'.format(A[0], B[0]))
  #C = A + B
  #print(C)
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