//6. Zigzag Conversion
class Solution {
public:
    string convert(string s, int numRows) {
        string kq;
        int middle;
        if(s.size()<numRows ||numRows==1){
            return s;
        }
        for(int row=0;row<numRows;row++){
            int i=row;
            int down=2*(numRows - 1 - row);
            int up=2*row;
            bool usedown=true;
            while (i<s.size()){
                kq.push_back(s[i]);
                if(row==0 || row==numRows-1){
                    i=i+2*(numRows-1);
                } else{
                    if(usedown==true && down>0){
                        i=i+down;
                    } else if(usedown==false && up >0){
                        i=i+up;
                    }
                    usedown=!usedown;
                }
            }    
        }
        return kq;
    }
};