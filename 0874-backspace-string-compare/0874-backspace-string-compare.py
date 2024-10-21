class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_string(string):
            k = 0
            for i in range(len(string)):
                if string[i] != "#":
                    string[k] = string[i]
                    k += 1
                else:
                    k = max(k - 1, 0)
            return k
        s , t = list(s), list(t)
        k = process_string(s)
        p = process_string(t)
        if k != p:
            return False
        for i in range(k):
            if s[i] != t[i]:
                return False
        return True

        