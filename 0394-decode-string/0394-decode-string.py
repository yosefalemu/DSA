class Solution:
    def decodeString(self, s: str) -> str:
        result = []
        for ch in s:
            if ch != "]":
                result.append(ch)
            else:
                curr_sub_string = ""
                while result and result[-1] !="[":
                    curr_sub_string = result.pop() + curr_sub_string
                # Remove the [ from the stack
                result.pop()
                curr_multiplier = ""
                while result and result[-1].isdigit():
                    curr_multiplier = result.pop() + curr_multiplier
                result.append(curr_sub_string*int(curr_multiplier))
        return "".join(result)





    
        