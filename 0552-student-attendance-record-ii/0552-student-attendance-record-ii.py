class Solution:
    def tabulation(self, N):
        MOD = 1000000007
        prev_dp = [[1]*(3) for _ in range(2)]
        curr_dp = [[1]*(3) for _ in range(2)]
        for n in range(1, N+1):
            for total_absent in range(1, -1, -1):
                for consecutive_late in range(2, -1, -1):
                    present = prev_dp[total_absent][0]
                    absent, late = 0, 0
                    if total_absent<1:
                        absent = prev_dp[total_absent+1][0]
                    if consecutive_late<2:
                        late = prev_dp[total_absent][consecutive_late+1]
                    curr_dp[total_absent][consecutive_late] = (present+absent+late)%MOD
            curr_dp, prev_dp = prev_dp, curr_dp
        return prev_dp[0][0]

    def checkRecord(self, n: int) -> int:
        return self.tabulation(n)