class Solution:
    def compress(self, chars: List[str]) -> int:
        slow_pt = fast_pt = 0
        while fast_pt < len(chars):
            char = chars[fast_pt]
            count = 0
            while fast_pt < len(chars) and chars[fast_pt] == char:
                count += 1
                fast_pt += 1
            chars[slow_pt] = char
            slow_pt += 1
            if count > 1:
                for digit in str(count):
                    chars[slow_pt] = digit
                    slow_pt += 1
        return slow_pt



        