first_line = input().split()
second_line = input().split()
third_line = input().split()

for index in range(3):
  
  if first_line[index] == "1" and second_line[index] == "1"\
    and third_line[index] =="1":
      print("First player won")
      quit()
  
  if first_line[index] == "2" and second_line[index] == "2"\
    and third_line[index] =="2":
      print("Second player won")
      quit()
    
if first_line[0] == "1" and second_line[1] == "1" and third_line[2] == "1":
    print("First player won")
    quit()

if first_line[0] == "2" and second_line[1] == "2" and third_line[2] == "2":
    print("Second player won")
    quit()

if first_line[2] == "1" and second_line[1] == "1" and third_line[0] == "1":
    print("First player won")
    quit()

if first_line[2] == "2" and second_line[1] == "2" and \
  third_line[0] == "2":
    print("Second player won")
    quit()

if first_line.count("1") == 3:
    print("First player won")
    quit()

if second_line.count("1") == 3:
    print("First player won")
    quit()

if third_line.count("1") == 3:
    print("First player won")
    quit()

if first_line.count("2") == 3:
    print("Second player won")
    quit()

if second_line.count("2") == 3:
    print("Second player won")
    quit()

if third_line.count("2") == 3:
    print("Second player won")
    quit()

print("Draw!")
