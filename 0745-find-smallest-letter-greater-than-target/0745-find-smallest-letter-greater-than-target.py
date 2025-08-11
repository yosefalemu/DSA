class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = letters[0]
        for c in letters:
            if c > target:
                ans = c
                break
        return ans
        