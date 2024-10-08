class Quick_Sort:
    def __init__(self, arr):
        self.arr = arr
        self.quicksort(self.arr, 0, len(self.arr) - 1)

    def position(self, arr, lb, up):
        pivot = lb
        start = lb
        end = up
        while start < end:
            while arr[start] <= arr[pivot] and start < up:
                start += 1
            while arr[end] > arr[pivot] and end > lb:
                end -= 1
            if start < end:
                arr[start], arr[end] = arr[end], arr[start]
        arr[pivot], arr[end] = arr[end], arr[pivot]
        return end

    def quicksort(self, arr, lb, up):
        if lb < up:
            loc = self.position(arr, lb, up)
            self.quicksort(arr, lb, loc - 1)
            self.quicksort(arr, loc + 1, up)
# Example
arr = [3, 6, 8, 10, 1, 2, 1]
qs = Quick_Sort(arr)
print(arr)
