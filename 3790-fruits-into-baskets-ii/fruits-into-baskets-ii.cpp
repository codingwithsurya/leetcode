class Solution {
public:
    int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
        int n = fruits.size() ;
        vector<bool> basketsUsed(n,false);

        int unplacedCount = 0;

        for (int i =0; i < n; ++i) { 
            bool placed = false;

            for (int j = 0; j < baskets.size(); j++) { 
                // if it hasnt been used and basket can fit the fruit    
                if (!basketsUsed[j] && baskets[j] >= fruits[i]) {
                    placed = true;
                    basketsUsed[j] = true;
                    break;
                }
            }

            if (!placed) { 
                unplacedCount++;
            }

        }

        return unplacedCount;

    }
};