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
    stack = deque([[starting_node]])
    visited = set()
    # keep track of the longest traversal/path, or earliest ancestor path
    longest_path = []
    while len(stack)>0:
        path = stack.pop()
        v = path[-1]
        if v not in visited:
            visited.add(v)
            # check if has no ancestors
            if not graph[v]:
                if len(path)>len(longest_path):
                    longest_path = path
            for n in graph[v]:
                stack.append(path + [n])
                
    # return the earliest ancestor or -1 if starting node doesn't have any ancestors
    ancestor = longest_path[-1]
    return -1 if ancestor==starting_node else ancestor


test = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test, 2))