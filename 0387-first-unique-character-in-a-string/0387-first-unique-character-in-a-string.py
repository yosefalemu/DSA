class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        queue = deque()

        for i, char in enumerate(s):
            queue.append((char, i))
            while queue and counts[queue[0][0]] > 1:
                queue.popleft()
        return queue[0][1] if queue else -1
        