"""
Project: Mini Courier Planner
Author: Vinayak Vashisth (Roll No: 2501730150)
Programme: B.Tech CSE (AI & ML)
Course: Design and Analysis of Algorithms (DAA)
"""

# Nearest-Neighbor TSP Approximation

import heapq


def shortest_path(graph, source, target):
    """
    Find the shortest path and distance between two nodes.
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

        if current_node == target:
            break

        for neighbor, weight in graph[current_node]:

            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:

                distances[neighbor] = new_distance
                previous[neighbor] = current_node

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor)
                )

    path = []
    current = target

    while current is not None:
        path.append(current)

        if current == source:
            break

        current = previous[current]

    path.reverse()

    return path, distances[target]


def nearest_neighbor_tsp(graph, start, destinations):
    """
    Generate a delivery route using
    Nearest-Neighbor TSP approximation.

    Returns:
        customer_order: Order of customer visits.
        route: Expanded shortest-path traversal.
        total_distance: Total route distance.
    """

    unvisited = set(destinations)

    current = start

    customer_order = [start]
    route = [start]
    total_distance = 0

    while unvisited:

        nearest_destination = None
        nearest_distance = float("inf")
        nearest_path = None

        for destination in unvisited:

            path, distance = shortest_path(
                graph,
                current,
                destination
            )

            if distance < nearest_distance:

                nearest_destination = destination
                nearest_distance = distance
                nearest_path = path

        # Add expanded shortest path
        route.extend(nearest_path[1:])

        # Add only the actual customer
        customer_order.append(nearest_destination)

        total_distance += nearest_distance

        current = nearest_destination

        unvisited.remove(nearest_destination)

    # Return to Warehouse
    return_path, return_distance = shortest_path(
        graph,
        current,
        start
    )

    route.extend(return_path[1:])

    customer_order.append(start)

    total_distance += return_distance

    return customer_order, route, total_distance