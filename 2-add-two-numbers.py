#!/usr/bin/python
# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        placeholder = self
        finalStr = ""
        while placeholder != None:
            finalStr += str(placeholder.val)
            placeholder = placeholder.next
            
        return finalStr


class Solution:

    def __init__(self):
        thing = 0
        
    def carryCatchAll(self, carry):
        if carry == 0:
            return None
        return ListNode(carry, None)
        
    def addTheHardWay(self, l1, l2, power=0, carry=0):
        if (l1 != None and l2 != None) and l1.next == None and l2.next == None:
            final = l1.val + l2.val + carry
            newCarry = (final - (final % 10))//10
            return ListNode(final%10, self.carryCatchAll(newCarry))
        elif l1 != None and l2 != None:
            initial = l1.val + l2.val + carry
        elif (l1 == None or l1.next == None) and l2 != None:
            initial = l2.val + carry
        elif (l2 == None or l2.next == None) and l1 != None:
            initial = l1.val + carry
        else:
            return self.carryCatchAll(carry)
            
        newCarry = (initial - (initial % 10))//10
        final = initial % 10
        
        if l1 == None:
            part1 = l1
        else:
            part1 = l1.next
        if l2 == None:
            part2 = l2
        else:
            part2 = l2.next
        nextNode = self.addTheHardWay(part1, part2, power+1, newCarry)
        node = ListNode(final, nextNode)
        return node

    def addTwoNumbers(self, l1, l2):
        return self.addTheHardWay(l1, l2)
    
    
n1 = ListNode(9, None)
n2 = ListNode(1, None)
sol = Solution()
print(sol.addTwoNumbers(n1, n2))
