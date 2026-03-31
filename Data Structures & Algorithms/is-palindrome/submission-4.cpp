class Solution {
public:
    
    bool _isAlpha(char c) {
        return (c >= 'A' && c <= 'Z' ||
                c >= 'a' && c <= 'z' ||
                c >= '0' && c <= '9');
    }

    bool isPalindrome(string s) {
        int l = 0;
        int r = s.size() - 1;

        while (l < r) {

            while (l < r && _isAlpha(s[l]) != true) { l += 1; }
            while (r > l && _isAlpha(s[r]) != true) { r -= 1; }  

            if (tolower(s[l]) != tolower(s[r])) { return false; }
            l += 1;
            r -= 1;
        }
    
        return true;
    }
};
