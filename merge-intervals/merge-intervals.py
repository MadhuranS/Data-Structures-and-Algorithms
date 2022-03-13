from __future__ import print_function


class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def print_interval(self):
    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals):
  merged = []
  intervals.sort(key=lambda x: x.start)
  first = intervals[0].start
  last = intervals[0].end
  for i in range(1, len(intervals)):
    if intervals[i].start < last:
      last = max(last, intervals[i].end)
    else:
      merged.append(Interval(first, last))
      first= intervals[i].start
      last = intervals[i].end
  merged.append(Interval(first, last))
  return merged


def main():
  print("Merged intervals: ", end='')
  for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
    i.print_interval()
  print()

main()