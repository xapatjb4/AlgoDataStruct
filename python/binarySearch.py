#Template binary search
#pre reqs: array must be sorted
from typing import List
class BinSearch:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1

        #Stop when low > high
        while low <= high:
            #Get midway point
            mid = int((low + high)/2)

            #if number return midway point
            if nums[mid] == target:
                return mid

            #if number too low check right side by setting low to midway + 1
            if nums[mid] < target:
                low = mid + 1

            #if number to high chekc left side by setting high to midway - 1
            else :
                high = mid - 1


        #returns null if number not in list
        return -1
        