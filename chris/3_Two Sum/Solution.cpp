class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int, int> num_map;
        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            int complement = target - num;
            if (num_map.find(complement) != num_map.end()) {
                return {num_map[complement], i};
            } else {
                num_map[num] = i;
            }
        }

        return {};
    }
};