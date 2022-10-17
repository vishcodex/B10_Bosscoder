class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo, hi = max(weights), sum(weights)
        while lo <= hi:
            mid = (lo + hi) // 2
            if not self.is_possible(weights, days, mid):
                lo = mid + 1
            else:
                hi = mid - 1
        return lo
    
    def is_possible(self, weights, days, size):
        t = 0
        for w in weights:
            t += w
            if t > size:
                days -= 1
                t = w
                if days == 0:
                    break
        return days > 0