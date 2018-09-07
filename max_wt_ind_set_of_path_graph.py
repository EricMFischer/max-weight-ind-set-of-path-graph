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


# Vertex class for undirected graphs
class Vertex():
    def __init__(self, key):
        self._key = key
        self._nbrs = {}

    def __str__(self):
        return '{' + "'key': {}, 'nbrs': {}".format(
            self._key,
            self._nbrs
        ) + '}'

    def add_nbr(self, nbr_key, weight=1):
        if (nbr_key):
            self._nbrs[nbr_key] = weight

    def has_nbr(self, nbr_key):
        return nbr_key in self._nbrs

    def get_nbr_keys(self):
        return self._nbrs.keys()

    def get_nbr_values(self):
        return self._nbrs.values()

    def remove_nbr(self, nbr_key):
        if nbr_key in self._nbrs:
            del self._nbrs[nbr_key]

    def get_e(self, nbr_key):
        if nbr_key in self._nbrs:
            return self._nbrs[nbr_key]


# Undirected graph class
class Graph():
    def __init__(self):
        self._vertices = {}

    # 'x in graph' will use this containment logic
    def __contains__(self, key):
        return key in self._vertices

    # 'for x in graph' will use this iter() definition, where x is a vertex in an array
    def __iter__(self):
        return iter(self._vertices.values())

    def __str__(self):
        output = '\n{\n'
        vertices = self._vertices.values()
        for v in vertices:
            graph_key = "{}".format(v._key)
            v_str = "\n   'key': {}, \n   'nbrs': {}".format(
                v._key,
                v._nbrs
            )
            output += ' ' + graph_key + ': {' + v_str + '\n },\n'
        return output + '}'

    def add_v(self, v):
        if v:
            self._vertices[v._key] = v
        return self

    def get_v(self, key):
        try:
            return self._vertices[key]
        except KeyError:
            return None

    def get_v_keys(self):
        return list(self._vertices.keys())

    # removes vertex as neighbor from all its neighbors, then deletes vertex
    def remove_v(self, key):
        if key in self._vertices:
            nbr_keys = self._vertices[key].get_nbr_keys()
            for nbr_key in nbr_keys:
                self.remove_e(nbr_key, key)
            del self._vertices[key]

    def add_e(self, from_key, to_key, weight=1):
        if from_key not in self._vertices:
            self.add_v(Vertex(from_key))
        if to_key not in self._vertices:
            self.add_v(Vertex(to_key))

        self._vertices[from_key].add_nbr(to_key, weight)
        self._vertices[to_key].add_nbr(from_key, weight)

    def get_e(self, from_key, to_key):
        if from_key and to_key in self._vertices:
            return self.get_v(from_key).get_e(to_key)

    # adds the weight for an edge if it exists already, with a default of 1
    def increase_e(self, from_key, to_key, weight=1):
        if from_key not in self._vertices:
            self.add_v(Vertex(from_key))
        if to_key not in self._vertices:
            self.add_v(Vertex(to_key))

        weight_u_v = self.get_v(from_key).get_e(to_key)
        new_weight_u_v = weight_u_v + weight if weight_u_v else weight

        weight_v_u = self.get_v(to_key).get_e(from_key)
        new_weight_v_u = weight_v_u + weight if weight_v_u else weight

        self._vertices[from_key].add_nbr(to_key, new_weight_u_v)
        self._vertices[to_key].add_nbr(from_key, new_weight_v_u)

    def has_e(self, from_key, to_key):
        if from_key in self._vertices:
            return self._vertices[from_key].has_nbr(to_key)

    def remove_e(self, from_key, to_key):
        if from_key in self._vertices:
            self._vertices[from_key].remove_nbr(to_key)
        if to_key in self._vertices:
            self._vertices[to_key].remove_nbr(from_key)

    def for_each_v(self, cb):
        for v in self._vertices:
            cb(v)


# Global variables
A = list()  # keys: position in path graph, values: max weight at position
NUM_NODES = None
S = list()  # the maximum-weight independent set of the path graph


# input: a file
# output: array in which the ith entry is the max weight of a subset w/ length i of the path graph
def gen_cache_of_max_wts_of_path_subsets(filename):
    global NUM_NODES
    with open(filename) as f_handle:
        NUM_NODES = int(f_handle.readline())
        # initialize cache
        A.append(0), A.append(int(f_handle.readline()))
        for i, line in enumerate(f_handle):
            path_pos = i + 2  # 1-indexed
            node_wt = int(line)
            A.append(max(A[path_pos - 1], A[path_pos - 2] + node_wt))


# output: uses A, with the max-weights of path subsets, to return the max-weight independent set
# (MWIS) of the path graph (e.g. [1, 4, 6] -> vertices 1, 4, and 6 constitute the MWIS)
def gen_actual_max_wt_ind_set_of_path():
    global S
    # traverses array A backwards
    i = NUM_NODES
    while 1 <= i:
        if A[i - 1] == A[i]:  # case 1: current (last) node excluded
            i -= 1  # skips current vertex
        else:  # case 2: current node included
            S = [i] + S
            i -= 2
    return S


# input: test vertices, e.g. [1, 2, 3, 4, 17, 117, 517, 997]
# output: binary string with 0's or 1's indicating whether a test vertex is in the MWIS
def gen_binary_encoding_for_whether_vertices_in_MWIS(vertices):
    MWIS = {}
    for v in S:
        MWIS[v] = 1
    bin_str = ''
    for v in vertices:
        bin_str = bin_str + '1' if v in MWIS else bin_str + '0'
    return bin_str


def main():
    start = time.time()

    gen_cache_of_max_wts_of_path_subsets('max_wt_ind_set_of_path_graph.txt')
    max_wt_ind_set = gen_actual_max_wt_ind_set_of_path()
    bin_str = gen_binary_encoding_for_whether_vertices_in_MWIS([1, 2, 3, 4, 17, 117, 517, 997])
    # expected ex. file results: max sum = 2617, chosen vertices (position): [2, 4, 7, 10]
    print('MWIS: ', max_wt_ind_set)
    print('binary string: ', bin_str)
    print('elapsed time: ', time.time() - start)


main()
