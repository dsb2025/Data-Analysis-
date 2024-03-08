#  File: Adjacency.py

#  Description: Converts an edge list into an adjacency matrix
#  Student Name: Danielle Balque
#  Student UT EID: dsb2643
#  Course Name: CS 313E
#  Unique Number: 85785

import sys


def edge_to_adjacency(edge_list):
    #create set
    vert = set()
    for i in edge_list:
        vert.add(i[0])
        vert.add(i[1])
    
    
    vertices = len(vert)
    new_vert = sorted(vert)

    vert_indices = {}
    for index, vertex in enumerate(new_vert):
        vert_indices[vertex] = index
        adj_matrix = [[0 for i in range(vertices)] for i in range(vertices)]

    for i in edge_list:
        start, end, num = i[0], i[1], i[2]
        start, end = vert_indices[start], vert_indices[end]
        adj_matrix[start][end] = num

    return adj_matrix


# remove formatting and convert to list of tokens
# do not change this method
def clean(text):
    text = text.strip()
    text = text.replace("[", "")
    text = text.replace("]", "")
    text = text.replace("”", "")
    text = text.replace(" ", "")
    text = text.replace("\"", "")
    text = text.split(",")
    return text


''' DRIVER CODE '''

# Debug flag - set to False before submitting
debug = False
if debug:
    in_data = open('adjacency.in')
else:
    in_data = sys.stdin

# get line of input, remove formatting, convert to list of tokens
input_text = in_data.readline()
input_text = clean(input_text)

# convert one string to 2D list of edge data
edges = []
for i in range(0, len(input_text), 3):
    newList = [input_text[i], input_text[i+1], int(input_text[i+2])]
    edges.append(newList)

# convert the 2D list to an adjacency matrix
adj_matrix = edge_to_adjacency(edges)

print('\n'.join([' '.join([str(cell) for cell in row]) for row in adj_matrix]))
