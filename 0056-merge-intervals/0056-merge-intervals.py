from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])    
        slowpt = 0
        fastpt = 1
        ans = []      
        while fastpt < len(intervals):
            if intervals[slowpt][1] >= intervals[fastpt][0]:
                intervals[slowpt][1] = max(intervals[slowpt][1], intervals[fastpt][1])
            else:
                ans.append(intervals[slowpt])
                slowpt = fastpt
            fastpt += 1
        ans.append(intervals[slowpt])      
        return ans
