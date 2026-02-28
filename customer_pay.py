print("================= Coffee Shop =================")
price = float(input("Enter the price of the cofee: "))
has_a_card = input("Does he have a loyalty card? (y/n) : ")== "y"
hour = int(input("What time is it? : "))
time= input("Enter the time (AM/PM) : ") == "AM"
is_happy_hour = hour < 10 and time
print(f"Your coffe price is : {price*(75/100): .2f}" if has_a_card and is_happy_hour else(f"Your coffe price is : {price * (85/100): .2f}" if (has_a_card and not is_happy_hour) or (not has_a_card and is_happy_hour)  else f"Your coffe price is: {price: .2f}" ) )