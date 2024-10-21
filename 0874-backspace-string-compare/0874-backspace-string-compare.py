class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sStack = []
        tStack = []
        for c in s:
            if c != "#":
                sStack.append(c)
            else:
                if sStack:
                    sStack.pop()
        for c in t:
            if c != "#":
                tStack.append(c)
            else:
                if tStack:
                    tStack.pop()
        return sStack == tStack
        