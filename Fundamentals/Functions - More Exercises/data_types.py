def data_types(data_type, num):

  if data_type == "int":
    num = int(num)
    
    return num * 2
  
  elif data_type == "real":
    num = float(num)
    
    return f"{num * 1.5:.2f}"
  
  return f"${num}$"


input_data_type = input()
input_num = input()

print(data_types(input_data_type, input_num))
