from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end='')
      temp = temp.next
    print()


def find_cycle_start(head):
  slow = head
  fast = head
  current = None
  while fast is not None and fast.next is not None:
    fast = fast.next.next
    slow = slow.next
    if fast == slow:
      current = slow
      break
  
  placeholder = current
  size = 1
  current = current.next
  while current is not placeholder:
    current = current.next
    size += 1

  first = head

  for _ in range(size):
    first = first.next
  
  print(first.value)
  second = head
  while first is not second:
    first = first.next
    second = second.next
  
  return first


  



def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
