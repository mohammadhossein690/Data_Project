'''
This program will calculate the middle of series of
number we provided as a list 
'''
def middle_list(num_list:list) -> float:
    '''
    This program will take a list as argument
    and after that it will find the middle of
    that list
    '''
    num_list.sort()
    if len(num_list)%2 == 0:
        # We will first choose both data in the middle 
        # and after that take average of that two numbers
        last_index = int(len(num_list) - 1)
        middle1 , middle2 = last_index // 2 , last_index // 2 + 1
        return (num_list[middle1] + num_list[middle2]) / 2
    # We will choose the data in the middle of that list
    last_index = len(num_list) - 1
    return num_list[int(last_index/2)]

number_list = [1,5,6,7,9,3,15,18]
print(middle_list(number_list))
