class Solution {
public:
    int myAtoi(string s) {
        double num = 0;
        short int sign = 1;
        int i = 0;

        // Ignore leading whitespace
        for (; i < s.size(); i++) {
            if (s[i] != ' ') break;
        }

        if (s[i] == '-') {
            sign = -1;
            i++;
        } else if (s[i] == '+') {
            i++;
        }

        // Read digits
        for (; i < s.size(); i++) {
            if (s[i] >= '0' && s[i] <= '9') {
                num = num * 10 + s[i] - 48;

                // Return now if number exceeds integer bounds
                if (num >= INT_MAX && sign > 0) return INT_MAX;
                if (-num <= INT_MIN && sign < 0) return INT_MIN;
            } else {
                // Break if it is a non-digit char
                break;
            }
        }

        return num * sign;
    }
};
