# Reference taken from https://gist.github.com/amitabhadey/37af83a84d8c372a9f02372e6d5f6732


graph = {

'a':{'b':7,'c':9, 'd':7},
'b':{'c':1,'f':5},
'c':{'f':6,'d':7},
'd':{'e':3, 'g':6},
'e':{'g':6, 'h':4},
'f':{'e':1, 'h':8},
'g':{'h':8},
'h':{'g':2}
}


def dijkstra(graph,source,destination):

    track_predecessor,unseenNodes,infinity,track_path = {},graph,float('inf'),[]  # required variable assignment

    shortest_distance =  dict(zip([x for x in unseenNodes.keys()] ,[ 0 if source == node else infinity for node in unseenNodes])) # Assing 0 to source node and infinity to rest nodes


    while unseenNodes:
        min_distance_node = None
        for node in unseenNodes:
            if min_distance_node is None or shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node
        for child_node, weight in graph[min_distance_node].items():
            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                track_predecessor[child_node] = min_distance_node

        unseenNodes.pop(min_distance_node) # removing visited node

    currentNode,loop_continue = destination,True
    while currentNode != source and loop_continue:
        try:
            track_path.insert(0,currentNode)
            currentNode = track_predecessor[currentNode]
        except KeyError:
            print(f'Path not reachable with the {currentNode}')
            loop_continue = False
    track_path.insert(0,source)


    if shortest_distance[destination] != infinity:
        print(f'Shortest distance in between {source} and {destination} is {shortest_distance[destination]}')
        print(f'The path which gets the shortest distance is { " -->> ".join(track_path)}')


dijkstra(graph, 'a', 'h') # call dijkstra function with necessary argument