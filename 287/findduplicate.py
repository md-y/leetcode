class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # Can't modify nums and extra space should be O(1).
        # Length of nums is <= 10^5, so it is O(1) space (technically)
        found_nums = [0] * len(nums)
        for i in nums:
            if found_nums[i]:
                return i
            else:
                found_nums[i] = 1
        return -1

sol = Solution()
res = sol.findDuplicate([18,13,14,17,9,19,7,17,4,6,17,5,11,10,2,15,8,12,16,17])
print(res)
