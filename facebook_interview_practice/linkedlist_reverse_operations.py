'''
Reverse Operations
You are given a singly-linked list that contains N integers. 
A subpart of the list is a contiguous set of even elements, bordered either 
by either end of the list or an odd element. For example, if the list is 
[1, 2, 8, 9, 12, 16], the subparts of the list are [2, 8] and [12, 16].
Then, for each subpart, the order of the elements is reversed. In the 
example, this would result in the new list, [1, 8, 2, 9, 16, 12].
The goal of this question is: given a resulting list, 
determine the original order of the elements.
'''


from __future__ import print_function
import math

class Node:
  def __init__(self, x):
    self.data = x
    self.next = None


def reverse(head):
  # Write your code here
  top = head
  evens = [] # list will collect even number linked lists
  while top is not None:
    if top.data % 2 == 0:
      evens.append(top)
      
    if top.data % 2 != 0 or top.next is None:
      # reverse the evens list
      for i in range(len(evens)//2):
        evens[i].data, evens[len(evens)-i-1].data = evens[len(evens)-i-1].data, evens[i].data
      # evens.clear()
      evens[:] = []
      
    

    top = top.next
  return head



def printLinkedList(head):
  print('[', end='')
  while head != None:
    print(head.data, end='')
    head = head.next
    if head != None:
      print(' ', end='')
  print(']', end='')

test_case_number = 1

def check(expectedHead, outputHead):
  global test_case_number
  tempExpectedHead = expectedHead
  tempOutputHead = outputHead
  result = True
  while expectedHead != None and outputHead != None:
    result &= (expectedHead.data == outputHead.data)
    expectedHead = expectedHead.next
    outputHead = outputHead.next

  if not(outputHead == None and expectedHead == None):
    result = False

  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, ' Test #', test_case_number, sep='')
  else:
    print(wrongTick, ' Test #', test_case_number, ': Expected ', sep='', end='')
    printLinkedList(tempExpectedHead)
    print(' Your output: ', end='')
    printLinkedList(tempOutputHead)
    print()

  test_case_number += 1

def createLinkedList(arr):
  head = None
  tempHead = head
  for v in arr:
    if head == None:
      head = Node(v)
      tempHead = head
    else:
      head.next = Node(v)
      head = head.next
  return tempHead

head_1 = createLinkedList([1, 2, 8, 9, 12, 16])
expected_1 = createLinkedList([1, 8, 2, 9, 16, 12])
output_1 = reverse(head_1)
printLinkedList(output_1)

head_2 = createLinkedList([2, 18, 24, 3, 5, 7, 9, 6, 12])
expected_2 = createLinkedList([24, 18, 2, 3, 5, 7, 9, 12, 6])
output_2 = reverse(head_2)
printLinkedList(output_2)