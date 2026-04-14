# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = None
        pointer = None

        while(True):
            minimum: Optional[ListNode] = None
            minimumInd = -1
            for i in range(len(lists)): 
                if lists[i] == None: 
                    continue
                if minimum == None: 
                    minimum = lists[i]
                    minimumInd = i
                    continue
                if lists[i].val < minimum.val:
                    minimum = lists[i]
                    minimumInd = i

            if minimum != None: 
                lists[minimumInd] = minimum.next
                if result == None:
                    result = ListNode(minimum.val, None)
                elif result.next == None:
                    pointer = ListNode(minimum.val, None)
                    result.next = pointer
                else:
                    pointer.next = minimum
                    pointer = pointer.next
            else: 
                return result 
 
        return result

                
            

        

            