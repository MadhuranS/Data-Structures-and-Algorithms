def find_happy_number(num):
  # TODO: Write your code here
  num1 = num
  num2 = num
  while num2 != 1:
    num1 = square_digits(num1)
    num2 = square_digits(square_digits(num2))
    if num1 == num2:
      return False

  return True

def square_digits(num):
  product = 0
  while num > 0:
    product += (num % 10) ** 2
    num  = num // 10

  return product

def main():
  print(find_happy_number(23))
  print(find_happy_number(12))


main()
