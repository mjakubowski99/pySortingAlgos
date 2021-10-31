import random 

class MergeSort:

    def __init__(self, arr):
        self.arr = arr

    def merge(self, begin, pivot, end):
        mergeArr = []
        i, j = begin, pivot+1
        while True:
            if i > pivot:
                while j <= end:
                    mergeArr.append(self.arr[j-1])
                    j+=1
                break
            if j > end:
                while i <= pivot:
                    mergeArr.append(self.arr[i-1])
                    i+=1
                break      

            if self.arr[i-1] <= self.arr[j-1]:
                mergeArr.append(self.arr[i-1])
                i+=1
            else:
                mergeArr.append(self.arr[j-1])
                j+=1

        i, j = begin, 0 
        while i <= end:
            self.arr[i-1] = mergeArr[j]
            i+=1
            j+=1

    def mergeSort(self, begin, end):
        if( begin < end ):
            pivot = (begin + end)//2 

            self.mergeSort(begin, pivot)
            self.mergeSort(pivot+1, end)

            self.merge(begin, pivot, end)

    def sort(self):
        self.mergeSort(1, len(self.arr))
        return self.arr 


test = [ random.randint(0, 20) for x in range(0,30) ]
sort = MergeSort(test)
print( sort.sort() )


