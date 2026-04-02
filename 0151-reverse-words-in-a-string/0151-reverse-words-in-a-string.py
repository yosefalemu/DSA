class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split()
        ans = []
        for i in range(len(temp) - 1, -1, -1):
            ans.append(temp[i])
            if i != 0:
                ans.append(" ")
        return "".join(ans)



        