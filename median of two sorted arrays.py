class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length=len(nums1)+len(nums2)
        indice_1=0
        indice_2=0
        sort_list=[]
        for _ in range(length):
            if (len(nums1)>indice_1)&(len(nums2)>indice_2):
                    if(nums1[indice_1]>=nums2[indice_2]):
                        sort_list.append(nums2[indice_2])
                        indice_2+=1
                    else:
                        sort_list.append(nums1[indice_1])
                        indice_1+=1
            elif(len(nums1)>indice_1):
                sort_list.append(nums1[indice_1])
                indice_1+=1
            elif(len(nums2)>indice_2):
                sort_list.append(nums2[indice_2])
                indice_2+=1
        if length%2==0:
            return (sort_list[length//2-1]+sort_list[length//2])/2
        else:
            return sort_list[length//2]
        
