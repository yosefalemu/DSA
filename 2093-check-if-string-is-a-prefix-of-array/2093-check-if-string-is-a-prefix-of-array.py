class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        concateString = ""
        for c in words:
            concateString += c
            if concateString == s:
                return True
        return False
        