class Solution:
    
    #finding if this k is the correct one or not
    def _correctK(self, piles, h, k, totalS, maxi) -> int:

        if k >= piles[maxi]:
            return len(piles)
        else:
            #return (sum(piles) // k) + (sum(piles) % k)
        
            temp_piles = [piles[i] for i in range(len(piles))]
            temp_h = 0
            index = 0
            
            # O(n)
            for i in range(len(piles)):
                if piles[i] <= k:
                    temp_h += 1
                else:
                    if (piles[i] % k):
                        temp_h += (piles[i] // k) + 1
                    else:
                        temp_h += (piles[i] // k)

            return temp_h
        
    #finding the max and the total sum
    def _find_max_totalSum(self, piles) -> (int, int):
        totalSum = 0
        maxi = 0
        for i in range(len(piles)):
            if piles[i] > piles[maxi]:
                maxi = i
            totalSum += piles[i]
        return (maxi, totalSum)
    
    #Actual Binary Search Logic
    def _bs(self, l, r, piles, h, totalS, maxi):

        if l > r:
            #print("l: ", l, "\tr: ", r)
            return l

        mid =  l + ((r-l) // 2)
        attempts = self._correctK(piles, h, mid, totalS, maxi)
        print("considering: ", mid, "\tattempts are: ", attempts)

        if (attempts > h):
            print("\tattempts was wrong: ", attempts, "\tnew l: ", mid+1, "\tnew r: ", r)
            return self._bs(mid + 1, r, piles, h, totalS, maxi)
        elif (attempts <= h):
            print("\tattempts was: ", attempts, "\tnew l: ", l, "\tnew r: ", mid - 1)
            return self._bs(l, mid-1, piles, h, totalS, maxi)

    #main function
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxi, ts =  self._find_max_totalSum(piles)
        return self._bs(1, piles[maxi], piles, h, ts, maxi)
