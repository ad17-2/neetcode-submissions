class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        res = float('inf')

        most_efficient_time = max(piles)
        most_inefficient_time = 1

        while most_inefficient_time <= most_efficient_time:
            mid_time = (most_inefficient_time + most_efficient_time) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / mid_time)
            
            if hours <= h:
                res = mid_time
                most_efficient_time = mid_time - 1
            else:
                most_inefficient_time = mid_time + 1

        return res