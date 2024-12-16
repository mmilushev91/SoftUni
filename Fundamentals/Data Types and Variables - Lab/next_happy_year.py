year = int(input())

while True:
  year += 1
  string_year = str(year)
  
  year_list = [digit for digit in string_year if string_year.count(digit) < 2]
  
  if len(string_year) == len(year_list):
    print("".join(year_list))
    break
