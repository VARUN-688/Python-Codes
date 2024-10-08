class Array:
    def __init__(self, arr):
        self.arr = arr

    def quicksort(self, arr=None):
        if arr is None:
            arr = self.arr
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quicksort(left) + middle + self.quicksort(right)

    def sort(self):
        self.arr = self.quicksort()
    
    def __str__(self):
        return f"The array is = {self.arr}"

# Example
arr = Array([-1, 2, 1, 0, -100])
arr.sort()
print(arr)
