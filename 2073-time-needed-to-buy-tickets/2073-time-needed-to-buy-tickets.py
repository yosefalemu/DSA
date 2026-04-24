class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        target = tickets[k]
        ans = 0
        for i in range(len(tickets)):
            if i == k:
                ans += target
            elif i < k:
                ans += min(target, tickets[i])
            else:
                if tickets[i] < target:
                    ans += min(target, tickets[i])
                else:
                    ans += (min(target, tickets[i]) - 1)
        return ans
        