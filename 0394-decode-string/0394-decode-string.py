class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                current_substring = ""
                while stack and stack[-1] != "[":
                    current_substring = stack.pop() + current_substring
                stack.pop()
                current_multiplier = ""
                while stack and stack[-1].isdigit():
                    current_multiplier = stack.pop() + current_multiplier
                stack.append(current_substring * int(current_multiplier))
        return "".join(stack)



    
        