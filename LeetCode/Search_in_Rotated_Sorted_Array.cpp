class Solution {
public:
    int search(vector<int>& nums, int target) {
        int start = 0, endof = nums.size()-1;
        
        while (start <= endof) {
            int middle = (start + endof) / 2;
            int number = nums[middle];
            
            if (number == target) {
                return middle; 
                
            } else if (number < nums[endof]) {
                if (number < target && target <= nums[endof])
                    start = middle +1;
                else
                    endof = middle -1;
            } else {
                if(nums[start] <= target && target < number)
                    endof = middle -1;
                else
                    start = middle +1;
            }
        }
        return -1;
    }
};
