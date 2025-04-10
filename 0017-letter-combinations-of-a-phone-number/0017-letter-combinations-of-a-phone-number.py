class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_to_chars = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        def helper(idx, temp):
            if idx == len(digits):
                ans.append(temp)
                return
            for char in digit_to_chars[digits[idx]]:
                helper(idx + 1, temp + char)
        ans = []
        helper(0,"")
        return ans
        