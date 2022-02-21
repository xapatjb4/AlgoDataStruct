def binSearch(elems, key):
    start = 0
    end = len(elems)-1
    while start <= end:
        mid = (start + end) // 2
        if elems[mid] == key:
            return mid
        elif elems[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return None


test = [1, 3, 4, 5, 6, 8, 9]
print(binSearch(test, 10))
