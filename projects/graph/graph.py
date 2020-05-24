"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise ValueError("ERROR: Vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError("ERROR: Vertex does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue
        # Enqueue the starting vertex
        # Create a set to store visited vertices 
        # While the queue is not empty...
            # Dequeue the first vertex
            # Check if it's been visited
            # If it hasn't been visited...
                # Mark it as visited
                # Enqueue all its neighbors
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                print(v)
                visited.add(v)
                for n in self.get_neighbors(v):
                    q.enqueue(n)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a stack
        # Push the starting vertex
        # Create a set to store visited vertices
        # While the stack is not empty...
            # Pop the first vertex
            # Check if it's been visited
            # If it hasn't been visited...
                # Mark it as visited
                # Push all its neighbors to stack
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                visited.add(v)
                print(v)
                for n in self.get_neighbors(v):
                    s.push(n)

    def dft_recursive(self, vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Check if the node has been visited
        # If not...
            # Mark it as visited
            # Call dft_recursive on each neighbor

        # either us a helper function inside or pass a cache
        if not visited:
            visited = set()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)
            for n in self.get_neighbors(vertex):
                self.dft_recursive(n, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue
        # Enqueue A PATH TO the starting vertex
        # Create a set to store visited vertices
        # While the queue is not empty...
            # Dequeue the first PATH
            # GRAB THE VERTEX FROM THE END OF THE PATH
            # Check if it's been visited
            # If it hasn't been visited...
                # Mark it as visited
                # CHECK IF IT'S THE TARGET
                    # IF SO, RETURN THE PATH
                # Enqueue A PATH TO all its neighbors, to do that:
                    # MAKE A COPY OF THE PATH
                    # ENQUEUE THE COPY
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()
        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]
            if v not in visited:
                visited.add(v)
                if v==destination_vertex:
                    return path
                for n in self.get_neighbors(v):
                    q.enqueue(path + [n])

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a stack
        # push a path to the starting vertex
        # create set to store visited vertices
        # While the stack is not empty...
            # pop the first path
            # grab the vertex from the end of that path
            # if the vertex hasn't been visited...
                # mark it as visited
                # if it is the target...
                    # return the path to that vertex
                # push a path to each of its neighbors
        s = Stack()
        s.push([starting_vertex])
        visited = set()
        while s.size() > 0:
            path = s.pop()
            v = path[-1]
            if v not in visited:
                visited.add(v)
                if v==destination_vertex:
                    return path
                for n in self.get_neighbors(v):
                    s.push(path + [n])

    def dfs_recursive(self, vertex, destination, path=None, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # check if vertex is visited...
            # if so, return
        # create a new_path from old_path + list(vertex)
        # add vertex to visited
        # if vertex is the destination..
            # return new_path
        # for each of the current vertex's neighbors..
            # recursively call the function and pass in the neighbor, destination, new_path, and visited
        if not path: path=list()
        if not visited: visited=set()

        if vertex not in visited:
            visited.add(vertex)
            new_path = path + [vertex]
            if vertex==destination:
                return new_path
            for n in self.get_neighbors(vertex):
                p = self.dfs_recursive(n, destination, new_path, visited)
                if p: return p

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
