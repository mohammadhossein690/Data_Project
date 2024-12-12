'''
This program is just a simple calculator that just
do simple arthmetic addition subtraction divivsion
and also multiplication 
'''
# -------------------------- function definition -------------------------- 
def addition(number1:float,number2:float) -> float:
    '''
    This function will add two numbers together
    '''
    return number1 + number2

def subtraction(number1:float,number2:float) -> float:
    '''
    This function will subtract two numbers together
    '''
    return number1 - number2

def multiplication(number1:float,number2:float) -> float:
    '''
    This function will multiply two numbers together
    '''
    return number1 * number2

def divivsion(number1:float,number2:float) -> float:
    '''
    This function will divide two numbers together
    '''
    return number1 / number2

# -------------------Now let's write our main program (body of program)-------------------
number_1 = float(input('Enter first number :'))
number_2 = float(input('Enter second number :'))
print('---------------------------------')
print('Please select your operation : ')
print('1) +')
print('2) -')
print('3) *')
print('4) /')

while True:
    operator = input('Enter your operator : ')
    if operator in ['1','2','3','4']:
        break

if operator == '1':
    print(f'The sum of {number_1} and {number_2} is {addition(number_1,number_2)}')

elif operator == '2':
    print(f'The subtraction of {number_1} and {number_2} is {subtraction(number_1,number_2)}')

elif operator == '3':
    print(f'The multiplication of {number_1} and {number_2} is {multiplication(number_1,number_2)}')

elif operator == '4':
    print(f'The division of {number_1} and {number_2} is {divivsion(number_1,number_2)}')
