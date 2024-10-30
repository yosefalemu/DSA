class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        index = 1
        listOfSentence = sentence.split(" ")
        n = len(searchWord)
        for c in listOfSentence:
            if c[:n] == searchWord:
                return index
            index += 1
        return -1
        