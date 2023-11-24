from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m=0
        i=0
        c=0
        while i<len(nums):
            if nums[i]==1:
                x=0
                j=i
                while j<len(nums):
                    if nums[j]!=1:break
                    else:
                        j+=1
                        x+=1
                        c+=1
                i=c
                if m<x:
                    m=x
            else:
                i+=1
                
        return m
# s=Solution()
# s.findMaxConsecutiveOnes([1,0,1,1,0,1])
