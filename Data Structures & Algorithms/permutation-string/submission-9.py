class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        m=len(s2)
        if n>m:
            return False
        s1_dict={}
        s2_dict={}
        for right in range(0,n):
            if s1[right] in s1_dict:
                s1_dict[s1[right]]+=1
            else:
                s1_dict[s1[right]]=1
        
        for i in range(0,n):
            if s2[i] in s2_dict:
                s2_dict[s2[i]]+=1
            else:
                s2_dict[s2[i]]=1
        
        if s1_dict==s2_dict:
            return True

        for right in range(n,m):
            if s2[right] in s2_dict:
                s2_dict[s2[right]]+=1
            else:
                s2_dict[s2[right]]=1

            outgoing=s2[right-n]
            s2_dict[outgoing]-=1

            if s2_dict[outgoing]==0:
                del s2_dict[outgoing]
            
            if s1_dict==s2_dict:
                return True
        return False