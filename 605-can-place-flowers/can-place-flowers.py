class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True
        planted = 0
        total_plots = len(flowerbed)
        for index in range(total_plots):
            if flowerbed[index] == 1:
                continue
            left_clear = (index == 0) or (flowerbed[index - 1] == 0)
            right_clear = (index == total_plots - 1) or (flowerbed[index + 1] == 0)
            if left_clear and right_clear:
                flowerbed[index] = 1
                planted += 1
                if planted == n:
                    return True
        return False
