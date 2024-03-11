class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        // Index variable for nums2
        int j = 0; 

        // Go through every m value (and any new merged values), 
        // and insert the value at j if it is less than the value at i.
        // Stop the loop if every n value has been compared.
        for (int i = 0; i < m + j && j < n; i++) {
            if (nums2[j] <= nums1[i]) {
                nums1.insert(nums1.begin() + i, nums2[j]);
                nums1.pop_back();
                j++;
            }
        }

        // Simply add all values from nums2 once ervery m value has been compared
        for (; j < n; j++) {
            nums1[m + j] = nums2[j];
        }
    }
};
