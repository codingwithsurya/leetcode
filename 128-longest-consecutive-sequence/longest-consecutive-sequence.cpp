class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        set<int> numSet(nums.begin(), nums.end()); 
        int streak = 0, maxStreak = 0;

        for (int n : numSet) { 
            if (!numSet.contains(n - 1)) { 
                int current = n;
                streak = 1;

                while (numSet.contains(current + 1)) { 
                    streak++;
                    current++;
                    
                }
                maxStreak = max(maxStreak, streak);
            }
        }
        return maxStreak;
        
    }
};