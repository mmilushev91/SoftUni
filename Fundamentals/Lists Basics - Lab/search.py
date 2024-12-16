n = int(input())
word = input()

complete_list = []
filtered_list = []

for _ in range(n):
  item = input()
  
  complete_list.append(item)
  
  if word in item:
    filtered_list.append(item)

print(complete_list)
print(filtered_list)
