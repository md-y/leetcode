class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        cache = {}
        for i in range(len(nums)):
            t = target - nums[i]
            if t in cache:
                return [i, cache[t]]
            cache[nums[i]] = i

sol = Solution()
res = sol.twoSum([3,2,4], 6)
print(res)


