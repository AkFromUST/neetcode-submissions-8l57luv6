class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        forward, backward = {}, {}

        for num in nums:
            forward[num] = set()
            backward[num] = set()

        #propagation
        for num in nums:
            if ((num+1) in forward):
                forward[num] = num+1
                backward[num+1] = num
    
        seen = set()
        all_len = []
        def DFS(node):
            stack = []
            stack.append(node)
            nodes = 1
            while stack:
                v = stack.pop()
                if forward[v]!= set() and forward[v] not in seen:
                    stack.append(forward[v])
                if backward[v] != set() and backward[v] not in seen:
                    stack.append(backward[v])
                seen.add(v)
                nodes +=1
            all_len.append(nodes)

        for num in nums:
            if num not in seen:
                DFS(num)
        
        return max(all_len) - 1