class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        options = 0
        for i in range(len(flowerbed)):
            if i == 0 and flowerbed[i] == 0 and (i + 1 >= len(flowerbed) or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                options += 1
                continue
            if i - 1 > 0 and i < len(flowerbed) - 1:
                if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    options += 1
                    continue
            if i == len(flowerbed) - 1:
                if flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    options += 1
        return options >= n
             


        