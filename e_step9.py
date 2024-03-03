def WeaklyConnectedSemiEuler(indegree, outdegree):
    isWeaklyConnectedSemiEuler = True
    i_counter = 0
    o_counter = 0

    for ideg, odeg in zip(indegree, outdegree):
        if ideg != odeg:
            if ideg + 1 == odeg:
                i_counter += 1
            elif ideg == odeg + 1:
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

n = int(input())
word = []
top_word_dict = {}
last_word_dict = {}

indegree = [0]*26
outdegree = [0]*26

for _ in range(n):
    w = input()
    a = ord(list(w)[0])-97
    b = ord(list(w)[-1])-97
    outdegree[a] += 1
    indegree[b] += 1

#print(indegree)
#print(outdegree)

WeaklyConnectedSemiEuler(indegree, outdegree)