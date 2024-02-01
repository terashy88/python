sname = "susanne"   # "f" from line 2 is important for input in line 4
comment = f"""
comment section
hello {sname},
this is a test line
"""

print("hello double quotes")
print('\nhello with with single quotes')
name, Year = "Richard", 1985
# Year = 1985
number = 1, 2, 3, 4, 5
print(Year, number, Year, name, Year)


def hello():  # only lowercase
    Year = "2020"
    return "hello"


print(comment,)
