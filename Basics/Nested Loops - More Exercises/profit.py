ones = int(input()) + 1
twos = int(input()) + 1
fives = int(input()) + 1

money = int(input())

for i1 in range(ones):
  for i2 in range(twos):
    for i3 in range(fives):

      if (i1 * 1 + i2 * 2 + i3 * 5) == money:
        print(f"{i1} * 1 lv. + {i2} * 2 lv. + {i3} * 5 lv. = {money} lv.")
