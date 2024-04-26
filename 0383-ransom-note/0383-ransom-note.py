class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dicRansomNote = {}
        dicMagazine = {}
        for item in ransomNote:
            if item in dicRansomNote:
                dicRansomNote[item] += 1
            else:
                dicRansomNote[item] = 1
        for item in magazine:
            if item in dicMagazine:
                dicMagazine[item] += 1
            else:
                dicMagazine[item] = 1
        for item in dicRansomNote:
            if item not in dicMagazine.keys():
                return False
            else:
                if dicRansomNote[item] > dicMagazine[item]:
                    return False
        return True
            
        