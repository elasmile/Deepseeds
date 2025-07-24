# #simple calculator
# first_number = float(input("Enter the first number"))
# second_number = float(input("Enter the second number"))
# operator = input("Enter operator")
# result = 0

# if operator == "+":
#     results = first_number + second_number
# elif operator == "=":
#   results = first_number - second_number
# elif operator == "*":
#   results = first_number *second_number
# elif operator == "/":
#   if second_number == 0:
#     print("Undefined, Enter a number different from 0")
#   results = first_number / second_number

# else:
#     print("Please check your operator sign again")


# print(f"The results of ur computation is {results}")

#leap year exercise
print("___" * 50)
year = int(input("Enter the year to check: "))

if year%4==0 and year%100 != 0 or year%400==0:
    print(f"The year {year}, was/is a leap year")
else:
    print(f"The year {year}, was/is not a leap year")
