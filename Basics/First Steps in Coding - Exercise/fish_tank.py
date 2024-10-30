SHOES_PERCENT = 0.4
OUTFIT_PERCENT = 0.2
BALL_PERCENT = 0.25
ACCESSORIES = 0.2

yearly_tax = int(input())

shoes = yearly_tax - (yearly_tax * SHOES_PERCENT)
outfit = shoes - (shoes * OUTFIT_PERCENT)
ball = outfit * BALL_PERCENT
accessories = ball * ACCESSORIES

total_cost = yearly_tax + shoes + outfit + ball + accessories

print(total_cost)
