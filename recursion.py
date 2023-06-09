from typing import List


def factorial(n: int):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# print(factorial(6))

def sum(arr: List[int]):
    if not arr:
        return 0
    else:
        return arr[0] + sum(arr[1:])

# print(sum([1,2,3,4]))


def count_items(arr: List[int]):
    if not arr:
        return 0
    return 1 + count_items(arr[1:])


# print(count_items([1,2,3,4]))


def max_num(arr: List[int]):
    # Base case: when the list is empty, return None
    if not arr:
        return None

    # Recursive case: compare the first element with the maximum element in the rest of the list
    # and return the larger of the two
    max_rest = max_num(arr[1:])
    if max_rest is not None and max_rest > arr[0]:
        return max_rest
    else:
        return arr[0]


# print(max_num([1,2,10,4]))


def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([10, 5, 2, 3]))
