from scc import findSCC


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
