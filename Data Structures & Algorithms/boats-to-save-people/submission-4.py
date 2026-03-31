class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        print(people)

        l,r = 0, len(people) - 1
        local_boat, boat_count = 0 , 0
        while l < r:
            local_boat += people[l] + people[r]
            if local_boat > limit:
                local_boat = 0
                boat_count += 1
                r -= 1
                continue
            if local_boat <= limit:
                l += 1
            
        return boat_count + 1