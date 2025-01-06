qty = float(input("Enter the investment QTY: "))
interest = float(input("Write the porcentage of your investment return expectations? "))
years = int(input("How many years? "))

result = round(qty * (interest / 100 + 1) ** years, 2)
print(f"||||||||||||||||||||||\nThis is your return:\n ${result} \n||||||||||||||||||||||")