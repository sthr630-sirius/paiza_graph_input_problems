"""
loop vertex, directed graph
"""
n, m = map(int, input().split())

loop_vertex = []

for _ in range(m):
    a, b = map(int, input().split())
    if a == b:
        loop_vertex.append(a)

print(len(loop_vertex))
for a in sorted(loop_vertex):
    print(a)