class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid = l + (r - l) // 2
            hourCount = 0

            # Calculate total hours to finish all piles with speed mid
            for pile in piles:
                hourCount += math.ceil(pile / mid)

            # If Koko can finish all piles within h hours, try a smaller speed
            if hourCount <= h:
                res = mid  # Update the result with a valid speed
                r = mid - 1
            else:
                l = mid + 1

        return res
