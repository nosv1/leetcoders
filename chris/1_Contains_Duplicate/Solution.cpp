class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        if (nums.empty()) return false;

        unordered_map<int, int> unique_nums;
        for (int i = 0; i < nums.size(); i++) {
            if (unique_nums.find(nums[i]) != unique_nums.end()) {
                return true;
            }
            unique_nums[nums[i]] = 1;
        }
        return false;
    }        
};