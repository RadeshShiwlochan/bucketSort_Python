"""
create a function to read in data from textfile
store numbers in a list
sort numbers

"""
the_list = []

def read_in_file(input_file):
    nums = open(input_file)
    index = 0
    for num in nums:
        the_list.append(num)

def print_list(input_list):
    for num in input_list:
        print num + "  "

read_in_file('list_of_numbers.txt')
print_list(the_list)