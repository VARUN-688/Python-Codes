class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        x=[x for x in nums if len(str(x))%2==0 ]
        return len(x)
# s=Solution()
# s.findNumbers([12,345,2,6,7896])->2
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits
