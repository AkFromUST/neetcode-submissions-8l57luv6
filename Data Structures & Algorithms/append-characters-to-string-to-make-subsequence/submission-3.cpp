class Solution {
public:
    int appendCharacters(string s, string t) {
        int sn= s.size(); int tn= t.size();

        int l = 0; int r = 0;

        while (l < sn && r < tn) {
            if (s[l] == t[r]) { r++;}
            l++;
        }

        return tn-r;
        
    }
};