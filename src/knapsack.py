"""
Project: Mini Courier Planner
Author: Vinayak Vashisth (Roll No: 2501730150)
Programme: B.Tech CSE (AI & ML)
Course: Design and Analysis of Algorithms (DAA)
"""

# 0/1 Knapsack using Dynamic Programming


def knapsack(parcels, capacity):
    """
    Select parcels with maximum total value
    without exceeding vehicle capacity.
    """

    n = len(parcels)

    # DP table
    dp = [
        [0] * (capacity + 1)
        for _ in range(n + 1)
    ]

    # Build DP table
    for i in range(1, n + 1):

        weight = parcels[i - 1]["weight"]
        value = parcels[i - 1]["value"]

        for w in range(capacity + 1):

            if weight <= w:

                dp[i][w] = max(
                    dp[i - 1][w],
                    value + dp[i - 1][w - weight]
                )

            else:
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find selected parcels
    selected_parcels = []

    w = capacity

    for i in range(n, 0, -1):

        if dp[i][w] != dp[i - 1][w]:

            selected_parcels.append(
                parcels[i - 1]
            )

            w -= parcels[i - 1]["weight"]

    selected_parcels.reverse()

    return selected_parcels, dp