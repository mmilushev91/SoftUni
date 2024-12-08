first = input()
second = input()

for i in range(len(first)):

    if first[i] != second[i]:
        print(f"{second[:i+1]}{first[i+1::]}")
