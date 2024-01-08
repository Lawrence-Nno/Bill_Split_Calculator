def tip_calculator():
    """
    This function calculates the total amount each individual should pay when splitting bills taking into account
    the total bill, total number of persons involved and the % of bill to add as tip
    :return: a float rounded to 2 decimal places
    """

    # Welcome message
    print("Welcome to the Tip Calculator")

    # A while loop to ensure only a float or integer is inputted as bill
    while True:
        try:
            bill = float(input("What was the total bill?\n"))
        except ValueError:
            print("Bill must be numerals")
        else:
            break

    # A while loop to ensure only an integer is inputted as number of persons
    while True:
        try:
            num_of_persons = int(input("How many people to split the bill?\n"))
        except ValueError:
            print("Number of persons must be a whole number")
        else:
            break

    # A while loop to ensure only a float or integer is inputted as tip percentage
    while True:
        try:
            tip = float(input("What percentage tip would you like to give?\n"))
        except ValueError:
            print("Percentage must be a float or a whole number")
        else:
            break

    # Amount each person should pay rounded to 2 decimal places
    amount_to_pay = round(((bill + ((tip/100) * bill)) / num_of_persons), 2)

    print(f"Each person should pay ${amount_to_pay}")
    return amount_to_pay


if __name__ == '__main__':
    tip_calculator()

