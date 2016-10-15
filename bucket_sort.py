"""
create a function to read in data from textfile
store numbers in a list
sort numbers

"""
import numpy

def bucket_sort(input_file):
    size = get_max(input_file)
    #the_list = numpy.empty(size,dtype=int)
    the_list = [None] * size
    nums = open(input_file)
    index = 0
    for num in nums:
        #the_list.append(num)
        index = int(num)
        the_list.insert(index,num)
    return the_list

def print_list(input_list):
    for num in input_list:
        if num == None:
            continue
        else:
            print num

def get_min(input_file):
    the_min = 1000000
    read_frm_file = open(input_file)
    for num in read_frm_file:
        if num < the_min:
            the_min = num
    return int(the_min)

def get_max(input_file):
    read_frm_file = open(input_file)
    the_max = -9999
    for num in read_frm_file:
        if num > the_max:
            the_max = num
    return int(the_max)

get_list = bucket_sort('list_of_numbers.txt')
print_list(get_list)
