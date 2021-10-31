import random

class QuickSort:

    def __init__(self, arr):
        self.arr = arr 

    def swap(self, i1, i2):
        pom = self.arr[i1]
        self.arr[i1] = self.arr[i2]
        self.arr[i2] = pom 

    def splitArray(self, begin, end):
        split = random.randint(begin, end-1)
        splitValue = self.arr[split]

        self.swap(split, end-1)

        pos = begin 
        for x in range(begin, end-1):
            if self.arr[x] < splitValue:
                self.swap(x, pos)
                pos += 1

        self.swap(pos, end-1)

        return pos 

    def quickSort(self, begin, end):
        if begin < end:
            pivot = self.splitArray(begin, end)
            self.quickSort(begin, pivot)
            self.quickSort(pivot+1, end)

    def sort(self):
        self.quickSort(0, len(self.arr))

        return self.arr 


sort = QuickSort([1, 11, 52, 12, 11115, 3, 6, 9111, 12, 1])

print(sort.sort())
