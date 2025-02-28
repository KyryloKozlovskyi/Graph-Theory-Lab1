import numpy as np


# Exercise 1
# (a) Create a graph G1 = (V1,E1)
V1 = ["a","b","c","d","e"] # Vertices
E1 = ({"a","b"},{"c","d"},{"a","d"},{"b","c"},{"b","d"},{"d","e"}) # Edges
G1 = (V1,E1) # Graph consisting of vertices V1 and edges E1

# (b) Create a function called calculateDegree, that calculates the degree of the
# vertices in a graph. The return type should either be an array of integers or a
# dictionary

def calculateDegree(V, E):
    counts = {}
    # Initialize counts dictionary
    for v in V:
        counts[v] = 0
    # Count the number of times a vertex appears in an edge
    for v in V:
        for e in E:
            # If the vertex is in the edge, increment the count
            if v in e:
                counts[v] += 1
    return counts

# Test the function calculateDegree
print(calculateDegree(V1, E1))

# (c) Write a function called outputDegreeSequence to output a degree sequence.
def outputDegreeSequence(D):
    # Sort the dictionary by key in descending order
    sorted_degrees = sorted(D.items(), key=lambda x:x[1], reverse=True)
    # Convert the sorted list to a dictionary
    converted_degrees = dict(sorted_degrees)
    print(converted_degrees)

# Test the function outputDegreeSequence
outputDegreeSequence(calculateDegree(V1, E1))

# Exercise 2
# Create a function which outputs the Adjacency Matrix of a Graph. The output should be
# a numpy matrix (so at the start use import numpy as np).
def outputAdjacencyMatrix(V, E):
    # Create an empty matrix
    m = np.zeros((len(V), len(V)))
    # Fill the matrix with 1s where there is an edge
    for e in E:
        # Find the index of the vertices in the edge
        i = V.index(list(e)[0])
        j = V.index(list(e)[1])
        # Fill the matrix with 1s
        m[i][j] = 1
        m[j][i] = 1
    # Return the matrix
    return np.matrix(m)

# Test the function outputAdjacencyMatrix
print(outputAdjacencyMatrix(V1, E1))

# Exercise 3
# Create a function which takes a list of vertices and an adjacency matrix, and outputs a
# list of edges.
def outputListOfEdges(V, M):
    E = []
    for i in range(len(M)):
        for j in range(i, len(M)):
            # Check if the element at position [i,j] equals 1
            if M[i,j] == 1:
                E.append((V[i], V[j]))
    return E

# Test the function outputListOfEdges
print(outputListOfEdges(V1, outputAdjacencyMatrix(V1, E1)))