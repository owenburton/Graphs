from collections import deque

def earliest_ancestor(ancestors, starting_node):
    # reverse the tuples direction of edges for ancestors
    # so you can traverse only to older generations
    lis = [tup[::-1] for tup in ancestors]
    # create the directed graph
    graph = {}
    for tup in lis:
        if tup[0] in graph:
            graph[tup[0]].add(tup[1])
        else:
            graph[tup[0]] = {tup[1]}
        if tup[1] in graph:
            continue
        else:
            graph[tup[1]] = set()
    # do a depth first traversal for the starting node
    stack = deque([starting_node])
    visited = set()
    while len(stack)>0:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            # return the furthest node
            if not graph[v]:
                print(graph[v])
                print(v)
            for n in graph[v]:
                stack.append(n)


test = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test, 3)