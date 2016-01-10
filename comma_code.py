# Comma Code
# Insert list and output will be string of all list items
import sys

# Define function
def comma_code(input):
    if type(input) != type(list()):
        print('Error: list data type not detected')
        sys.exit()
    string = ''
    for i in range(0,len(input)):
        string = string + input[i]
        if i < len(input) - 1:
            string += ', '
        if i == len(input)-2:
            string += 'and '
    return string
        
# Execute
spam = ['cat','dog','mouse','moose','deer','cow']
string = comma_code(spam)
print(string)
print(type(string))
