a = 0

print("Hi, how old are you? ")
a = int(input())

if a < 4 and a > 0:
    print(a + " so you most be a baby..")
elif a < 13 and a >= 4:
    print(a + " so you most be a kid..")
elif a < 18 and a >= 13:
    print(a + " so you most be a teenager..")
elif a >= 18 and a < 111:
    print(a + " so you most be a adult..")
else:
    print("Yes, I guess " + str(a) + " that is not right..")
