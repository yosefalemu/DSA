class Solution:
    def isValid(self, s: str) -> bool:
        validParen = {
            "]" : "[",
            "}" : "{",
            ")" : "("
        }
        container = []
        for c in s:
            if c not in validParen:
                container.append(c)
            else:
                corresponding_open = container.pop() if container else None
                if validParen[c] != corresponding_open:
                    return False
        return len(container) == 0
        