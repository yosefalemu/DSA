class Solution:
    def isValid(self, s: str) -> bool:
        parenthesesRelation = {
            ")" : "(",
            "]" : "[",
            "}" : "{"           
        }
        stack = []
        for item in s:
            if stack and  item in parenthesesRelation.keys():
                if parenthesesRelation[item] != stack.pop():
                    return False
            else:
                stack.append(item)
        return not stack
                
                
            
            