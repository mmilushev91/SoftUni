color_points = {
  "red": [0, lambda x: x + 5],
  "orange": [0, lambda x: x + 10],
  "yellow": [0, lambda x: x + 15],
  "white": [0, lambda x: x + 20],
  "black": [0, lambda x: int(x / 2)],
}

n = int(input())

others = 0
final_points = 0
  
for _ in range(n):
  color = input()
  
  if color not in color_points:
    others += 1
    
    continue
  
  final_points = color_points[color][1](final_points)
  
  color_points[color][0] += 1
  
print(f"Total points: {final_points}")  
print(f"Red balls: {color_points['red'][0]}")
print(f"Orange balls: {color_points['orange'][0]}")
print(f"Yellow balls: {color_points['yellow'][0]}")
print(f"White balls: {color_points['white'][0]}")
print(f"Other colors picked: {others}")
print(f"Divides from black balls: {color_points['black'][0]}")
