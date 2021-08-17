# Hash Table/Hash Map is implemented in python using built in datatype dictionary

class HashTable:
    def __init__(self, max_size):
        self.max_size = max_size
        self.arr = [[] for _ in range(max_size)]

    def hashFunc(self, val):
        sum_ch = 0
        for ch in str(val):
            sum_ch += sum_ch + ord(ch)

        return sum_ch % self.max_size

    def __setitem__(self, key, value):
        idx = self.hashFunc(key)
        self.arr[idx].append((key, value))

    def __getitem__(self, key):
        idx = self.hashFunc(key)
        for tup in self.arr[idx]:
            if tup[0] == key:
                return tup[1]

    def __delitem__(self, key):
        idx = self.hashFunc(key)
        counter = 0
        for tup in self.arr[idx]:
            if tup[0] == key:
                break
            counter += 1

        del self.arr[idx][counter]

    def __len__(self):
        counter = 0
        for lst in self.arr:
            for tup in lst:
                counter += 1

        return counter

    def __iter__(self):
        self.n = 0
        self.keys = []
        for lst in self.arr:
            for tup in lst:
                self.keys.append(tup[0])
        return self

    def __next__(self):
        if self.n < len(self.keys):
            result = self.keys[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration



ht = HashTable(10)
ht["15August2021"] = 100
ht["16August2021"] = 200
ht["17August2021"] = 300
ht["18August2021"] = 400
ht["19August2021"] = 500
ht["20August2021"] = 600
ht["21August2021"] = 700
ht["22August2021"] = 800
ht["23August2021"] = 900
ht["24August2021"] = 1000
ht["25August2021"] = 1100
ht["26August2021"] = 1200
ht["march 6"] = 110
ht["march 17"] = 120
print(ht.arr)
print(ht["22August2021"])
print("--- del key = 20August2021---")
del ht["20August2021"]
print(ht.arr)
print("length of hash table: ", len(ht))
print("**************")
for key in ht:
    print(key)