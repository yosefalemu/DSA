class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        dict1 = {
            1:["q","w","e","r","t","y","u","i","o","p"],
            2:["a","s","d","f","g","h","j","k","l"],
            3:["z","x","c","v","b","n","m"]            
        }
        ans = []
        for item in words:
            ref = 0
            if item[0].lower() in dict1[1]:
                ref = 1
            elif item[0].lower() in dict1[2]:
                ref = 2
            elif item[0].lower() in dict1[3]:
                ref = 3
            else:
                pass
            flag = True
            for char in item:
                if char.lower() not in dict1[ref]:
                    flag = False
                    break
            if flag:
                ans.append(item)
        return ans
        