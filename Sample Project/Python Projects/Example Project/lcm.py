'''
This program will calculat the lowest common multiple
of two numbers we provided
'''
def lowest_common_multiple(number1:int,number2:int) -> int:
    '''
    This function will calculate the lcm of two numbers
    we provided as agrgument
    '''
    if number1 > number2:
        number1 , number2 = number2 , number1
    number1_multiples = []
    number2_multiples = []
    i = 1
    while True:
        number1_multiples.append(number1*i)
        number2_multiples.append(number2*i)
        if number1_multiples[i-1] in number2_multiples:
            return number1_multiples[i-1]
        i += 1

print(lowest_common_multiple(36,48))
