

# when implementing a hash table
# you want to define __setItem__(key, value): this adds an item to the list which the key hashes to
# __getItem__(key): this gets the item based on the value
# resize: for if we pass a threshold for array capacity
# delete

class HashMap:

    def __init__(self, size=7):
        self.n = 0
        self.table = [[] for _ in range(size)]

    def __setitem__(self, key, value):
        # hash key, check that index at hash(key) not none
        # check that value with that key does not exist
        # append to list, or update
        ni = self.Item(key, value)
        h = hash(key) % len(self.table)
        isUpdate = False
        print('hash key is')
        print(h)
        for i in self.table[h]:
            print('lookin at item')
            print(i)
            if i.key == ni.key:
                i.value = ni.value
                isUpdate = True
                break

        if not isUpdate:
            self.table[h].append(ni)
            self.n += 1
            print('new bucket content')
            print(self.table[h])

        if self.isPassedT():
            print('is resizing')
            self.resize()

    def isPassedT(self):
        print('printing array fulness')
        print(self.n / len(self.table))
        return self.n / len(self.table) > 0.5

    def resize(self):
        # copy everythin into a new array
        # set item on all elements
        aux = []
        for bucket in self.table:
            print('bucket is')
            print(bucket)
            for i in bucket:
                aux.append(i)

        self.table = [[] for _ in range(len(self.table)*2)]
        self.n = 0
        print('printing empty table')
        print(self.table)
        print(aux)

        for i in aux:
            self[i.key] = i.value
        print(self.table)

    def __getitem__(self, key):
        h = hash(key) % len(self.table)
        bu = self.table[h]

        for i in bu:
            if i.key == key:
                return i.value

        raise KeyError('No key with that value found')

    class Item:
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __repr__(self):
            return 'key: {}, value: {}'.format(self.key, self.value)


h = HashMap()
h['yo'] = 'yoa'
h['yo'] = 'yoaa'
h['ya'] = 'yoa'
h['y3'] = 'yoa'
h['ye'] = 'yoa'
h['yq'] = 'yoa'
print(h['yo'])
