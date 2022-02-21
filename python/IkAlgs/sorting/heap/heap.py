import random


class Heap:
    def __init__(self, elems):
        self.elems = elems
        self.size = len(elems)
        self.buildMaxHeap()

    def buildMaxHeap(self):
        mid = self.size // 2
        for x in range(mid - 1, -1, -1):
            self.maxHeapify(x)

    # recursive max heapify
    # def maxHeapify(self, x):
    #     largest = x

    #     if self.left(x) < self.size and self.elems[largest] < self.elems[self.left(x)]:
    #         largest = self.left(x)
    #     if self.right(x) < self.size and self.elems[largest] < self.elems[self.right(x)]:
    #         largest = self.right(x)
    #     if largest != x:
    #         self.elems[largest], self.elems[x] = self.elems[x], self.elems[largest]
    #         self.maxHeapify(largest)

    def maxHeapify(self, x):
        ix = x
        while True:
            il = ix
            if self.left(ix) < self.size and self.elems[ix] < self.elems[self.left(ix)]:
                il = self.left(ix)
            if self.right(ix) < self.size and self.elems[il] < self.elems[self.right(ix)]:
                il = self.right(ix)
            if il == ix:
                break
            else:
                self.elems[il], self.elems[ix] = self.elems[ix], self.elems[il]
                ix = il

    def sort(self):
        elems = self.elems
        for x in range(len(elems) - 1, 0, -1):
            elems[0], elems[x] = elems[x], elems[0]
            self.size -= 1
            self.maxHeapify(0)

    def left(self, x):
        return 2*x + 1

    def right(self, x):
        return 2*x + 2

    def parent(self, x):
        return (x+1)//2 - 1  # 0 = -1, 1 and 2 = 0, 3 and 4 = 1 ...

    def max(self, x):
        if self.size < 1:
            raise Exception('Heap empty')
        return self.elems[0]

    def extractMax(self):
        if self.size < 1:
            raise Exception('Heap empty')
        max = self.elems[0]
        self.elems[0] = self.elems[self.size - 1]
        self.size -= 1
        self.maxHeapify(0)
        return max

    def increaseKey(self, x, key):
        if x >= self.size:
            raise Exception('Out of bounds')
        if key < self.elems[x]:
            raise Exception('We need a bigger key')
        self.elems[x] = key

        while x > 0 and self.elems[self.parent(x)] < self.elems[x]:
            parent = self.parent(x)
            self.elems[parent], self.elems[x] = self.elems[x], self.elems[parent]
            x = parent

    def insert(self, x):
        self.increaseSize()
        self.elems[self.size - 1] = x  # access last index
        self.increaseKey(self.size - 1, x)

    def increaseSize(self):
        if self.size + 1 >= len(self.elems):
            self.elems.append(None)
        self.size += 1


for x in range(1000):
    test = [random.randint(0, 9) for x in range(10)]

    print('b4')
    print(test)
    heap = Heap([])
    for num in test:
        heap.insert(num)
    newArr = [heap.extractMax() for x in range(10)]
    test = newArr

    isSorted = all(test[i] >= test[i+1] for i in range(len(test)-1))
    print('a4')
    print(test)
    if not isSorted:
        print('is not sorted')
        break
