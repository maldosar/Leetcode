class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return (lambda d: next(
            (k, d[target - i])
            for k, i in enumerate(nums)
			if target - i in d or d.update({i: k})
        ))({})
