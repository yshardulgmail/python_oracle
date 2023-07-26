#Answers to the coding exercises in this URL - 
#https://www.codingninjas.com/studio/library/30-most-common-accenture-coding-questions


"""
30. Write a function to check if the given two strings are anagrams or not. 
Return ‘Yes’ if they are anagrams, otherwise, return ‘No’.
Example
Input 1: build
Input 2: dubli
Output:
Yes 
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def populate_list(self, arr):
        list1 = end = ListNode(arr[0])
        # count = 0
        for i in range(1, len(arr)):
            # print(f"Iteration==>{count+1}")
            node = ListNode(arr[i])
            end.next = node
            end = node
        
        return list1
    
    def sort_list(self, list_to_sort):
        i = list_to_sort
        
        while i.next:
            j = i.next
            while j:
                if i.val > j.val:
                    temp = i.val
                    i.val = j.val
                    j.val = temp
                j = j.next
            i = i.next
        
        return list_to_sort

    
    def copy_list(self, copy_to_list, copy_from_list):
        first = copy_from_list
        while first:
            # print(first.val)
            copy_to_list.next = ListNode(first.val)
            copy_to_list = copy_to_list.next
            first = first.next

        return copy_to_list

    def display_list(self, list_to_show):
        first = list_to_show
        while first:
            print(first.val)
            first = first.next

    def mergeTwoLists(self) -> ListNode:
        arr1 = [1,2,4]
        arr2 = [1,3,4]

        list1 = self.populate_list(arr1)
        list2 = self.populate_list(arr2)
        
        merged = end = ListNode(list1.val)
        end = self.copy_list(end, list1.next)
        end = self.copy_list(end, list2)

        merged = self.sort_list(merged)
        self.display_list(merged)

        return list1
                    

def exercise_30():
    solution = Solution()
    solution.mergeTwoLists()
    

exercise_30()


