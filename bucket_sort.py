"""
create a function to read in data from textfile
store numbers in a list
sort numbers

"""


def read_in_file(input_file):
    the_list = []
    nums = open(input_file)
    index = 0
    for num in nums:
        the_list.append(num)
    return the_list

def print_list(input_list):
    for num in input_list:
        print num + "  "

def get_min(a_list):
    index = 0
    the_min = a_list[index]
    for num in a_list:
        if num < the_min:
            the_min = num
    return the_min

def get_max(a_list):
    the_max = 0
    for num in a_list:
        if num > the_max:
            the_max = num
    return the_max

get_list = read_in_file('list_of_numbers.txt')
print_list(get_list)
min = get_min(get_list)
print min