## Cap 4 - Conditional operators
# EX3 - CHINESE ZODIAC

year = eval(input("Enter a year: "))
zodiac_year = year % 12

if zodiac_year == 0:
    print("monkey")
elif zodiac_year == 1:
    print("rooster")
elif zodiac_year == 2:
    print("dog")
elif zodiac_year == 3:
    print("pig")
elif zodiac_year == 4:
    print("rat")
elif zodiac_year == 5:
    print("ox")
elif zodiac_year == 6:
    print("tiger")
elif zodiac_year == 7:
    print("rabbit")
elif zodiac_year == 8:
    print("dragon")
elif zodiac_year == 9:
    print("snake")
elif zodiac_year == 10:
    print("horse")
else:
    print("sheep")


