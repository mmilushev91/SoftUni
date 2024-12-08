n = int(input())

not_pure = [",", ".", "_"]

for _ in range(n):

    string = input()

    for char in string:

        if char in not_pure:
            print(f"{string} is not pure!")
            break
    else:
        print(f"{string} is pure.")
