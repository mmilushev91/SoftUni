numbers = [int(num) for num in input()]

numbers.sort(reverse=True)

print(''.join([str(num) for num in numbers]))
