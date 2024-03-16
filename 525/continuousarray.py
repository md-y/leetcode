class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        sums = {}
        total = 0
        largest = 0
        for i in range(len(nums)):
            total += 1 if nums[i] == 1 else -1
            if total == 0:
                largest = i + 1
            elif total not in sums:
                sums[total] = i
            elif (diff := i - sums[total]) > largest:
                largest = diff
        return largest

sol = Solution()
res = sol.findMaxLength([0] * 1000 + [1] * 1000)
print(res)
