company_name = input()
addults_ticket_count = int(input())
kids_ticket_count = int(input())
addults_ticket_price = float(input())
service_tax = float(input())

addults_price = addults_ticket_count * (service_tax + addults_ticket_price)
  
kids_price = ((addults_ticket_price * 0.30) + service_tax) * kids_ticket_count

final_income = (addults_price + kids_price) * 0.20

print(f"The profit of your agency from {company_name} tickets is {final_income:.2f} lv.")
