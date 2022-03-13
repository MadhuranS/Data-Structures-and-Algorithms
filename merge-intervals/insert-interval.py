def insert(intervals, new_interval):
  merged = []
  first = new_interval[0]
  last = new_interval[1]
  counter = len(intervals)
  for i in range(len(intervals)):
    interval = intervals[i]
    if last >= interval[0] and first < interval[0]:
      last = max(interval[1], last)
    elif first <= interval[1] and last > interval[1]:
      first = min(interval[0], first)
    else: 
      if interval[0] > last:
        merged.append([first, last])
        counter = i
        break
      merged.append(interval)
  
  if counter == len(intervals):
    merged.append([first, last])
  while counter < len(intervals):
    merged.append(intervals[counter])
    counter += 1
  # TODO: Write your code here
  return merged
