from typing import List
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        if arr[0]>=arr[1]:
            return False
        inc=1
        m=1
        while m<=len(arr)-2:
            i=arr[m]
            j=arr[m+1]
            if i==j:
                return False
            elif i>j:
                inc=0
                break
            m+=1
        print(m)

        if inc==1:
            return False
        while m<len(arr)-2:
            i=arr[m]
            j=arr[m+1]
            if i<=j:
                return False
            m+=1
        i=arr[m]
        j=arr[m+1]
        if i<=j:
            return False
        elif inc==0:
            return True
            
