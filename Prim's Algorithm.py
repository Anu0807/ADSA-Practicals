# Prim's Algorithm - Minimum Spanning Tree

V = 5   # Number of vertices


def min_key(key, mst_set):
    minimum = float('inf')
    min_index = -1

    for v in range(V):
        if mst_set[v] == False and key[v] < minimum:
            minimum = key[v]
            min_index = v

    return min_index


def prim_mst(graph):
    parent = [-1] * V
    key = [float('inf')] * V
    mst_set = [False] * V

    # Start from vertex 0
    key[0] = 0
    parent[0] = -1

    for count in range(V - 1):
        # Pick minimum key vertex
        u = min_key(key, mst_set)

        # Add vertex to MST
        mst_set[u] = True

        # Update adjacent vertices
        for v in range(V):
            if graph[u][v] != 0 and mst_set[v] == False \
                    and graph[u][v] < key[v]:
                parent[v] = u
                key[v] = graph[u][v]

    # Print MST
    print("Edge\tWeight")

    for i in range(1, V):
        print(parent[i], "-", i, "\t", graph[i][parent[i]])


# Example graph
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

prim_mst(graph)
