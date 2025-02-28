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
print(outputDegreeSequence(calculateDegree(V1, E1)))