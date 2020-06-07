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
    # Implement this
    return []

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
