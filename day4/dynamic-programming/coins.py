class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def coinChangeInner(amount, cache):
            if amount < 0:
                return math.inf
            if amount == 0:
                return 0
            if amount in cache:
                return cache[amount]
            
            cache[amount] = min(
                [coinChangeInner(amount - x, cache) + 1 for x in coins]
            )
            return cache[amount]
        
        ans = coinChangeInner(amount, {})
        return -1 if ans == math.inf else ans
