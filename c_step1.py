"""
loop vertex, indirected graph
"""
n = int(input())
g = [[0]*n for _ in range(n)]
for i in range(n):
    g[i] = list(map(int, input().split()))

loop_vertex = []

for i in range(n):
    if g[i][i] == 1:
        loop_vertex.append(i+1)

print(len(loop_vertex))
for v in loop_vertex:
    print(v)