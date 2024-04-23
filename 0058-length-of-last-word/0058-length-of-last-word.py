class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ansList = []
        tempStr = ""
        for eachItem in s:
            if eachItem != " ":
                tempStr += eachItem
            else:
                if tempStr:
                    ansList.append(tempStr)
                    tempStr = ""
        if tempStr:
            ansList.append(tempStr)
        return len(ansList[-1])
                    
                    
                    
                
            
        