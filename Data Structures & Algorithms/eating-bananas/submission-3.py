class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            k = (left + right) // 2
            lst = []

            for i in range(len(piles)):
                a = piles[i]
                x = math.ceil(a / k)
                lst.append(x)

            if sum(lst) <= h:
                right = k - 1
            else:
                left = k + 1

        return left