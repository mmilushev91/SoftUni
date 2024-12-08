command = input()

while command != "End":
    string = command

    if string != "SoftUni":
        repeated_string = ""

        for char in string:
            repeated_string += char * 2

        print(repeated_string)
        
    command = input()
