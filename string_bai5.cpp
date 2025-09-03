//5. Longest Palindromic Substring
class Solution {
public:
string expand(string &s, int l, int r){
            while(l>=0 && r<s.size() && s[l]==s[r]){
                l--;
                r++;
            }
            return s.substr(l+1,r - l -1);
        }
    string longestPalindrome(string s) {
        string kq="";
        for(int i=0;i<s.size();i++){
            string sub1=  expand(s,i,i);
            if(sub1.size()>kq.size()){
                kq=sub1;
            }
            string sub2=expand(s,i,i+1);
            if(sub2.size()>kq.size()){
                kq=sub2;
            }
        }
        return kq;
    }
};