class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        prev = []
        for i in range(numRows):
            if i == 0:
                prev = [1]
                ans.append(prev)
            else:
                curr = [1]
                j = 1
                while j < i:
                    curr.append(prev[j - 1] + prev[j])
                    j += 1
                curr.append(1)
                ans.append(curr)
                prev = curr
        return ans
                
            
        