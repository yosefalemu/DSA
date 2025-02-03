class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(numRows - 1):
            prev = ans[-1]
            temp = [1]
            if len(prev) >= 2:
                left = 0
                right = 1
                while right < len(prev):
                    aboveSum = prev[left] + prev[right]
                    temp.append(aboveSum)
                    left += 1
                    right += 1
            temp.append(1)
            ans.append(temp)
        return ans

        
                
            
        