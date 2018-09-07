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
The last algorithm on Huffman coding provided an example of how dynamic programming, a binary tree, a heap, and a unique reconstruction procedure after every returned recursive call worked together to solve a complex problem. This algorithm will provide another example of how dynammic programming can be useful for problems where we can: 1) identify a small number of subproblems, 2) quickly compute and correctly solve larger subproblems given the solutions to smaller ones, and 3) quickly compute the final solution after solving all subproblems. In general, reasoning about the structure of the optimal solution is how we identify what the smaller subproblems should be in dynamic programming.

In this algorithm, we did not need a binary tree or heap, but we did use a unique reconstruction procedure again to solve a problem that would have been more complex otherwise. After generating the array A which holds the maximum weights for subsets of the path graph, we traversed A backwards to generate the *actual* maximum-weight independent set (MWIS) of the path graph, each time deciding whether or not to include a vertex in the MWIS depending on whether or not the previous entry in A is equal to (case 1) or less (case 2) than the current entry in A. If the previous entry is equal (case 1), that means the subset of the path graph with the current vertex removed has the same maximum weight and thus we should exclude the current vertex because the computation of A, which correctly computes the maximum weights at each forward step in the path, excluded it from the actual MWIS. If it is less than the current entry in A, that means the subset of the path graph which includes the current vertex has a greater maximum weight than any subset which excludes it and thus the current vertex should be included in the MWIS.

This can be proved by induction. The recursive calls are assumed to be continually correct by the inductive hypothesis, and the inductive step is justified by a case analysis focusing on the last 3 vertices in a proposed MWIS of a path graph.

## Acknowledgements

This algorithm is part of the Stanford University Algorithms 4-Course Specialization on Coursera, instructed by Tim Roughgarden.
