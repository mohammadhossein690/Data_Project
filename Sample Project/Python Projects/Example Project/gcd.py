'''
This program will calculate the greatest common divisor of
 two numbers we provided and we use ladder method for solving that
'''
def greatest_common_divisor(number1:int,number2:int) -> int:
    '''
    This function will calculate the greatest 
    common divisor base on two numbers we provided
    '''
    # First we realize maximum and minimum
    maximum = max(number1,number2)
    minimum = min(number1,number2)
    result = maximum % minimum
    divisor = 0
    if result == 0:
        divisor = minimum
    else:
        while True:
            if result != 0:
                maximum = minimum
                minimum = result
                divisor = result
                result = maximum % divisor
            else:
                break
    return divisor

print(greatest_common_divisor(150,425))
