# class Solution:
#     def twoSum(self,List,target) -> List[int]:
#         length=len(List)
#         for item0 in range(length):
#             item=target-List[item0]
#             for item1 in range(item0+1,length):
#                 if(List[item1]==item):
#                     return [item0,item1]
                
class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        dict={}
        for i,word in enumerate(nums):
            dict[word] = i
        for index,i in enumerate(nums):
            if (target-i) == i:
                if nums.count(i) == 1:
                    continue
            temp = dict.get((target-i),-1)
            if temp == -1:
                continue
            return [index,temp]
