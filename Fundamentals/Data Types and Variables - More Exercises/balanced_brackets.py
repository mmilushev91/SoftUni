n = int(input())

brackets = ""

for _ in range(n):
    string = input()
  
    if string == "(" or string == ")":
      brackets += string
      
      if len(brackets) == 2:
      
        if brackets == "()":
          brackets = ""
        
        else:
          print("UNBALANCED")
          break
