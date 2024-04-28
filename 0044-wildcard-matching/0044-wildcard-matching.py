class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache={}
        def dfs(i, j):

            if (i,j) in cache:
                return cache[i,j]

            if i >= len(s) and j >= len(p):
                cache[(i,j)]=True

                return cache[(i,j)]
            if j >= len(p):
                cache[(i,j)]=False
                return cache[i,j]
            
            match = i < len(s) and (s[i] == p[j] or p[j] == '?' or p[j] == '*')
            
            if p[j] == '*':
                # Match zero characters or match one or more characters
                cache[(i,j)]= dfs(i, j + 1) or (match and dfs(i + 1, j))
                return cache[(i,j)]
            
            if match:
                cache[(i,j)]=dfs(i + 1, j + 1)
                return cache[(i,j)]
            
            cache[(i,j)]=False
        
        return dfs(0, 0)