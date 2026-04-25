class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = {}
        store = deque()

        for i, ch in enumerate(s):
            counts[ch] = counts.get(ch, 0) + 1
            store.append((ch, i))
            while store and counts[store[0][0]] > 1:
                store.popleft()
        return store[0][1] if store else -1
        