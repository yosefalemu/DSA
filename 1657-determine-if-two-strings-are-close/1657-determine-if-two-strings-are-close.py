class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Step 1: same length
        if len(word1) != len(word2):
            return False
        
        count1 = Counter(word1)
        count2 = Counter(word2)
        
        # Step 2: same set of characters
        if count1.keys() != count2.keys():
            return False
        
        # Step 3: same frequency distribution
        return Counter(count1.values()) == Counter(count2.values())