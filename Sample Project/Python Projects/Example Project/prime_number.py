'''
This program will realize that the number is prime or 
not and then give us the last prime number in a range
we provided and tell us how many prime numbers we have
'''
import time
def is_prime(number:int) -> bool:
    '''
    This funcion will check that whether 
    the number we provided is prime or not
    '''
    # First we suppose that the number is prime
    prime = True
    # We will go up to the square root of number + 1
    for i in range(2,int((number**0.5)+1)):
        if number%i == 0:
            prime = False
            break
    return prime

# first we assign counter to 0 and every time the number is
# prime it will add 1 to counter 
start = time.time()
COUNTER = 0
for num in range(1,1000001):
    if is_prime(num):
        COUNTER += 1
        # The last prime number every time updates until the last one
        last_prime_number = num
end = time.time()
print(f'We have {COUNTER} prime numbers below 1000000')
print(f'The last prime number below 1000000 is {last_prime_number}')
print('----------------------------------------------')
print(f'The duration of running this program is {end-start:.3f}s')
