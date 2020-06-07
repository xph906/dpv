"""
Find the strong connected graph.

Arguments:
    graph: adjacency list. E.g., the neighbors of node 2 is 3 and 4, so that
        graph[2] == [3,4]
Returns:
    Strong connected component index array scc. E.g., the scc index of node 2
    can be found at scc[2]. The index is in topological order
"""

def findSCC(graph):
    n = len(graph)
    nodes = [i for i in range(n)]

    # Step 1
    reverse_graph = reverseGraph(graph)

    # Step 2
    # The postorders start from 1 to n.
    postorders, _ = dfsGraph(reverse_graph, nodes)

    # Step 3
    # Topological sort the nodes based on nodes' postorders.
    ordered_nodes = [0 for i in range(n)]
    for i in range(n):
        # idx is the postorder of node i.
        idx = postorders[i]
        # Sort the nodes based on idx, descending.
        ordered_nodes[n-idx] = i

    # Step 4
    _, scc = dfsGraph(graph, ordered_nodes)

    return scc


"""
Apply DFS on the graph, and output the postorder as well as strong connected
component index of each node.


Arguments:
    graph: adjacency list.

Returns:
    postorders: The array of postorder for each node. The postorder ranges from
        1 to n.
    scc: the scc array
"""
def dfsGraph(graph, nodes):
    n = len(graph)
    postorders = [0 for i in range(n)]
    scc = [0 for i in range(n)]
    visited = [False for i in range(n)]

    scc_idx = 1
    postorder_idx = 1
    for node in nodes:
        if visited[node]:
            continue
        explore(node, graph, visited, postorder_idx, postorders, scc_idx, scc)
        scc_idx += 1


    return postorders, scc

"""
Apply DFS on the graph from a single source.


Arguments:
    graph: adjacency list.
    visited: the visited array
    postorder_idx: postorder index
    postorders: the postorder array
    scc_idx: scc index.
    scc: the strong connected component array.

Returns:
    the current postorder_idx
"""
def explore(source, graph, visited, postorder_idx, postorders, scc_idx, scc):
    visited[source] = True
    scc[source] = scc_idx

    for dst in graph[source]:
        if visited[dst]:
            continue
        postorder_idx = explore(dst, graph, visited, postorder_idx, postorders, scc_idx, scc)

    postorders[source] = postorder_idx
    postorder_idx += 1
    return postorder_idx


def reverseGraph(graph):
    n = len(graph)
    r_graph = [[] for i in range(n)]

    for src in range(n):
        for dst in graph[src]:
            r_graph[dst].append(src)

    return r_graph

############################################
def buildDpvFigure310():
    graph = [[] for i in range(12)]
    graph[1] = [0,4]
    graph[2] = [1,5]
    graph[3] = [1]
    graph[4] = [1]
    graph[5] = [2,4]
    graph[6] = [4,8]
    graph[7] = [5,6]
    graph[8] = [9]
    graph[9] = [6,11]
    graph[10] = [7]
    graph[11] = [10]
    return graph

def main():
    graph = buildDpvFigure310()
    scc = findSCC(graph)
    for i in range(len(graph)):
        print(i, scc[i])

main()
