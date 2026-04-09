import time as t
x = int(input("Enter the time: "))
for i in reversed(range(0, x)):
    seconds = (i % 60)
    minutes = int(i / 60) % 60
    hours = int(i/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    t.sleep(1)
print("Time's Up!")
# Division (/) tells you how many full groups you have.
#Remainder (%) tells you what couldn't fit into a group.