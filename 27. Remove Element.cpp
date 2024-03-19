// https://leetcode.com/problems/remove-element/

class Solution {
public:
    int removeElement(vector<int>& p, int val) {
        int k=0;
        for(int i=0; i<p.size();i++)
        {
            int temp=0;
            if(p[i]!=val)
            {
                temp = p[k];
                p[k++]=p[i];
                p[i]=temp;
            }
        }
        return k;
    }
};