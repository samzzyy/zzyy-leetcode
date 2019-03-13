class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (s !=""):
            max_list=[1]
            start=0
            end=1
            for _ in range(1,len(s)):
                print(s[start:end],start,end)
                if s[end] not in s[start:end]:
                    max_list.append(end-start)
                else:
                    max_list.append(end-start)
                    for char_index in range(end-start):
                        if (s[char_index]==s[end]):
                            start=start+1+char_index
                end+=1
            print(max_list)
            return max(max_list)
        else:
            return 0