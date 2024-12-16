def load_bar(percent):
  bar = ["%"] * 10
  result = [
   f"{percent}%",]
  
  if percent < 100:
    
    percent_max_index = int(percent / 10)
    
    for i in range(0, 10):
      
      if i < percent_max_index:
        bar[i] = "%"
      else:
        bar[i] = "."
        
    result[0] += f" [{''.join(bar)}]"
    
    result.append("Still loading...")
  else:
    bar = ["%"] * 10
    
    result[0] += " Complete!"
    
    result.append(f"[{''.join(bar)}]")
  
  
  print("\n".join(result))

input_percent = int(input())

load_bar(input_percent)
