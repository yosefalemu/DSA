class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)

        # Create a Set of words from the array so that the
        # lookup cost in the Set becomes O(1)
        word_set = set(wordDict)

        # Initialize the lookup table
        dp = [[] for _ in range(n + 1)]

        # Set the first element to an empty string
        dp[0] = [""]

        for i in range(1, n + 1):
            temp = []
            for j in range(i):
                suffix = s[j:i]
                # Checking if the substring from j to i is
                # present in the wordSet
                if suffix in word_set:
                    # Retrieve the valid sentences from the
                    # previously computed subproblem
                    for substring in dp[j]:
                        # Merge the suffix with the already
                        # calculated results, excluding the leading
                        # space
                        temp.append(f"{substring}{' ' if substring else ''}{suffix}")
            dp[i] = temp

        # Return the last element of dp array It contains all
        # the sentences formed from the complete string s.
        return dp[n]