# Написать функцию, которая будет перемножать любое количество переданных ей аргументов.
def adder(*nums):
   mult = 1
   for n in nums:
      mult *= n

   return mult


print(adder(1, 2, 3, 4, 5, 6))
