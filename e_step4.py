"""
degree euler graph, indirected graph
全ての辺を一筆書きすることができる必要十分条件
(semi euler graphであることの必要十分条件)
「次数が奇数である頂点の個数が、ちょうど0または2」
"""
n, m = map(int, input().split())
degree = [0]*n
counter = 0
#isSemiEuler = True

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    degree[a] += 1
    degree[b] += 1

for d in degree:
    if d%2 == 1:
        counter += 1

if counter == 0 or counter == 2:
    print(1)
else:
    print(0)
