import time

i = 0
a = 0

print("How much do you want to count? ")
a = int(input())

print("Counting.. " + str(a))

while i <= a:
    print(i)
    i += 1
    time.sleep(0.066)

print("done")
