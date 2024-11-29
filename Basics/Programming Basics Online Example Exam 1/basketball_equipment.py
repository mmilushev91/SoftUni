yearly_basketball_price = int(input())

shoes = yearly_basketball_price - yearly_basketball_price * 0.40
shirt = shoes - shoes * 0.20
ball = shirt / 4 
accessories = ball / 5 

total_cost = yearly_basketball_price + shoes + shirt + ball + accessories

print(f"{total_cost:.2f}")
