class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // Iterate through the vector backwards to avoid messing up the ptr when
        // an element is removed.
        for (vector<int>::iterator ptr = nums.end() - 1; ptr > nums.begin(); ptr--) {
            if (*ptr == *(ptr - 1)) nums.erase(ptr);
        }
        return nums.size();
    }
};
