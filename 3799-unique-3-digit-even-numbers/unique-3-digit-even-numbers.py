class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        available = [0] * 10
        for d in digits:
            available[d] += 1
        count = 0
        for num in range(100, 1000, 2):
            h = num // 100
            t = (num // 10) % 10
            u = num % 10
            available[h] -= 1
            available[t] -= 1
            available[u] -= 1
            if available[h] >= 0 and available[t] >= 0 and available[u] >= 0:
                count += 1
            available[h] += 1
            available[t] += 1
            available[u] += 1
        return count
