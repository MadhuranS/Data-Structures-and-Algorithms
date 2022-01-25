def make_squares(arr):
  ans = [0] * len(arr)
  idx = len(ans) - 1

  l = 0
  r = len(arr) - 1

  while l <= r:
    lSquared = arr[l] ** 2
    rSquared = arr[r] ** 2

    if lSquared > rSquared:
      ans[idx] = lSquared
      l += 1
    else:
      ans[idx] = rSquared
      r -= 1
    idx -= 1
  return ans