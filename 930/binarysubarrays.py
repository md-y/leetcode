class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        count = 0
        l = len(nums)
        j = 0
        s = 0 # Sum between j and i
        lz = 0 # Leading zeroes before i
        for i in range(l):
            s += nums[i]

            # Can't do anything until a valid subarray is found
            if s < goal:
                continue

            # If the sum is too large, attempt to move j to lower it
            if s > goal and j < i:
                s -= nums[j]
                j += 1
                lz = 0

            # Count the number of leading zeros
            while j < i and nums[j] == 0:
                lz += 1
                j += 1

            # If a valid subarray, and it and the zero-prefixed versions
            if s == goal:
                count += lz + 1

        return count

sol = Solution()
res = sol.numSubarraysWithSum([1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0], 0)
print(res)

