//https://leetcode.com/problems/reverse-integer/

int reverse(long int x){
    int rev = 0;
    while (x != 0) {
        int remainder = x % 10;
        x /= 10;
        if (rev > INT_MAX/10 || rev < INT_MIN/10)
            return 0;
        rev = rev * 10 + remainder;
        }
        return rev;
}