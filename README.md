## Synopsis
In this programming problem you'll code up the dynamic programming algorithm for computing a
maximum-weight independent set of a path graph. The accompanying text file describes the weights of the vertices in a path graph (with the
weights listed in the order in which vertices appear in the path). It has the following format:

[number_of_vertices]

[weight of first vertex]

[weight of second vertex]

...


For example, the third line of the file is "6395702," indicating that the weight of the second
vertex of the graph is 6395702.

Your task in this problem is to run the dynamic programming algorithm (and the reconstruction
procedure) from lecture on this data set. The question is: of the vertices 1, 2, 3, 4, 17, 117,
517, and 997, which ones belong to the maximum-weight independent set? (By "vertex 1" we mean the
first vertex of the graph---there is no vertex 0.) In the box below, enter a 8-bit string, where
the ith bit should be 1 if the ith of these 8 vertices is in the maximum-weight independent set,
and 0 otherwise. For example, if you think that the vertices 1, 4, 17, and 517 are in the
maximum-weight independent set and the other four vertices are not, then you should enter the
string 10011010 in the box below.

## Motivation
The last algorithm on Huffman codes provided an example of how dynamic programming, a binary tree, a heap, and a unique reconstruction procedure after every returned recursive call worked together to solve a complex problem. This algorithm will provide another example of how dynammic programming can be so useful. 

## Acknowledgements

This algorithm is part of the Stanford University Algorithms 4-Course Specialization on Coursera, instructed by Tim Roughgarden.
