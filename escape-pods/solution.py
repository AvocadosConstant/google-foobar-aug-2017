""" Tim Hung timhung1010@gmail.com """

from future_builtins import zip

INF = float('inf')

def find_augmented_path(graph, source, sink):
    """ Uses BFS to find an augmented path """
    queue = [source]
    parent_map = {}
    visited = set()

    # bfs to find the sink
    while queue:
        cur = queue.pop(0)
        for next_room, cap in enumerate(graph[cur]):
            # has capacity and is unvisited
            if cap and next_room not in visited:
                queue.append(next_room)
                visited.add(next_room)
                parent_map[next_room] = cur
                if next_room == sink:
                    # exit bfs
                    queue = []

    if sink not in visited:
        return None

    # build augmented path from parent_map
    aug_path = [sink]
    while aug_path[0] != source:
        aug_path.insert(0, parent_map[aug_path[0]])

    return aug_path


def min_flow_in_path(graph, path):
    min_flow = INF
    for start, dest in zip(path, path[1:]):
        min_flow = min(min_flow, graph[start][dest])
    return min_flow


def saturate_flow(graph, path, min_flow):
    """ Saturates the corresponding residual capacities for an augmented path """
    for start, dest in zip(path, path[1:]):
        graph[start][dest] -= min_flow
        if dest < len(graph):
            graph[dest][start] += min_flow


def edmonds_karp(graph, source, sink):
    """ Calculates max flow using Edmonds-Karp Algorithm """
    max_flow = 0
    while True:
        aug_path = find_augmented_path(graph, source, sink)
        if not aug_path:
            return max_flow

        min_flow = min_flow_in_path(graph, aug_path)

        if min_flow == 0:
            return max_flow

        max_flow += min_flow

        saturate_flow(graph, aug_path, min_flow)

    return max_flow


def resolve_multi_sink_source(graph, entrances, exits):
    """ Creates a supersource and supersink """
    source = len(graph)
    sink = source + 1

    # add two new dimensions for supersource and supersink
    for i, room in enumerate(graph):
        room.extend([0, INF if i in exits else 0])

    graph.append([0] * (sink + 1))

    # add row for supersource edges
    for entrance in entrances:
        graph[source][entrance] = INF

    return source, sink


def answer(entrances, exits, path):
    # adjacency matrix
    graph = [list(row) for row in path]

    source, sink = resolve_multi_sink_source(graph, entrances, exits)
    return edmonds_karp(graph, source, sink)
