class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            t = numbers[l] + numbers[r]
            if t < target:
                l += 1
            elif t > target:
                r -= 1
            elif t == target:
                return [l + 1, r + 1]

sol = Solution()
res = sol.twoSum([0,0,3,4], 0)
print(res)
