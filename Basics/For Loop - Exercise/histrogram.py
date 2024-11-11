numbers_count = int(input())

p1, p2, p3, p4, p5 = 0, 0, 0, 0, 0

for _ in range(numbers_count):
    num = int(input())
    
    if num < 200:
        p1 += 1 
    elif num < 400:
        p2 += 1 
    elif num < 600:
        p3 += 1 
    elif num < 800:
        p4 += 1 
    else:
        p5 += 1 

print(f"{p1 / numbers_count * 100:.2f}%")
print(f"{p2 / numbers_count * 100:.2f}%")
print(f"{p3 / numbers_count * 100:.2f}%")
print(f"{p4 / numbers_count * 100:.2f}%")
print(f"{p5 / numbers_count * 100:.2f}%")
