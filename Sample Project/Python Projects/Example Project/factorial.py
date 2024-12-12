'''
This program will calculate thefactorial of 
numbers we provided 
'''
def factorial_number(number:int) -> int:
    '''
    This function will recieve number and then
    calcualte for its factorial
    '''
    fact = 1
    for i in range(1,number+1):
        # multiply i by fact and save it inplace
        fact *= i
    return fact
NUM = 4
print(f'{NUM}! = {factorial_number(NUM)}')
