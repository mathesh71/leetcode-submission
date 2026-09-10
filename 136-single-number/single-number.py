class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen={}
        for i in nums:
            seen[i]=seen.get(i,0)+1
        for key,value in seen.items():
            if value==1:
                return key
                