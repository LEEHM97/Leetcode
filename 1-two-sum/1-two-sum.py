class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            tmp = target - nums[i]

            if tmp in nums:
                if i == nums.index(tmp):
                    continue
                return [i, nums.index(tmp)]