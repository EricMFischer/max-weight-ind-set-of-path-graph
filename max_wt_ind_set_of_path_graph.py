'''
In this programming problem you'll code up the dynamic programming algorithm for computing a
maximum-weight independent set of a path graph.

The accompanying text file describes the weights of the vertices in a path graph (with the
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
first vertex of the graph---there is no vertex 0.) In the box below, enter an 8-bit string, where
the ith bit should be 1 if the ith of these 8 vertices is in the maximum-weight independent set,
and 0 otherwise. For example, if you think that the vertices 1, 4, 17, and 517 are in the
maximum-weight independent set and the other four vertices are not, then you should enter the
string 10011010 in the box below.
'''
import time

# Global variables
A = list()  # keys: position in path graph, values: max weight at position
NUM_NODES = None
S = list()  # the maximum-weight independent set of the path graph


# input: file
# output: array in which ith entry is the max weight of a subset with length i of the path graph
def gen_max_wt_cache_of_path_subsets(f):
    global NUM_NODES
    with open(f) as f_handle:
        NUM_NODES = int(f_handle.readline())
        # initialize cache
        A.append(0), A.append(int(f_handle.readline()))
        for i, line in enumerate(f_handle):
            path_pos = i + 2  # 1-indexed
            node_wt = int(line)
            A.append(max(A[path_pos - 1], A[path_pos - 2] + node_wt))


# output: uses A with max-weights of path subsets to return the max-weight independent set
# (MWIS) of the path graph (e.g. [1, 4, 6] -> vertices 1, 4, and 6 constitute the MWIS)
def gen_max_wt_ind_set():
    global S
    i = NUM_NODES
    # traverses array A backwards
    while 1 <= i:
        if A[i - 1] == A[i]:  # case 1: current (last) node excluded
            i -= 1  # skips current vertex
        else:  # case 2: current node included
            S = [i] + S
            i -= 2
    return S


# input: test vertices, e.g. [1, 2, 3, 4, 17, 117, 517, 997]
# output: binary string with a 0 or 1 indicating whether a test vertex is in the MWIS
def gen_bin_str_for_whether_vertices_in_MWIS(vertices):
    MWIS = {}
    for v in S:
        MWIS[v] = 1
    bin_s = ''
    for v in vertices:
        bin_s = bin_s + '1' if v in MWIS else bin_s + '0'
    return bin_s


def main():
    start = time.time()

    gen_max_wt_cache_of_path_subsets('max_wt_ind_set_of_path_graph.txt')
    max_wt_ind_set = gen_max_wt_ind_set()
    bin_str = gen_bin_str_for_whether_vertices_in_MWIS([1, 2, 3, 4, 17, 117, 517, 997])

    # expected ex file results: max sum = 2617, vertices (position): [2, 4, 7, 10]
    print('MWIS: ', max_wt_ind_set)
    print('binary string: ', bin_str)
    print('elapsed time: ', time.time() - start)


main()
