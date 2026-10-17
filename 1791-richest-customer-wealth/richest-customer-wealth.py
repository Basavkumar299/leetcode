class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:       
        maximum=0
        for amount in accounts :
            if sum(amount)>maximum:
                maximum=sum(amount)
        return maximum