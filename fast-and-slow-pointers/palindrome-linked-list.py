class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def is_palindromic_linked_list(head):
  if head is None or head.next is None:
    return True
  fast = head
  slow = head
  while fast is not None and fast.next is not None:
    fast = fast.next.next
    slow = slow.next
  
  second_half = reverseList(slow)
  temp = second_half
  while second_half is not None and head is not None:
    if second_half.value != head.value:
      break
    head = head.next
    second_half = second_half.next
  
  reverseList(temp)
  if second_half == None or head == None:
    return True
  return False

def reverseList(head):
  prev = None
  while head is not None:
    next = head.next
    head.next = prev
    prev = head
    head = next
  return prev

def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  print("Is palindrome: " + str(is_palindromic_linked_list(head)))

  head.next.next.next.next.next = Node(2)
  print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()







