class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left,right + 1):
            count = 0
            for c in ranges:
                begin, end = c
                if i in range(begin, end + 1):
                    break
                elif count == len(ranges) - 1 and i not in range(begin, end + 1):
                    return False
                count += 1
        return True
        