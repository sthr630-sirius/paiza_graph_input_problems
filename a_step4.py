"""
input adjacency matrix, judge existence of edge
"""
n, q = map(int, input().split())
g = []
for _ in range(n):
    g.append(list(map(int, input().split())))
for _ in range(q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    print(g[a][b])
