"""
create a function to read in data from textfile
store numbers in a list
sort numbers

"""
import numpy

def read_in_file(input_file):
    size = get_max(input_file)
    print "this is the size "
    print size
    the_list = numpy.empty(size,dtype=int)
    nums = open(input_file)
    index = 0
    for num in nums:
        #the_list.append(num)
        print "this is the num "
        num
        index = int(num)
        #the_list.insert(index,num)
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

def get_max(input_file):
    read_frm_file = open(input_file)
    the_max = -9999
    for num in read_frm_file:
        if num > the_max:
            the_max = num
    return int(the_max)

read_in_file('list_of_numbers.txt')
#print_list(get_list)
