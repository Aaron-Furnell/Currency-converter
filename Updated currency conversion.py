print("-Written by Aaron 😀")

##global variables
currency = ""
numbers = "1234567890"
pounds = 0
discount = 0
fee = 0

##Get and validate pounds
def get_pounds():
    while True:
        try:
            pounds = float(input("Enter pounds and pence: "))
            if pounds != "" and pounds < 2500:
                return pounds
            else:
                print("Enter something")
        except ValueError:
            print("Enter a float")


##multiply pounds by conversion fee
def conversion_fee(pounds):
    while True:
        if pounds <= 300:
            pounds *= 0.965
            return pounds
        elif pounds > 300 and pounds <= 750:
            pounds *= 0.97
            return pounds
        elif pounds > 750 and pounds <= 1000:
            pounds *= 0.975
            return pounds
        elif pounds > 1000 and pounds <= 2000:
            pounds *= 0.98
            return pounds
        else:
            pounds *= 0.985
            return pounds


##get and validate exchange rate
def exchange_rate(pounds):
    options = ["USD", "EUR", "BRL", "JPY", "TRY", "usd", "eur", "brl", "jpy", "try"]
    length = len(options)
    count = 0
    print("The currency options are: ")
    while count != length:
        print(options[count])
        count +=1
    while True:
        currency = input("Enter currency: ")
        if currency not in options:
            print("Invalid input")
        else:
            if currency == "USD" or currency == "usd":
                pounds *= 1.40
                return pounds
            elif currency == "EUR" or currency == "eur":
                pounds *= 1.14
                return pounds
            elif currency == "BRL" or currency == "brl":
                pounds *= 4.77
                return pounds
            elif currency == "TRY" or currency == "try":
                pounds *= 5.68
                return pounds
            elif currency == "JPY" or currency == "jpy":
                pounds *= 151.05
                return pounds
            else:
                print("Invalid input")

def employee_discount(pounds):
    while True:
        try:
            employee = 2
            employee = int(input("Enter 1 if you are an employee or 2 if not: "))
            if int(employee) == 1:
                pounds *= 1.05
                return pounds
            if int(employee) == 2:
                discount = 0
                return pounds
        except ValueError:
            print("Invalid input")

def output_pounds(pounds):
    rounded_pounds = round(pounds, 2)
    ##get fee here
    if origional_pounds <= 300:
        fee = 3.5
    elif origional_pounds > 300 and origional_pounds <= 750:
        fee = 3
    elif origional_pounds > 750 and origional_pounds <= 1000:
        fee = 2.5
    elif origional_pounds >1000 and origional_pounds <= 2000:
        fee = 2
    else:
        fee = 1.5

    if pounds2 == pounds:
        discount = 0
    else:
        discount = 5
        

    print(f"You had {exchanged}{currency} before any fees")
    print(f"{fee}% transaction fee")
    print(f"{discount}% discount amount")
    print(f"{rounded_pounds}{currency}")

##main
pounds = get_pounds()
origional_pounds = pounds
pounds = exchange_rate(pounds)
exchanged = pounds
pounds = conversion_fee(pounds)
pounds2 = pounds
pounds = employee_discount(pounds)
discount2 = discount
output_pounds(pounds)
                
