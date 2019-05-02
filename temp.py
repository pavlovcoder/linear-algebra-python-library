class UnAcceptedValueError(Exception):   
    def __init__(self, data):    
        self.data = data
    def __str__(self):
        return repr(self.data)

def custom_function():
    Total_Marks = int(input("Enter Total Marks Scored: "))
    try:
        Num_of_Sections = int(input("Enter Num of Sections: "))
        if(Num_of_Sections < 1):
            raise UnAcceptedValueError("Number of Sections can't be less than 1")

    except (ValueError) as e:
        print('You entered value of the data. Please, try again...', e.errno)

    except (TypeError):
        print('You entered incorrect type of data. Please, try again...')

    except SyntaxError:
        print('You should enter [1] or [2] number for handling program. This command shouldn\'t be empty!')
        custom_function()

    except KeyboardInterrupt:
        print('You cannot using "Ctrl+C" or "DELETE" for quit the program. Please, try again...')
        custom_function()

    except UnAcceptedValueError as e:
        print ("Received error:", e.data)

    except:
        print('Unexpected error.')
        custom_function()

custom_function()

is_nice = True
state = "nice" if is_nice else "not nice"

X_train = X[0:split]
X_test  = X[split:]
y_train = y[0:split]
y_test  = y[split:]

grade = [random.random() for ii in range(0,n_points)]
bumpy = [random.random() for ii in range(0,n_points)]

X = [[gg, ss] for gg, ss in zip(grade, bumpy)]
split = int(0.75*n_points)
