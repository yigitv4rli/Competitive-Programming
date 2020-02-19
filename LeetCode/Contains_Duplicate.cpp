class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::map<int,int> hash_map;
        sort(nums.begin(),nums.end());
        
        for (int i = 0; i < nums.size(); i++) {
            if(hash_map.find(nums[i]) != hash_map.end()) {
                return true;
            } else { 
                hash_map.insert(std::pair<int, int>(nums[i], 1));
            }
        } return false;
    }
};
