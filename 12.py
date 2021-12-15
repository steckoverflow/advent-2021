def aoc12(filename):
    graph = {
        "start": [],
        "end": []
        }
    
    with open(filename, 'r') as f:
        for line in f.readlines():
            a, b = line.strip().split('-')
            if a not in graph.keys():
                graph[a] = []
            graph[a].append(b)
            if b not in graph.keys():
                graph[b] = []
            graph[b].append(a)
    
    node = 'start'
    path = [0, node] # path[0] added to track one revisit to small cave
    count = 0
    paths = [path]
    while len(paths) != 0:
        if node.islower() and path.count(node) > 1: # added for day 12B
            path[0] = 1
        for n in graph[node]:
            if n == 'start':
                continue
            if n == 'end':
                count += 1
                continue
            if n in path and n.islower() and path[0] == 1: # 'and path[0] == 1' added for day 12B 
                continue
            paths.append(path + [n])
        path = paths.pop()
        node = path[-1]
    
    print(count)

aoc12("input12-1.txt")
    
