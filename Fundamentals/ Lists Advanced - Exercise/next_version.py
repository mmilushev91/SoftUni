start, mid, end = [int(num) for num in input().split(".")]

end += 1 

if end > 9:
  end = 0
  mid += 1 
  
  if mid > 9:
    mid = 0
    start += 1

print(f"{start}.{mid}.{end}")
