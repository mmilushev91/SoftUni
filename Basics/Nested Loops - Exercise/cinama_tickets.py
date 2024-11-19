command = input()

tickets = {
  "student": 0,
  "standard": 0,
  "kid": 0
}

total_tickets = 0

while command != "Finish":
  movie = command
  
  tickets_count = int(input())
  
  sold_tickets = 0
  
  for _ in range(tickets_count):
    ticket_type = input()
    
    if ticket_type == "End":
      break
    
    tickets[ticket_type] += 1
    sold_tickets += 1
  
  total_tickets += sold_tickets
  
  print(f"{movie} - {sold_tickets / tickets_count * 100:.2f}% full.")
  
  command = input()

student_tickets = tickets["student"] / total_tickets * 100
standard_tickets = tickets["standard"] / total_tickets * 100
kid_tickets = tickets["kid"] / total_tickets * 100
  
print(f"Total tickets: {total_tickets}")
print(f"{student_tickets:.2f}% student tickets.")
print(f"{standard_tickets:.2f}% standard tickets.")
print(f"{kid_tickets:.2f}% kids tickets.")
