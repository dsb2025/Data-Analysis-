#  File: Spiral.py
#  Student Name: Danielle Balque
#  Student UT EID: dsb2643
import sys


# Input: n
# Output:
def get_dimension(in_data):
    #read in first line as dimension define as n
    n = int(in_data.readline().strip())
   
    return n


# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
def create_spiral(n):
    #check if n is od
    if n % 2 == 0:
        n += 1
    #create spiral with 2d list    
    spiral = [[0 for i in range(n)] for j in range(n)]
    #start point
    num = 1
    #find center
    row = n // 2
    col = n // 2
    #define possible directions 
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    #start dir index
    direction_index = 0
    #start count that will traverse through each circle in the spiral
    curr_circle_length = 1
    #will start is less o2r equal to dim
    while num <= n*n:
        #define start in spiral
        spiral[row][col] = num
        #go though all directions in list
        move1 = directions[direction_index % 4]
        for i in range(curr_circle_length):
            if num >= n*n:
                return spiral
            #start num goes through dir right down
            row += move1[0]
            col += move1[1]
            num += 1
            spiral[row][col] = num
        #imcrement dir
        direction_index += 1
        #repeat moves for 2nd move
        move2 = directions[direction_index % 4]
        for i in range(curr_circle_length):
            if num >= n *n:
                return spiral
            row += move2[0]
            col += move2[1]
            num += 1
            spiral[row][col] = num
        direction_index += 1
        #complete circle to next one in spiral
        curr_circle_length += 1
        
    return spiral
            

# Input: handle to input file
#        the number spiral
# Output: printed adjacent sums
def print_adjacent_sums(in_data, spiral):
    for line in in_data:
        try:
            #read dim
            num = int(line.strip())
            #read integer for which the adjacent sum should be calculated
            adjacent_sum = sum_adjacent_numbers(spiral, num)
            print(adjacent_sum)
        except ValueError:
            #print invalid if input error
            print("Invalid data")
  


# Input: the number spiral
#        the number to find the adjacent sum for
# Output: integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    #define sp5iral size
    size = len(spiral)
    #define row and col
    row, col = None, None
    for r in range(size):
        for c in range(size):
            #size of r and c is the dim
            if spiral[r][c] == n:
                row = r
                col = c
                break
            
    if (row is None) or (col is None):
        return 0

    adjacent_sum = 0
    for dx in range(-1, 2): #range end to center [-1, 0, 1]
        for dy in range(-1, 2):
            #traverse through diagnals
            curr_row = row + dx
            curr_col = col + dy
            #test for different cases and add r and c
            if curr_row >= 0 and curr_row < size and curr_col >= 0 and curr_col < size and not (dx == 0 and dy ==0):
                adjacent_sum += spiral[curr_row][curr_col]
    return adjacent_sum


            

# Added for debugging only. No changes needed.
# Do not call this method in submitted version of your code.
def print_spiral(spiral):
    for i in range(0, len(spiral)):
        for j in range(0, len(spiral[0])):
            row_format = '{:>4}'
            print(row_format.format(spiral[i][j]), end='')
        print()


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # set the input source - change to False before submitting
    debug = False
    if debug:
        in_data = open('spiral.in')
    else:
        in_data = sys.stdin

    # process the lines of input
    size = get_dimension(in_data)

    # create the spiral
    spiral = [[]]
    spiral = create_spiral(size)
    # use following line for debugging only
    # print_spiral(spiral)

    # process adjacent sums
    print_adjacent_sums(in_data, spiral)


if __name__ == "__main__":
    main()
