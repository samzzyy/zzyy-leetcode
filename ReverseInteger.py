# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            output_num = 0
            while (x != 0):
                output_num = output_num * 10 + (x % 10)
                x = x // 10
            if output_num < 2147483648:
                return output_num
            else:
                return 0
        else:
            x = -x
            output_num = 0
            while (x != 0):
                output_num = output_num * 10 + (x % 10)
                x = x // 10
            if output_num < 2147483648:
                return -1 * output_num
            else:
                return 0

# print(("z">"1")&("z"<"9"))
a="   -42".split(' ')
a.remove('')
print(a)