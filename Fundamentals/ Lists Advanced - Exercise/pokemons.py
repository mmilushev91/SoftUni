distances = [int(distance) for distance in input().split()]

score = 0

while distances:
  index = int(input())
  removed_value = None
  
  if index < 0:
    removed_value = distances.pop(0)
    distances.insert(0, distances[-1])
  
  elif index >= len(distances):
    removed_value = distances.pop()
    distances.insert(len(distances), distances[0])

  else:
    removed_value = distances.pop(index)
  
  for i in range(len(distances)):
    
    if removed_value >= distances[i]:
      distances[i] += removed_value
    else:
      distances[i] -= removed_value
  
  score += removed_value

print(score)
