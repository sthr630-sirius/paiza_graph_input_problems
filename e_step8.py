"""
euler graph, directed graph
weakly connected
有向グラフを無向グラフとみなした時に、どの２つの頂点間も辺をたどって行き来ができる：弱連結なグラフ
弱連結な有向グラフにおいて、全ての辺を一筆書きできる必要十分条件
(semi euler graphであることの必要十分条件)
「全ての頂点において、入次数と出次数が一致する」
or
「（入次数）=(出次数+1)となる頂点がちょうど1つ存在
（入次数+1）=(出次数)となる頂点がちょうど1つ存在
残りの全ての頂点について、入次数と出次数が一致
」
"""
n, m = map(int, input().split())
outdegree = [0]*n
indegree = [0]*n
isWeaklyConnectedSemiEuler = True
i_counter = 0
o_counter = 0

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    outdegree[a] += 1
    indegree[b] += 1

for ideg, odeg in zip(indegree, outdegree):
    if ideg != odeg:
        if ideg+1 == odeg:
            i_counter += 1
        elif ideg == odeg+1:
            o_counter += 1
        else:
            isWeaklyConnectedSemiEuler = False

if i_counter == 0 and o_counter == 0:
    pass
elif i_counter == 1 and o_counter == 1:
    pass
else:
    isWeaklyConnectedSemiEuler = False

if isWeaklyConnectedSemiEuler:
    print(1)
else:
    print(0)


