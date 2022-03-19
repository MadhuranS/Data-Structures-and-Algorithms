from __future__ import print_function
from heapq import *

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def find_employee_free_time(schedule):
    result = []
    heap = []
    for i, emp in enumerate(schedule):
        heappush(heap, (emp[0].start, i, 0))

    temp = heappop(heap)
    prevEnd = schedule[temp[1]][temp[2]].end
    if len(schedule[temp[1]]) > temp[2] + 1:
        newInterval = schedule[temp[1]][temp[2] + 1]
        heappush(heap, (newInterval.start, temp[1], temp[2] + 1))
    while len(heap) > 0:
        temp = heappop(heap)
        newStart = temp[0]
        if newStart > prevEnd:
            result.append(Interval(prevEnd, newStart))
        prevEnd = max(prevEnd, schedule[temp[1]][temp[2]].end)
        if len(schedule[temp[1]]) > temp[2] + 1:
            newInterval = schedule[temp[1]][temp[2] + 1]
            heappush(heap, (newInterval.start, temp[1], temp[2] + 1))

    # TODO: Write your code here
    return result


def main():

    input = [[Interval(1, 3), Interval(5, 6)], [
        Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [
        Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [
        Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()


main()
