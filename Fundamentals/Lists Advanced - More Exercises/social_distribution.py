population = [int(num) for num in input().split(", ")]
poor_limit = int(input())

for i in range(len(population)):
  
  richest = max(population)
  richest_index = population.index(richest)
  
  if population[i] >= poor_limit:
    continue
    
  needed = poor_limit - population[i]
    
  if (richest - needed) >= poor_limit:
    population[richest_index] -= needed
    population[i] += needed
  
  else:
    print("No equal distribution possible")
    break

else:  
  print(population)
