numbers = [list(((int(num) for num in number))) for number in input().split()]
message = list(input())

message_last_index = len(message)
word = ""

for number in numbers:
    digit_sum = sum(number)
    char_to_add_index = digit_sum

    while char_to_add_index >= message_last_index:
        char_to_add_index -= message_last_index

    word += message.pop(char_to_add_index)

print(word)
