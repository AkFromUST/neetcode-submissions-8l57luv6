class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #lets not use a hashset. But instead resort to a limimt var and a hashmap
        limit = 0
        
        #key: ch, val: last_known_pos
        ch_hashmap = {}
        longest = 0
        for i, ch in enumerate(s):
            ch = ord(ch)
            if ch not in ch_hashmap:
                ch_hashmap[ch] = i

                if longest < (i - limit):
                    print("True")
                    longest = i - limit

            else:
                #this is a true repeating char. If the last known was outside of limit, then we dont care. Just update the last pos
                if ch_hashmap[ch] >= limit:
                    #check if the longest or not
                    if longest < (i - limit):
                        longest = (i - limit)
                    
                    #new limit to the next pos of the prev known loc of this repeating char
                    limit = ch_hashmap[ch] + 1

                ch_hashmap[ch] = i

        #if the longest is including the right most end. then we need to have another check
        if longest < (len(s) - limit):
            longest = len(s) - limit
        return longest