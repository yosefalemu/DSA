class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        if set(word1) != set(word2):
            return False

        char_dict1 = dict()
        char_dict2 = dict()
        
        for char in word1:
            char_dict1[char] = char_dict1.get(char, 0) + 1
       
        for char in word2:
            char_dict2[char] = char_dict2.get(char, 0) + 1

        return sorted(char_dict1.values()) == sorted(char_dict2.values())
        