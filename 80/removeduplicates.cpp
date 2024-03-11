class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        for (vector<int>::iterator ptr = nums.end() - 2; ptr > nums.begin(); ptr--) {
            if (*(ptr - 1) == *ptr && *(ptr + 1) == *ptr) nums.erase(ptr);
        }
        return nums.size();
    }
};
