class Heap:
    def min_heap(self,arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.min_heap(arr, n, largest)

    def heap_push(self,arr,elm):
        arr.append(elm)
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            self.min_heap(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.min_heap(arr, i, 0)

    def heap_pop(self,arr):
        return arr.pop(0)
