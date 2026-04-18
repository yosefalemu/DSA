class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for asteroid in asteroids:
            while result and asteroid < 0 and result[-1] > 0:
                if result[-1] == -asteroid:
                    result.pop()
                    break
                elif result[-1] < -asteroid:
                    result.pop()
                    continue
                else:
                    break          
            else:
                result.append(asteroid)
        return result

        