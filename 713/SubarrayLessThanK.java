class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        if (k <= 0) return 0;

        int count = 0;
        int product = 1;
        for (int i = 0, j = 0; i < nums.length; i++) {
            // Reset the subarray if this element is way too big
            if (nums[i] >= k) {
                j = i + 1;
                continue;
            }

            product *= nums[i];

            // Shrink subarray until under k or 0-width
            while (product >= k && j <= i) {
                product /= nums[j];
                j++;        
            }
            if (j > i) {
                j = i;
                product = nums[i];
            }

            // Counts this new element and other permutations
            count += i - j + 1;
        }
        return count;
    }
}
