class Solution:
    def reverseWords(self, s: str) -> str:
        s1=s.split()
        ans=[]
        for i in range(len(s1)-1,-1,-1):
            ans.append(s1[i])
        return " ".join(ans)