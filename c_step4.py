"""
multiple edge, directed graph
"""
n = int(input())
g = [[0]*n for _ in range(n)]
for i in range(n):
    g[i] = list(map(int, input().split()))

multiple_edge = []

for i in range(n):
    for j in range(i+1, n):
        if (g[i][j] + g[j][i]) >= 2 :
            multiple_edge.append([i+1, j+1])

print(len(multiple_edge))
for a, b in multiple_edge:
    print(a, b)