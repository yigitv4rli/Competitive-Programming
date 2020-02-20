class Solution {
public:
    int lengthOfLastWord(string s) {
        int length, index;
        index = s.size() - 1;
        length = 0;
        
        while (isspace(s[index])) {
            index --;
        }
        while (isalnum(s[index])) {
            length++;
            index--;
        }
    return length;
    }
};
