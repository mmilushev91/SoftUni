paint_eggs_count = {
  "red": 0, 
  "orange": 0,
  "blue": 0,
  "green": 0,
}

eggs_count = int(input())

for _ in range(eggs_count):
  color = input()
  
  paint_eggs_count[color] += 1

max_eggs = float("-inf")
max_eggs_color = None 

for item, value in paint_eggs_count.items():
  
  if value > max_eggs:
    max_eggs = value
    max_eggs_color = item

print(f"Red eggs: {paint_eggs_count['red']}")
print(f"Orange eggs: {paint_eggs_count['orange']}")
print(f"Blue eggs: {paint_eggs_count['blue']}")
print(f"Green eggs: {paint_eggs_count['green']}")
print(f"Max eggs: {max_eggs} -> {max_eggs_color}")
