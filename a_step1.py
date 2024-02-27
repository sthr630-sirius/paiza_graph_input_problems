"""
output adjacency matrix, indirected graph
"""
n, m = map(int, input().split())
g = [[0]*n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a][b] = 1
    g[b][a] = 1

for gi in g:
    print(*gi)