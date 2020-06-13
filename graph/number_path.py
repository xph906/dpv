import queue
# This is problem 3.23 in DPV
# Find the number of different paths from s to t in a directed acyclic graph.

# Step 1. Trim the graph so that s is the SINGLE source.
# Step 2. Toppologically visit the graph and update the path list.

def numberOfPath(s, t, graph):
    n = len(graph)

    indegree = [0 for i  in range(n)]
    # Step 1: clean up the graph so that s is the only source
    for src in range(n):
        for dst in graph[src]:
            indegree[dst] += 1

    q = queue.Queue()
    for node in range(n):
        if indegree[node] == 0 and node != s:
            q.put(node)

    while not q.empty():
        src = q.get()
        print("Drop ", src)
        for dst in graph[src]:
            indegree[dst] -= 1
            if indegree[dst] == 0 and dst != s:
                q.put(dst)

    assert q.empty()
    assert indegree[src] == 0

    # Step 2: Toppologically visit the trimmed graph from s, and update the
    # path_cnt
    path_cnt = [0 for i in range(n)]
    path_cnt[s] = 1

    q.put(s)
    while not q.empty():
        src = q.get()
        for dst in graph[src]:
            path_cnt[dst] += path_cnt[src]
            indegree[dst] -= 1
            if indegree[dst] == 0:
                if dst == t:
                    return path_cnt[dst]
                q.put(dst)

    return path_cnt[t]


def main():
    graph = [[] for i in range(8)]
    graph[5] = [0,4]
    graph[0] = [1,2,3,4]
    graph[2] = [3]
    graph[3] = [4]
    graph[6] = [4]
    graph[7] = [0,1,2,3,4]

    print(numberOfPath(0, 4, graph))

if __name__ == "__main__":
    main()
