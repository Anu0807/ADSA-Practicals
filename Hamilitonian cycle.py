n = int(input("Enter number of vertices: "))
g = []

for i in range(n):
    g.append(list(map(int, input().split())))

path = [0]

def solve(v):
    if len(path) == n:
        return g[path[-1]][path[0]] == 1

    for i in range(1, n):
        if i not in path and g[v][i] == 1:
            path.append(i)

            if solve(i):
                return True

            path.pop()

    return False

if solve(0):
    path.append(0)
    print("Hamiltonian Cycle:", path)
else:
    print("No Hamiltonian Cycle")