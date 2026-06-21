class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        nei = [[-1,0], [0,1], [0,-1], [1,0]]
        m, n = len(image), len(image[0])
        
        def _dfs(x,y):
            seen = set()
            s = []
            s.append((x,y))
            original_color = image[sr][sc]
            while s:
                dx, dy = s.pop()
                image[dx][dy] = color
                for a,b in nei:
                    x1, y1 = dx + a, dy + b
                    if (x1 >= 0 and x1 < m) and (y1 >= 0 and y1 < n) and image[x1][y1] == original_color and ((x1,y1) not in seen):
                        s.append((x1,y1))
                        seen.add((x1,y1))
                        image[x1][y1] = color
                    
                seen.add((dx,dy))
                

        _dfs(sr,sc)

        return image