line = [int(num) for num in input().split(", ")]
beggars = [0] * int(input())

beggar_index = 0

for index in range(len(line)):
    if beggar_index == len(beggars):
        beggar_index = 0

    beggars[beggar_index] += line[index]

    beggar_index += 1

print(beggars)
