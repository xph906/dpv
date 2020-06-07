from scc import findSCC

"""
The 2-Sat solver.

Assuming no unique clause
Arguments:
    clauses: array of variable pairs e.g.,
        (x1 V x2) ^ (x2 V ~x1) ^ (~x1 V ~x2) =>
        [(1,2), (2,-1), (-1,-2)]
    n: the number of variables. The variables are x1 ... xn
"""
def solve2Sat(clauses, n):
    # Step 1: build graph
    # xi => graph[i-1]
    # ^xi => graph[i-1 + n]
    graph = [[] for i in range(2*n)]
    for clause in clauses:
        # e.g., (1,-2) means (x1 V ~x2)
        v1 = clauseValueToNodeIndex(clause[0], n)
        neg_v1 = clauseValueToNodeIndex(-clause[0], n)
        v2 = clauseValueToNodeIndex(clause[1], n)
        neg_v2 = clauseValueToNodeIndex(-clause[1], n)

        # add edge: neg_v1 => v2
        graph[neg_v1].append(v2)
        # add edge: neg_v2 => v1
        graph[neg_v2].append(v1)


    # Step 2: scc
    # smallest scc index is the sink, largest is the source
    scc = findSCC(graph)

    # Step 3: group nodes based on scc index.
    # E.g., scc_list[2] is all the nodes belong to the second SCC
    max_scc = max(scc)
    scc_list = [[] for i in range(max_scc+1)]
    for i in range(len(scc)):
        scc_list[scc[i]].append(i)

    # Step 4: attempt to assign values to the variables
    first = 1      # always points to the sink
    last = max_scc # always points to the source
    if first == last:
        return None

    assignment = [None for i in range(n)]
    while first < last:
        # Assign varaibles in the sink component to make sure they are resolved
        # to True
        for v in scc_list[first]:
            idx = v % n
            # If the value has been set already, it means infeasible.
            if assignment[idx] != None:
                return None

            if v >= n:
                assignment[idx] = False
            else:
                assignment[idx] = True
        # Get rid off the sink
        first += 1
        # Get rid off the source
        last -= 1

    return assignment




"""
    Example:
        If v is 2 and n = 3: there are three variables x1, x2, x3
        this value is x2 and its index is 1 (v - 1 + n)
        If v is -2 and n = 3: there are three variables x1, x2, x3
        this value is ~x2 and its index is 4 (-v - 1 + n)
"""
def clauseValueToNodeIndex(v, n):
    if v < 0:
        node = -1 * v -1 + n
    else:
        node = v - 1
    return node


############################################


def main():
    # Expect x1 = true and x2 = false
    print(solve2Sat([(1,2), (2,-1), (-1,-2)], 2))
    # Expect unsatisfiable
    print(solve2Sat([(1,2), (2,-1), (1,-2), (-1,-2)], 2))

if __name__ == "__main__":
    main()
