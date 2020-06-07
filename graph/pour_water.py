import queue

"""
Pour water among k containers, and check if it's possible to come into a state.
Each pour cannot stop unless the dst contianer is full or the src container is
empty.

Arguments:
    capacities: an array of container capacity.
    init_state: an array of inital state.
    predicate: check if a given node is what we want.

Returns:
    the step list to achieve the final state with minumal action counts, or None
    if it doesn't exist.

"""
def pour_water(capacities, init_state, predicate):
    # Build adjacency list graph using dictionary
    # The graph starts with one node and we build the rest of the graph as we
    # traverse the graph.
    graph = {}
    graph[init_state] = []
    k = len(capacities)

    # Start BFS search
    q = queue.Queue()
    q.put(init_state)
    # This dictionary is used to reconstruct the path.
    prev_node = {}
    prev_node[init_state]  = None
    visited = set()

    while not q.empty():
        node = q.get()
        if node in visited:
            continue
        visited.add(node)
        print('Start visit ',node)

        # Found the results.
        if predicate(node):
            return recoverPath(node, prev_node)

        # Generate the rest of the nodes
        # We need to explore k^2 possibilities.
        for src in range(k):
            # The selected src doesn't have anything to pour to other containers
            if node[src] == 0:
                continue
            for dst in range(k):
                if src == dst:
                    continue
                # The seelcted dst is full.
                if node[dst] == capacities[dst]:
                    continue
                # We can pour `value` amount each time
                value = min(node[src], capacities[dst]-node[dst])
                new_node = createNewNode(node, src, dst, value)
                # Add the node to the graph
                if not new_node in graph:
                    graph[new_node] = []
                    prev_node[new_node] = node
                # Add an edge from node to new_node
                graph[node].append(new_node)
                # Put new_node to the queue for future traverse.
                q.put(new_node)

    return False

def recoverPath(dst_node, prev_node):
    rs = [dst_node]
    node = prev_node[dst_node]
    while node is not None:
        rs.insert(0, node)
        node = prev_node[node]

    return rs

def createNewNode(original, src, dst, value):
    # Tuple is immutable so we need to convert it to list first
    new_node = list(original)
    new_node[src] -= value
    new_node[dst] += value
    return tuple(new_node)

##########################################################################
def predicate(node):
    if node[1] == 2 or node[2] == 2:
        return True
    return False

def main():
    rs = pour_water([10,7,4], (0,7,4), predicate)
    print(rs)

if __name__ == "__main__":
    main()
