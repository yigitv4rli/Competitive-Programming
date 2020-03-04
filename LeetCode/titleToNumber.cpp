class Solution {
public:
    int titleToNumber(string s) {
        int column = 0;
        
        if (s.size() == 1)
            return s[0]-64;
        
       for(int i = s.length(); i > 0; i--) {
            column += (s[i - 1] - 'A' + 1) * pow(26, (s.length() - i));
           
        } return column;
    }
};
