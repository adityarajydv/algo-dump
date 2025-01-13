from collections import defaultdict

class Graph:
    """Represents a graph using an adjacency list."""

    def __init__(self, vertices):
        """Initializes the graph with a given number of vertices."""
        self.vertices = vertices
        self.adj = defaultdict(list)  # Adjacency list

    def add_edge(self, u, v, directed=False):
        """Adds an edge to the graph.

        Args:
            u: The starting vertex.
            v: The ending vertex.
            directed: True if the graph is directed, False otherwise (default).
        """
        self.adj[u].append(v)
        if not directed:
            self.adj[v].append(u)  # Add edge in the opposite direction for undirected graphs

    def is_directed(self):
        """Detects if the graph is directed.

        Returns:
            True if directed, False otherwise.
        """
        for u in self.adj:
            for v in self.adj[u]:
                if u not in self.adj or v not in self.adj[v] or u not in self.adj[v]:
                    return True  # If u->v exists, but v->u doesn't, it's directed
        return False

    def is_cyclic_util(self, v, visited, stack):
        """Utility function for cycle detection using DFS."""
        visited[v] = True
        stack[v] = True

        for neighbor in self.adj[v]:
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, stack):
                    return True
            elif stack[neighbor]:  # If neighbor is in the stack, there's a cycle
                return True

        stack[v] = False  # Backtrack
        return False

    def is_cyclic(self):
        """Detects if the graph is cyclic using DFS."""
        visited = [False] * (self.vertices + 1)
        stack = [False] * (self.vertices + 1)

        for vertex in range(1, self.vertices + 1):
            if not visited[vertex]:
                if self.is_cyclic_util(vertex, visited, stack):
                    return True

        return False

# Example Usage
# Input for nodes and edges
num_vertices = int(input("Enter the number of vertices: "))
graph = Graph(num_vertices)
num_edges = int(input("Enter the number of edges: "))

for _ in range(num_edges):
    u, v = map(int, input("Enter edge (u v): ").split())
    directed_input = input("Is this edge directed? (yes/no): ").lower()
    directed = directed_input == "yes"
    graph.add_edge(u, v, directed)

# Check if directed
if graph.is_directed():
    print("The graph is directed.")
else:
    print("The graph is undirected.")

# Check if cyclic
if graph.is_cyclic():
    print("The graph contains a cycle.")
else:
    print("The graph is acyclic.")

# Print the adjacency list (representation of the graph)
print("Adjacency List:")
for vertex, neighbors in graph.adj.items():
    print(f"{vertex}: {neighbors}")

# Example of graph creation in code
graph2 = Graph(4)
graph2.add_edge(1, 2)
graph2.add_edge(2, 3)
graph2.add_edge(3, 1)

if graph2.is_cyclic():
    print("graph2 contains a cycle.")
else:
    print("graph2 is acyclic.")

graph3 = Graph(4)
graph3.add_edge(1, 2, True)
graph3.add_edge(2, 3, True)
graph3.add_edge(3, 4, True)
graph3.add_edge(4, 2, True)

if graph3.is_cyclic():
    print("graph3 contains a cycle.")
else:
    print("graph3 is acyclic.")