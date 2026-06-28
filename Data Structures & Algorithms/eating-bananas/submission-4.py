class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        ans=0
        while left<=right:
            total=0
            mid=(left+right)//2
            for i in piles:
                total+=math.ceil(i/mid)
            if total<=h:
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans