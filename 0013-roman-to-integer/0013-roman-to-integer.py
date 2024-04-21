class Solution:
    def romanToInt(self, s: str) -> int:
        romToint = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        subtractionMayOcuured = ["I","X","C"]
        index = 0
        ans = 0
        while index < len(s):
            if index + 1 < len(s) and s[index] in subtractionMayOcuured:
                if s[index] == "I" and s[index + 1] == "V":
                    ans += romToint["V"] - romToint["I"]
                    index += 2
                    continue
                elif s[index] == "I" and s[index + 1] == "X":
                    ans += romToint["X"] - romToint["I"]
                    index += 2
                    continue
                elif s[index] == "X" and s[index + 1] == "L":
                    ans += romToint["L"] - romToint["X"]
                    index += 2
                    continue
                elif s[index] == "X" and s[index + 1] == "C":
                    ans += romToint["C"] - romToint["X"]
                    index += 2
                    continue
                elif s[index] == "C" and s[index + 1] == "D":
                    ans += romToint["D"] - romToint["C"]
                    index += 2
                    continue
                elif s[index] == "C" and s[index + 1] == "M":
                    ans += romToint["M"] - romToint["C"]
                    index += 2
                    continue
                else:
                    ans += romToint[s[index]]
                    index += 1
            else:
                ans += romToint[s[index]]
                index += 1
        return ans
                
                

        