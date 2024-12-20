class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0]*len(code)
        if k > 0:
            ans = []
            for i in range(len(code)):
                if i + k < len(code):
                    ans.append(sum(code[i+1:i+k+1]))
                else:
                    remain = i + k - len(code)
                    if i < len(code) - 1:
                        ans.append(sum(code[:remain+1]) + sum(code[i+1:]))
                    else:
                        ans.append(sum(code[:remain+1]))
            return ans
        if k < 0:
            ans = []
            for i in range(len(code)):
                if i - abs(k) < 0:
                    remain = len(code) - abs(k) + i
                    ans.append(sum(code[remain:]) + sum(code[:i]))
                else:
                    ans.append(sum(code[i-abs(k):i]))
            return ans
                



        
        