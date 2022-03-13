def merge(intervals_a, intervals_b):
  result = []
  i, j, = 0, 0

  while i < len(intervals_a) and j < len(intervals_b):
    intervalA = intervals_a[i]
    intervalB = intervals_b[j]
    overlaps = False

    if (intervalA[1] >= intervalB[0] and intervalA[0] <= intervalB[0]) or (intervalA[0] <= intervalB[1] and intervalA[1] >= intervalB[1]):
      overlaps = True
    
    if overlaps:
      start = max(intervalA[0], intervalB[0])
      end = min(intervalA[1], intervalB[1])
      result.append([start, end])

    if intervalA[1] < intervalB[1]:
      i += 1
    else:
      j += 1
  # TODO: Write your code here
  return result


def main():
  print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
  print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()
