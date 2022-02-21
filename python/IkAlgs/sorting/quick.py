import random


def qsort(elems):
    qsortHelper(elems, 0, len(elems)-1)


def qsortHelper(elems, start, end):
    if end <= start:  # only one or no elements to sort
        return
    iPivot = partition(elems, start, end)
    qsortHelper(elems, start, iPivot-1)
    qsortHelper(elems, iPivot+1, end)


'''
partition(arr[], lo, hi) 
    pivot = arr[hi]
    i = lo     // place for swapping
    for j := lo to hi – 1 do
        if arr[j] <= pivot then
            swap arr[i] with arr[j]
            i = i + 1
    swap arr[i] with arr[hi]
    return i
'''


def partition(elems, start, end):  # Aka lomutos partition
    # return index of pivot for partitioned array
    iLeft = start
    iRight = start + 1
    while iRight <= end:
        if elems[iRight] <= elems[start]:
            iLeft += 1
            elems[iLeft], elems[iRight] = elems[iRight], elems[iLeft]
        iRight += 1
    elems[start], elems[iLeft] = elems[iLeft], elems[start]
    return iLeft


'''
partition(arr[], lo, hi)
   pivot = arr[lo]
   i = lo - 1  // Initialize left index
   j = hi + 1  // Initialize right index

   // Find a value in left side greater
   // than pivot
   do
      i = i + 1
   while arr[i] < pivot

   // Find a value in right side smaller
   // than pivot
   do
      j--;
   while (arr[j] > pivot);

   if i >= j then 
      return j

   swap arr[i] with arr[j]
'''


def hpartition(elems, start, end):
    pass


for x in range(1000):
    test = [random.randint(0, 9) for x in range(10)]
    print(test)
    qsort(test)
    isSorted = all(test[i] <= test[i+1] for i in range(len(test)-1))
    print(test)
    if not isSorted:
        print('is not sorted')
        break
