class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dict={}
        for i in range(len(s)):
            dict[s[i]]=i
        #  x → 3 ,y → 4 ,z → 7 ,b → 9 ,i → 10 ,s → 11 ,l → 12
        l=0
        r=0
        ans=[]
        for i in range(0,len(s)):
            r=max(r,dict[s[i]])
            if i==r:
                ans.append(r-l+1)
                l=i+1
        return ans