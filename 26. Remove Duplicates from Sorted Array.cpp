// https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution {
public:
    int removeDuplicates(vector<int>& p) {
        int k=1;
	    for(int i=1; i<p.size(); i++)        
		    if(p[i]!=p[i-1]) p[k++] = p[i];     
	    return k;
    }
};