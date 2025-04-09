class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        for hour in range(12):
            for minute in range(60):
                if bin(hour).count("1") + bin(minute).count("1") == turnedOn:
                    tempHour = str(hour)
                    tempMinute = str(minute) if minute >= 10 else "0" + str(minute)
                    currValue = tempHour + ":" + tempMinute
                    ans.append(currValue)
        return ans
        