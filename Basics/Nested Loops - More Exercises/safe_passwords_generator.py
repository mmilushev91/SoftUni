A_START = 35
A_END = 55
B_START = 64
B_END = 96

a = int(input())
b = int(input())

password_count_limit = int(input())

password_counter = 0

char1 = A_START
char2 = B_START
x = 1
y = 1

while password_count_limit != password_counter:
  
  if char1 > A_END:
    char1 = A_START
  
  if char2 > B_END:
    char2 = B_START
  
  password_counter += 1 
  
  print(f"{chr(char1)}{chr(char2)}{x}{y}{chr(char2)}{chr(char1)}", end="|")
  
  char1 += 1 
  char2 += 1 
  
  y += 1
  
  if y > b:
    x += 1 
    y = 1
  
  if x > a:
    break
    
