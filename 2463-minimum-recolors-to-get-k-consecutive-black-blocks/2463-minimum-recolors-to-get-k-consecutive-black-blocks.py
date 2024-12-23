class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        numOfIteration = len(blocks) - k + 1
        ans = inf
        for i in range(numOfIteration):
            temp = blocks[i:k+i]
            recolor = 0
            for c in temp:
                if c == "W":
                    recolor += 1
            ans = min(ans,recolor)
        return ans
            
        