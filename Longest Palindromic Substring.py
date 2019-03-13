# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"

# 14464 ms	13.2 MB
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<2:
            return s
        length=len(s)
        final_substring=''
        for index,word in enumerate(s):
            for i in range(index+1):#回文开始的位置,回文的长度length-index,
                flag=0
                for _ in range((length-index)//2+(length-index)%2):#  //2+1检查是否是回文
                    # print((length-index),i,_,s[i:length-index+i],s[i+_],s[i+(length-index)-1-_])
                    if (s[i+_]!=s[i+(length-index)-1-_]):
                        flag=0
                        break
                    flag=1# 最终循环退出后flag==1，则为真回文
                if (flag==1):
                    return s[i:length-index+i]

# 884 ms 13.3 MB
class Solution_others:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            # odd case, like "dcaba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res

    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

s='abcd'
s[1]=' '
print(s)

