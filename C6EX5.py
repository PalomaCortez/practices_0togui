## Cap 6 - functions
# EX5 - Print Calendar

def print_month(year, month):
    # print the headings of the calendar
    print_month_title(year, month)

    # print the body of the calendar
    print_month_body(year, month)


# print the month title e.g.. May 1999
def print_month_title(year, month):
    print("         ", get_month_name(month), " ", year)
    print("----------------------------------------")
    print(" Sun  Mon  Tue  Wed  Thu  Fri  Sat")


# print month body
def print_month_body(year, month):
    # Get start day of the month for the first date of the month
    start_day = get_start_day(year, month)

    # Get number of days in the month
    number_of_days_in_month = get_number_of_days_in_month(year, month)

    # Pad space before the first day of the month
    i = 0
    for i in range(0, start_day):
        print("    ", end=" ")

    for i in range(1, number_of_days_in_month + 1):
        print(format(i, "4d"), end=" ")

        if (i + start_day) % 7 == 0:
            print()  # jump to the next line


# Get the English name for the month
def get_month_name(month):
    if month == 1:
        month_name = "January"
    elif month == 2:
        month_name = "February"
    elif month == 3:
        month_name = "March"
    elif month == 4:
        month_name = "April"
    elif month == 5:
        month_name = "May"
    elif month == 6:
        month_name = "June"
    elif month == 7:
        month_name = "July"
    elif month == 8:
        month_name = "August"
    elif month == 9:
        month_name = "September"
    elif month == 10:
        month_name = "October"
    elif month == 11:
        month_name = "November"
    else:
        month_name = "December"

    return month_name


# Get the start day of the month/1/year
def get_start_day(year, month):
    START_DAY_FOR_JAN_1_1800 = 3

    # Get the total number of days from 1/1/1800 to month/1/year
    total_number_of_days = get_total_number_of_days(year, month)

    # Return the start day for month/1/year
    return (total_number_of_days + START_DAY_FOR_JAN_1_1800) % 7


# Get the total number of days from 1/1/1800
def get_total_number_of_days(year, month):
    total = 0

    # Get the total number of days from 1/1/1800 to 1/1/year
    for i in range(1800, year):
        if is_leap_year(i):
            total = total + 366
        else:
            total = total + 365

    # Add days from Jan to the month prior to the calendar month
    for i in range(1, month):
        total = total + get_total_number_of_days(year, i)

    return total


# get the number of days in a month
def get_number_of_days_in_month(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31

    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30

    if month == 2:
        return 29 if is_leap_year(year) else 28

    return 0  # if month is incorrect


# determine if it is a leap year
def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def main():
    # prompt the user to enter the month and year
    year = eval(input("Enter full year (e.g., 2001): "))
    month = eval(input("Enter month as a number between 1 and 12: "))

    # print calendar for the month of the year
    print_month(year, month)


main()  # call the main function
