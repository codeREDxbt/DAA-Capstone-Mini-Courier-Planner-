"""
Project: Mini Courier Planner
Author: Vinayak Vashisth (Roll No: 2501730150)
Programme: B.Tech CSE (AI & ML)
Course: Design and Analysis of Algorithms (DAA)
"""

# Merge Sort for parcel prioritization

def merge_sort(parcels):
    """
    Sort parcels in descending order of priority.
    If priorities are equal, earlier deadline comes first.
    """

    if len(parcels) <= 1:
        return parcels

    mid = len(parcels) // 2

    left = merge_sort(parcels[:mid])
    right = merge_sort(parcels[mid:])

    return merge(left, right)


def merge(left, right):
    """Merge two sorted parcel lists."""

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if (
            left[i]["priority"] > right[j]["priority"]
            or (
                left[i]["priority"] == right[j]["priority"]
                and left[i]["deadline"] < right[j]["deadline"]
            )
        ):
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result