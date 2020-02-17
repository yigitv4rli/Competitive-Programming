
class Solution {
public:
    std::vector<string> letterCombinations(string digits) {
        std::vector<std::string> combs = {};
        std::vector<std::vector<char>> phoneTable = {
            {' ', ' ', ' '},
            {' ', ' ', ' '},
            {'a', 'b', 'c'},
            {'d', 'e', 'f'},
            {'g', 'h', 'i'},
            {'j', 'k', 'l'},
            {'m', 'n', 'o'},
            {'p', 'q', 'r', 's'},
            {'t', 'u', 'v'},
            {'w', 'x', 'y', 'z'},
        };
        int index = 0;
        int c = 0;
        while(index != digits.size()) {
            if(c == 100)
                break;
            std::vector<char> currentDigitEntry = phoneTable[digits[index] - 48];
            if(combs.size() == 0) {
                for(auto k : currentDigitEntry) {
                    std::string s(1, k);
                    combs.push_back(s);
                }
                index++;
                continue;
            }
            for(int i = 0 ; i < currentDigitEntry.size() ; i++) {
                int size = combs.size();
                for(int j = 0 ; j < size ; j++) {
                    
                    combs.push_back(combs[j] + currentDigitEntry[i]);
                }
            }
            index++;
        }
        for(int i = combs.size() - 1; i >= 0 ; i--) {
            if(combs[i].size() != digits.size()) {
                combs.erase(combs.begin() + i);
            }
        }
        return combs;
    }
};
