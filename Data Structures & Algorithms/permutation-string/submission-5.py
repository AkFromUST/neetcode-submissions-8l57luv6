class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # create a set that stores the chars of s1.

        # char = set()

        # for c in s1:
        #     char.add(c)

        # # now iterate over the s2 in a fixed window. If any of the  1
        # i = 0
        # while i < len(s2):
        #     c = s2[i]
        #     if c in char:
                
        #         #making a new set
        #         temp = set()
        #         for k in s1:
        #             temp.add(k)
        #         j = i
        #         print("Entered from: ", c, " with temp: ", temp)
        #         if (j + len(s1)) >= len(s2):
        #             return False
        #         else:
        #             for j in range(i, i + len(s1)):
        #                 print("\t\tchecking:\t", s2[j])
        #                 if s2[j] in temp:
        #                     temp.remove(s2[j])
        #                 i = j

        #             # If temp is empty. Then we found the permutation else this is not the one.
        #             if len(temp) == 0:
        #                 return True
        #     i += 1
        # return False

        """
            Sliding window. Every window has its own set (chars of s1). We check of every window what all chars are not present.
            If false, restore the window accordingly, otherwise keep going until we find the permutation
        """

        if (len(s2)) < len(s1):
            return False

        l = 0

        chars = {}

        # Making freq hashmap
        for c in s1:
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1

        for r in range(len(s2)):

            if s2[r] in chars and chars[s2[r]] != 0:
                l = r
                
                while (r < len(s2)) and (s2[r] in chars) and (chars[s2[r]] != 0):
                    chars[s2[r]] -= 1
                    r += 1
                
                # this means that either we are done or we are not
                true = True
                for key, val in chars.items():
                    if val != 0:
                        true = False
                
                if true:
                    return True
                else:
                    for c in s2[l:r]:
                        chars[c] += 1
                    l = r
            print("This is not the one: ", chars)

        return False            











            







        