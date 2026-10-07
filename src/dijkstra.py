"""
Project: Mini Courier Planner
Author: Vinayak Vashisth (Roll No: 2501730150)
Programme: B.Tech CSE (AI & ML)
Course: Design and Analysis of Algorithms (DAA)
"""

# Dijkstra's Algorithm for shortest paths

import heapq


def dijkstra(graph, source):
    """
    Find the shortest distance from source
    to every node in a weighted graph.

    graph:
        Dictionary where each node contains
        neighboring nodes and edge weights.

    source:
        Starting node.
    """

    distances = {
        node: float("inf")
        for node in graph
    }

    previous = {
        node: None
        for node in graph
    }

    distances[source] = 0

    priority_queue = [(0, source)]

    while priority_queue:

        current_distance, current_node = heapq.heappop(
            priority_queue
        )

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:

            new_distance = (
                current_distance + weight
            )

            if new_distance < distances[neighbor]:

                distances[neighbor] = new_distance
                previous[neighbor] = current_node

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor)
                )

    return distances, previous


def get_shortest_path(previous, source, destination):
    """
    Reconstruct the shortest path from source
    to destination using the previous-node map.
    """

    path = []
    current = destination

    while current is not None:

        path.append(current)

        if current == source:
            break

        current = previous[current]

    path.reverse()

    return path