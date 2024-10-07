def radix_sort(arr):
    shift = min(arr)
    arr = [x - shift for x in arr]
    
    l = len(str(max(arr)))
    arr = [f"%.{l}d"%x  for x in arr]
    
    for i in range(l - 1, -1, -1):
        counts = [0] * 10
        
        for j in arr:
            counts[int(j[i])] += 1
        
        for j in range(1, len(counts)):
            counts[j] += counts[j - 1]
        
        res = [0] * len(arr)
        
        for j in arr[-1::-1]:
            counts[int(j[i])] -= 1
            res[counts[int(j[i])]] = j
        
        for j in range(len(arr)):
            arr[j] = res[j]
    
    arr = [int(i) + shift for i in arr]

arr = [-15, 1, 2, -890, 901, 105]

radix_sort(arr)

print(arr)
