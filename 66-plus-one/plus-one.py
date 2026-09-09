class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        for i in range(len(digits)):
            num=num*10+digits[i]
        numb=num+1
        res=[]
        while numb>0:
            digit=numb%10
            res.append(digit)
            numb=numb//10
        return res[::-1]