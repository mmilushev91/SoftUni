wanted_book = input()

command  = input()
books_counter = 0


while command != "No More Books":
  
  searched_book = command
  
  
  if wanted_book == searched_book:
    print(f"You checked {books_counter} books and found it.")
    break
  books_counter += 1 
  command = input()

else:
  print("The book you search is not here!")
  print(f"You checked {books_counter} books.")
  
