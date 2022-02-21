from collections import defaultdict, deque


def shortestWordEditPath(source, target, words):
    words_s = set()
    for word in words:
        if len(word) == len(source):
            words_s.add(word)

    if target not in words_s:
        return -1

    # generate possible transitions from every word and append to graph
    graph = generateGraph(words_s)

    # generate possible transitions from source, append to graph
    addStart(source, graph, words_s)

    return bfs(source, target, graph)


def generateGraph(words_set):  # pog, dog
    graph = defaultdict(list)
    for word in words_set:  # pog,dog
        # generate a-z for every index and check if its in words set
        word_arr = list(word)  # p,o,g
        for x in range(len(word_arr)):  # 1..3x
            # go from a-z
            for c in range(ord('a'), ord('z')+1):
                char = chr(c)  # a
                if char != word[x]:
                    word_arr[x] = char
                    new_word = "".join(word_arr)  # dog
                    if new_word in words_set:
                        graph[word].append(new_word)
            word_arr[x] = word[x]
    return graph


def addStart(source, graph, word_set):
    # generate possible transitions for source
    word_arr = list(source)  # p,o,g
    for x in range(len(word_arr)):  # 1..3x
        # go from a-z
        for c in range(ord('a'), ord('z')+1):
            char = chr(c)  # a
            if char != source[x]:
                word_arr[x] = char
                new_word = "".join(word_arr)  # dog
                if new_word in word_set:
                    graph[source].append(new_word)
        word_arr[x] = source[x]


def bfs(source, target, graph):
    q = deque()
    q.append(source)
    size = 1
    visited = set()
    hops = 1

    while q:
        curr = q.popleft()
        for move in graph[curr]:
            if move not in visited:
                if move == target:
                    return hops
                q.append(move)
                visited.add(move)
        size -= 1
        if size == 0:
            hops += 1
            size = len(q)
    return -1
