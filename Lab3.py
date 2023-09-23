def maximin(n):
   #n = int(input()) #количество дорог
   miN = 10000000000
   l = []

   for g in range(n):
      a = int(input()) #количество туннелей
      for g1 in range(a):
         b = int(input()) #высоты каждого туннеля
         if b < miN:
           miN = b
      l.append(miN)
      miN = 10000000000
   return l.index(max(l)) + 1, l[l.index(max(l))]

n = int(input())
print(*maximin(n))