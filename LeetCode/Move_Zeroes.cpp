class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        for (int current_index = 0, last_zero_index = 0; current_index < nums.size(); current_index++) {
            if(nums[current_index] != 0) {
               swap(nums[last_zero_index++],nums[current_index]);
            }
        }
    }
};
