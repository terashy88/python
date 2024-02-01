
# RSA cryptosystem
# Richard Derico


print("let's get n = p * q")

print("What is the input of p?")
p = int(input())

print("and the input of q?")
q = int(input())
n = (p*q)
print("n =", int(n))

print("Now we need m = (p - 1) * (q -1)")
print("Press any key for m")
input()
m = (p-1)*(q-1)
print("So m is:", m)

print("So now we need a Primekey 'e'")
print("the Primekey should be smaller than", m,)
print("e is?")
e = input()

print("and now we need d")
print("d has to be bigger than 0", "then d*e ^ m = 1")
print("d is?")
d = input()
print(d, "todo..")

# todo
