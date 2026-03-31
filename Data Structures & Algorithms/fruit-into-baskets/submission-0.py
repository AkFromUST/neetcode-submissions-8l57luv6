class Solution:
    def _remove_fruit(self, state):        
        remove_fruit_value = min(state.values())
        remove_fruit_name = ""
        for k,v in state.items():
            if v == remove_fruit_value:
                remove_fruit_name = k

        state.pop(remove_fruit_name)
        return remove_fruit_value+1
    
    def totalFruit(self, fruits: List[int]) -> int:
        
        l, maxfruits, currfruits = 0, 0, 0
        state = {}
        n = len(fruits)

        for r in range(n):
            #check if we can add this to the state
            if fruits[r] not in state:
                if currfruits < 2:
                    state[fruits[r]] = r
                    currfruits += 1
                else:
                    #now must remove one.
                    l = self._remove_fruit(state)
                    state[fruits[r]] = r

            #upate the loc of fruits[r]
            state[fruits[r]] = r

            #check the len
            maxfruits = max(maxfruits, r-l+1)
        
        return maxfruits