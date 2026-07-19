class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        count = 0
        for num in nums:
            if num == 0:
                count += 1
                continue
            prod *= num
        res = []
        for num in nums:
            if num == 0 and count == 1:
                res.append(prod)
                continue
            elif count > 0:
                res.append(0)
                continue
            res.append(prod//num)
        return res
