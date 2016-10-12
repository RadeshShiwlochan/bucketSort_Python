"""
create a function to read in data from textfile
store numbers in a list
sort numbers

"""
def read_in_file(input_file):
    nums = open(input_file)
    for num in nums:
        print num

read_in_file('list_of_numbers.txt')