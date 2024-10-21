class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            if ans[left].isalpha() and ans[right].isalpha():
                ans[left],ans[right] = ans[right], ans[left]
                left += 1
                right -= 1
            elif not ans[left].isalpha():
                left += 1
            else:
                right -= 1
        return "".join(ans)

        