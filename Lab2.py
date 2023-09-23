def sum_of_series(n):
   count = 0
   sum = 0
   
   while count < n:
      count += 1
      b = int(input("Введите число: "))
      if count % 2 == 0:
        sum = sum + b
      else:
        sum = sum - b
   
   return sum
n = int(input())
print(sum_of_series(n))