class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        new_array = [0]
        for c in flowerbed:
            new_array.append(c)
        new_array.append(0)
        for i in range(1,len(new_array) - 1):
            if new_array[i] == 0 and new_array[i - 1] == 0 and new_array[i + 1] == 0:
                new_array[i] = 1
                n -= 1
        if n > 0:
            return False
        else:
            return True
            
        