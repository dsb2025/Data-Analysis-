#  File: Work.py
#  Student Name: Danielle Balque
#  Student UT EID: dsb2643

import sys
import time


# Purpose: Determines how many lines of code will be written
#          before the coder crashes to sleep
# Input: lines_before_coffee - how many lines of code to write before coffee
#        prod_loss - factor for loss of productivity after coffee
# Output: returns the number of lines of code that will be written
#         before the coder falls asleep
def sum_series(lines_before_coffee, prod_loss):
    lines = lines_before_coffee
    #find lines after prod loss
    new_lines = lines // prod_loss
    #num of lines must be bigger than the productivity level
    while new_lines > 0:
        #add prod loss lines
        lines += new_lines
        new_lines = new_lines // prod_loss
    return lines
    

# Purpose: Uses a linear search to find the initial lines of code to
#          write before the first cup of coffee, so that the coder
#          will complete the total lines of code before sleeping AND
#          get to have coffee as soon as possible.
# Input: total_lines - lines of code that need to be written
#        prod_loss - factor for loss of productivity after each coffee
# Output: returns the initial lines of code to write before coffee
def linear_search(total_lines, prod_loss):
    total_lines = int(total_lines)
    prod_loss = int(prod_loss)
    count = 0
    #start count of sum series
    for lines_before_coffee in range(1, total_lines + 1):
        count += 1
        #n = num of lines of code to write
        if sum_series(lines_before_coffee, prod_loss) >= total_lines:
            return lines_before_coffee, count
    return total_lines, count
    # use linear search here
  


# Purpose: Uses a binary search to find the initial lines of code to
#          write before the first cup of coffee, so that the coder
#          will complete the total lines of code before sleeping AND
#          get to have coffee as soon as possible.
# Input: total_lines - lines of code that need to be written
#        prod_loss - factor for loss of productivity after each coffee
# Output: returns the initial lines of code to write before coffee
def binary_search(total_lines, prod_loss):
    total_lines = int(total_lines)
    prod_loss = int(prod_loss)
    lo = 0
    hi = total_lines
    #get half of lines of code and compare to n(num of code lines)
    count = 0
    # find lo being initial lines of code before coffee
    while hi >= lo:
        count += 1
        mid = (hi + lo)//2
        midnum = sum_series(mid,prod_loss)
        if midnum == total_lines:
            return mid, count
        #add to lo if mid num is less than the total lines
        if midnum < total_lines:
            lo = mid + 1
        #sub from hi if mid num is greater than the total lines
        if midnum > total_lines:
            hi = mid - 1


    return lo, count
    

''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # Open input source
    # Change debug to false before submitting
    debug = False
    if debug:
        in_data = open('work.in')
    else:
        in_data = sys.stdin

    # read number of cases
    line = in_data.readline().strip()
    num_cases = int(line)

    for i in range(num_cases):

        # read one line for one case
        line = in_data.readline().strip()
        data = line.split()
        total_lines = int(data[0])  # total number of lines of code
        prod_loss = int(data[1])  # read productivity loss factor
        
        print("=====> Case #", i + 1)

        # Binary Search
        start = time.time()
        print("Binary Search:")
        lines, count = binary_search(total_lines, prod_loss)
        print("Ideal lines of code before coffee:", lines)
        print("sum_series called", count, "times")
        finish = time.time()
        binary_time = finish - start
        print("Elapsed Time:", "{0:.8f}".format(binary_time),
              "seconds")
        print()

        # Linear Search
        start = time.time()
        print("Linear Search:")
        lines, count = linear_search(total_lines, prod_loss)
        print("Ideal lines of code before coffee:", lines)
        print("sum_series called", count, "times")
        finish = time.time()
        linear_time = finish - start
        print("Elapsed Time:", "{0:.8f}".format(linear_time),
              "seconds")
        print()

        # Comparison
        print("Binary Search was",
              "{0:.1f}".format(linear_time / binary_time),
              "times faster.")
        print()
        print()


if __name__ == "__main__":
    main()
