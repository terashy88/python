import time

a = 22
i = int(input("hi, we are counting to " + str(a) + "!\n..from where we want start?:..\n"))

while i < a:
    print(i)
    time.sleep(0.66)
    i += 1

if i > a:
    print("you are not in the range..")
else:
    print("here we go..")
