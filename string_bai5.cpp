//5. Longest Palindromic Substring
class Solution {
public:
    string longestPalindrome(string s) {
        bool check;
        string kq="";
        string temp;
        int l, r;
        if(s.size()==0){
            return "";
        }
        if(s.size()==1){
            return s;
        }
        if (s.size() == 2) {
            if (s[0] == s[1]) return s;
            else return s.substr(0,1);
        }
        for(int i=0;i<s.size()-1;i++){
            for(int j=i+1;j<s.size();j++){
                l=i;
                r=j;
                check=true;
                while(l<r){
                    if(s[l]==s[r]){

                        l++;
                        r--;
                        check=true;
                    } else{
                        check=false;
                        break;
                    }
                }
                if (check== true){
                    temp=s.substr(i,j-i+1);
                    if(temp.size()>kq.size()){
                        kq=temp;
                        temp.clear();
                    } else{
                        temp.clear();
                    }
                }
            }
        }
        return kq;
    }
};