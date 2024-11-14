class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0]*len(code)
        elif k > 0:
            tempArr = code + code[:k]
            ans = []
            for i in range(len(code)):
                ans.append(sum(tempArr[i + 1: i + k + 1]))
            return ans
        else:
            tempArr = code[k:] + code
            ans = []
            for i in range(len(code)):
                ans.append(sum(tempArr[i:i + abs(k)]))
            return ans
        
        