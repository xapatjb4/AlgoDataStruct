'''
Template for problems that apply binary search
'''

'''
def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    # could be [0, n], [1, n] etc. Depends on problem
    left, right = min(search_space), max(search_space)
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left
'''

'''
Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order. 
You may assume no duplicates in the array.
'''


def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left < right:
        mid = left + (right-left)//2
        if array[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left
