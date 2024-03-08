#  File: DNA.py
#  Student Name: Danielle Balque
#  Student UT EID: dsb2643
import sys


# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest
#         common subsequence. The list is empty if there are no
#         common subsequences.
def longest_subsequence(s1, s2):
    #find all substrings of each string and make into list
    lst1 = list(s1[i:j+1] for i in range (len(s1)) for j in range(i,len(s1)))
    lst2 = list(s2[i:j+1] for i in range (len(s2)) for j in range(i,len(s2)))
    #change all character to upper in both lists
    l1 = [x.upper() for x in lst1]
    l2 = [x.upper() for x in lst2]
    #through sets determine which substrings are found in both strings
    common_elements = set(l1).intersection(l2)
    #check if common elements are empty
    if common_elements == set():
        return None
    else:
        #count the character with max length in common elements
        m = max(map(len,common_elements)); [x for x in common_elements if len(x) == m] 
        #create list of longest common subsequences
        lst = []
        #for each element in common elements determine if its length is equal to the greatest length
        for s in common_elements:
            if len(s) == m:
                #append to list of longest common subsequences
                lst.append(s)
        
        return lst       


# Input: list of strings, one string per file input line
# Output: process each pair of DNA strings in the list
def process_lines(lines):
    #define first line as num of pairs
    num_of_pairs = lines[0]
    #start pair count
    pair1 = 1
    pair2 = 2
    #in the range of num pairs read 2 sequences
    for i in range(int(num_of_pairs)):
        s1 = lines[pair1].strip("\n")
        s2 = lines[pair2].strip("\n")
        #take in seq as list
        seq = longest_subsequence(s1, s2)
        #check if seq is empty
        if seq == None:
            print("No Common Sequence Found")
            continue
        #sort seq
        if len(seq) > 1:
            seq = sorted(seq)
        #print each string in seq
        for s in seq:
            print(s)
        #count pair lines in input
        pair1 += 2
        pair2 += 2
        print()

''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        # in_data = open('autograde/test_cases/test_3.in')
        in_data = open('dna.in')
    else:
        in_data = sys.stdin

    # input will be list of strings, one string per line
    lines = in_data.readlines()

    # process the lines
    process_lines(lines)
    in_data.close()


if __name__ == "__main__":
    main()
