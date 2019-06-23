# For vectors v1 and v2 check if they are orthogonal by
abs(scalar_product(v1,v2)/(length(v1)*length(v2))) < epsilon

# where epsilon is small enough. Analoguously you can use
scalar_product(v1,v2)/(length(v1)*length(v2)) > 1 - epsilon
# for parallelity test and
scalar_product(v1,v2)/(length(v1)*length(v2)) < -1 + epsilon
# for anti-parallelity.

def isOrthogonal(self,v,tolerance=1e-10):
    if abs(self.dotProduct(v)) < tolerance:
        return True

    return False

# Function for loop-creating new vectors using user's data:
def vectors_loop_creating():
    vectors = []
    vector_counter = 1
    coordinate_counter = 1
    vector_input_control = True
    while vector_input_control:
        print('Please, enter all coordinates of the %d-vector' % vector_counter)
        vector = []
        coordinate_counter = 1
        coordinate_input_control = True
        while coordinate_input_control:
            print('Please, enter %d-st coordinate:' % coordinate_counter)
            vector.append(float(input(">>>")))
            if len(vector) == 3:
                print("You almost entered the maximum number of coordinates on the {0}-vector. The maximum number of coordinates should be less of equal to 3.".format(vector_counter))
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