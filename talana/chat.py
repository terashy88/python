name = input("Hi, what is your name? ")
location = input("And where are you from, " + name + "? ")
print("So you are from " + location + ", ah.")

while True:
    age = int(input("..how old are you, " + name + "? "))
    if age > 110 or age <= 0:
        print("Ya I guess your are not " + str(age))
        print("..try again " + name + "!..")
    else:
        break

age += 3

print(
    "Ya, that's pretty nice. I'm "
    + str(age)
    + ", but sadly I'm not in your area. Maybe we can meet sometime in the future..."
)
