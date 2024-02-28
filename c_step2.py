"""
multiple edge, indirected graph
"""
n = int(input())
g = [[0]*n for _ in range(n)]
for i in range(n):
    g[i] = list(map(int, input().split()))

multiple_line =[]

for i in range(n):
    for j in range(i+1, n):
        if g[i][j] >= 2:
            multiple_line.append([i+1, j+1])

print(len(multiple_line))
for a, b in multiple_line:
    print(a, b)