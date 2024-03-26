class Solution {
    public int firstMissingPositive(int[] nums) {
        /**
        You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
         */

        // Smallest unseen pos value will be <= len, so len+1 is the default value
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] <= 0) nums[i] = nums.length + 1;
        }

        // Mark every seen index as negative
        for (int i = 0; i < nums.length; i++) {
            int j = Math.abs(nums[i]) - 1;
            if (j >= 0 && j < nums.length && nums[j] > 0) {
                nums[j] = -nums[j];
            }
        }

        // Find smallest unseen index
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) return i + 1;
        }

        return nums.length + 1;
    }
}

