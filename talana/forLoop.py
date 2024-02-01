import time

a = 0

print("How much do you want me to count? ")
a = int(input())

for i in range(a + 1):
    print(i)
    time.sleep(0.066)


print("done")
