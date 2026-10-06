INF = 9999

print("Enter number of vertices:")
n = int(input())

graph = []
dist = []

print("Enter the adjacency matrix:")
print("(Enter 9999 for INF)")

# Input and initialize distance matrix
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    dist.append(row.copy())

# Floyd-Warshall Algorithm
for k in range(n):
    for i in range(n):
        for j in range(n):

            if (dist[i][k] != INF and
                dist[k][j] != INF and
                dist[i][k] + dist[k][j] < dist[i][j]):

                dist[i][j] = dist[i][k] + dist[k][j]

# Display shortest distance matrix
print("\nShortest Distance Matrix:")

for i in range(n):
    for j in range(n):

        if dist[i][j] == INF:
            print("INF", end="\t")
        else:
            print(dist[i][j], end="\t")

    print()