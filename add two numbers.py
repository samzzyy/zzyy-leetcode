# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # dummy = cur = ListNode(0)
        # carry = 0
        # while l1 or l2 or carry:
        #     if l1:
        #         carry += l1.val
        #         l1 = l1.next
        #     if l2:
        #         carry += l2.val
        #         l2 = l2.next
        #     cur.next = ListNode(carry%10)
        #     cur = cur.next
        #     carry //= 10
        # return dummy.next
    
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            val=(carry+v1+v2)%10
            carry=(carry+v1+v2)//10
            n.next = ListNode(val)
            n = n.next
        return root.next
        
#         carry=(l1.val+l2.val)//10
#         reserve=(l1.val+l2.val)%10
#         l3_header=ListNode(reserve)
#         l3=l3_header
#         while (l1.next!=None)|(carry>0)|(l2.next!=None):
#             if (l2.next!=None)&(l1.next!=None):
#                 reserve=(carry+l1.next.val+l2.next.val)%10

#                 temp_l=ListNode(reserve)
#                 carry=(carry+l1.next.val+l2.next.val)//10

#                 l3.next=temp_l
#                 l3=temp_l
#                 l1.next=l1.next.next
#                 l2.next=l2.next.next
#             elif(l1.next!=None):
#                 reserve=(carry+l1.next.val)%10
#                 temp_l=ListNode(reserve)
#                 l3.next=temp_l
#                 l3=temp_l
#                 carry=(carry+l1.next.val)//10
#                 l1.next=l1.next.next
                
#             elif(l2.next!=None):
#                 reserve=(carry+l2.next.val)%10
#                 temp_l=ListNode(reserve)
#                 l3.next=temp_l
#                 l3=temp_l
#                 carry=(carry+l2.next.val)//10
#                 l2.next=l2.next.next
                
#             else:
#                 temp_l=ListNode(carry)
#                 l3.next=temp_l
#                 carry=0
            
#         return l3_header
            
            