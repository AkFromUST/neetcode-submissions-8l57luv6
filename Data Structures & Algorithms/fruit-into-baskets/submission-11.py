class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # sliding window, ayayaya
        l, total, res = 0, 0, 0
        n = len(fruits)

        count = defaultdict(int)

        for r in range(n):
            count[fruits[r]] += 1
            total += 1

            while len(count) > 2:
                # keep removing the l
                element = fruits[l]
                count[element] -= 1
                total -= 1
                l += 1

                if not count[element]:
                    count.pop(element)
            
            res = max(res, total)

        return res