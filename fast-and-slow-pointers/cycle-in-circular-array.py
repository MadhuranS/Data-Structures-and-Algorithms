def circular_array_loop_exists(arr):
  # TODO: Write your code here

  ##check for every array index
  ##fast and slow pointer
  ##break if change in direction
  ##return true if slow == fast

  for i in range(len(arr)):
    flag = True
    slow, fast = i, i
    directionForward = arr[i] > 0
    while True:
      slow = getNextIndex(slow, arr, directionForward)
      fast = getNextIndex(fast, arr, directionForward)
      if fast < 0 or slow < 0:
        break
      fast = getNextIndex(fast, arr, directionForward)
      if fast < 0:
        break
      if slow == fast:
        return True
  return False


def getNextIndex(index, arr, directionForward):
  index = (index + arr[index]) % (len(arr))
  if directionForward != (arr[index] > 0):
    return -1
  return index


def main():
  print(circular_array_loop_exists([1, 2, -1, 2, 2]))
  print(circular_array_loop_exists([2, 2, -1, 2]))
  print(circular_array_loop_exists([2, 1, -1, -2]))


main()
