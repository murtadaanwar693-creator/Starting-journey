string = input("Enter the input: ")
if string.isdigit():
    string =float(string)
    if string > 0 and string % 2 == 0:
        print("Positive, Whole number, Even")
    elif string > 0 and string % 2 == 1:
        print("Positive, Whole number, Odd")
    else: print("Zero, Whole number")
# it falls through the next block unnecessarily in some cases
try:
    string = float(string)
    if string < 0 and string % 2 == 0:
        print("Negative, Whole number, Even")
    elif string < 0 and string % 2 == 1:
        print("Negative, Whole number, Odd")
except ValueError:
    if string[0:2] == "py" and string [2] == " ":
        print("Looks like a Python keyword or module!")
    else:
        string = string.upper()
        print(string)
        print(len(string))
        print(string[0], string[-1])
        is_digit = False
        for check in string:
            if check.isdigit():
                is_digit = True
        if is_digit:
            print("It contains number/s!")
        else:
            print("It does not contain any number!")