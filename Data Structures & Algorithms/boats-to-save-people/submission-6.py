class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        l,r = 0, len(people) - 1
        local_boat, boat_count = 0 , 0
        while l <= r:
            #if the limit is the same
            local_boat = people[l] + people[r]

            if local_boat > limit:
                boat_count += 1
                r -= 1
                continue 

            l += 1
            r -= 1
            boat_count += 1

        return boat_count