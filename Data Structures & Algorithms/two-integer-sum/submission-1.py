class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for i, n in enumerate(nums):
            k = target - n

            if k in res:
                return [res[k], i]
            else:
                res[n] = i

        return []