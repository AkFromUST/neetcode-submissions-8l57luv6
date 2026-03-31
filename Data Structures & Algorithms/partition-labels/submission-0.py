class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        hashmap = {}

        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = [i]
            else:
                hashmap[s[i]].append(i)


        res = []
        i_max_sofar = hashmap[s[0]][-1]
        size = 0
        for i in range(len(s)):
            index = hashmap[s[i]][-1]
            size += 1

            i_max_sofar = max(i_max_sofar, index)

            if (i == i_max_sofar):
                res.append(size)
                size = 0

        return res