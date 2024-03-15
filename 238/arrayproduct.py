# You must write an algorithm that runs in O(n) time and without using the division operation.
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        output = [1]

        prod = 1
        for i in range(1, len(nums)):
            prod *= nums[i - 1]
            output.append(prod)

        prod = 1
        for i in range(len(nums) - 2, -1, -1):
            prod *= nums[i + 1]
            output[i] *= prod

        return output

# This solution has optimizations for zero products, but it performs just as well or worse than the simpler version above
# class Solution:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
#         output = [1]
#         prod = 1
#         for i in range(1, len(nums)):
#             prod *= nums[i - 1]
#             if prod != 0:
#                 output.append(prod)
#             else:
#                 if nums.count(0) > 1:
#                     return [0] * len(nums)
#                 else:
#                     output.extend([0] * (len(nums) - i))
#                     break
#
#         prod = 1
#         for i in range(len(nums) - 1, -1, -1):
#             output[i] *= prod
#             prod *= nums[i]
#             if prod == 0:
#                 return [0] * i + output[i:]
#        return output

sol = Solution()
res = sol.productExceptSelf([-1,1,0,-3,3, 0])
print(res)
