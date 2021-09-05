# Problem URL: https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
	# Handling Negative Input
        neg_flag = 0
        if x<0:
            neg_flag = 1
        string = [i for i in str(x)]
        if neg_flag == 1:
            string = string[1:]
        reversed_string = string[::-1]
        final_string = ''
        for i in reversed_string:
            final_string += i
        final_int =  int(final_string)

	# Handling Negative Input
        if neg_flag == 1:
            final_int = -final_int

	# Limit Checking
        if (final_int < -2**31 or final_int > 2**31 - 1):
            return 0
        return final_int