"""
multiple edge, directed graph
"""
n, m = map(int, input().split())
g = [[0]*n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a][b] += 1

multiple_edge = []

for i in range(n):
    for j in range(i+1, n):
        if (g[i][j]+g[j][i]) >= 2:
            multiple_edge.append([i+1, j+1])

print(len(multiple_edge))
for a, b in multiple_edge:
    print(a, b)