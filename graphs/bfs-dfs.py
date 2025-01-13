"""
BFS(graph, start_node):
  queue = new Queue()
  visited = new Set()

  queue.enqueue(start_node)
  visited.add(start_node)

  while queue is not empty:
    current_node = queue.dequeue()
    process(current_node) // Do something with the current node

    for neighbor in graph.neighbors(current_node):
      if neighbor is not in visited:
        queue.enqueue(neighbor)
        visited.add(neighbor)
"""

"""
    A
   / \
  B   C
 / \   \
D   E   F

BFS starting from node A:

Start: Queue: [A], Visited: {A}
Dequeue A: Process A. Neighbors of A: B, C. Queue: [B, C], Visited: {A, B, C}
Dequeue B: Process B. Neighbors of B: D, E. Queue: [C, D, E], Visited: {A, B, C, D, E}
Dequeue C: Process C. Neighbor of C: F. Queue: [D, E, F], Visited: {A, B, C, D, E, F}
Dequeue D: Process D. D has no unvisited neighbors. Queue: [E, F], Visited: {A, B, C, D, E, F}
Dequeue E: Process E. E has no unvisited neighbors. Queue: [F], Visited: {A, B, C, D, E, F}
Dequeue F: Process F. F has no unvisited neighbors. Queue: [], Visited: {A, B, C, D, E, F}
BFS traversal order: A, B, C, D, E, F
"""

# dfs

"""
DFS(graph, current_node, visited):
  visited.add(current_node)
  process(current_node)

  for neighbor in graph.neighbors(current_node):
    if neighbor is not in visited:
      DFS(graph, neighbor, visited)
"""

"""
    A
   / \
  B   C
 / \   \
D   E   F

DFS starting from node A (using the recursive approach):

Start: Visited: {A}
Explore B: Visited: {A, B}
Explore D: Visited: {A, B, D}
D has no unvisited neighbors. Backtrack to B.
Explore E: Visited: {A, B, D, E}
E has no unvisited neighbors. Backtrack to B.
B has no more unvisited neighbors. Backtrack to A.
Explore C: Visited: {A, B, D, E, C}
Explore F: Visited: {A, B, D, E, C, F}

DFS traversal order: A, B, D, E, C, F
"""
