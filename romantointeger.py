class Solution {
public:

    int romanToInt(string s) {

        unordered_map <char, int> roman = {
            {'I',1},
            {'V',5},
            {'X',10},
            {'L',50},
            {'C',100},
            {'D',500},
            {'M',1000}
        };

        int len= s.length();
        int sum = 0;

        for(int i = 0;i<len-1;i++){
                if(roman[s[i+1]] > roman[s[i]])
                    sum-=roman[s[i]];
                else
                sum+=roman[s[i]];
            }
        sum+=roman[s[len-1]];
        return sum;
        }
    };
