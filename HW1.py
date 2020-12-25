from ast import literal_eval

# Take 5 values from user then pirnt them with their types
def hw1():

    for i in range(0,5):
        print("Enter the {}. value please:".format(i+1))
        x = input()
        input_data = get_type(x)
        print("{}. Value Entered is ".format(i+1) + x + " Type ",input_data)
        
# Defines different types of the user inputs
def get_type(input_data):
    try:
        return type(literal_eval(input_data))
    except (ValueError, SyntaxError):
        return str
        

# Main function
if __name__ == '__main__':
    hw1()