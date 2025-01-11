#Asking the amount of money to invest and the interest expected
money = float(input("Please input the amount of money you want to invest: "))
interest = float(input("Please enter your expected interest: "))

#Calculations
first = money * (interest / 100 + 1)
second = first * (interest / 100 + 1)
third = second * (interest / 100 + 1)
return_ = third - money

#Reinvestment calculations
secondr = (first * (interest / 100 + 1)) + money
thirdr = (secondr * (interest / 100 + 1)) + money
return_r = thirdr - (money * 3)

#Asking if the user wants to reinvest the same amount
reinvestment = input("Do you want to reinvest the same amount yearly? please type \"YES\" or \"NO\": ")

#Possible answers
if reinvestment.lower() == "yes":
    print(f"\n------------------------------------------------------------------\n\nThis could be your savings on the 1st year: ${int(first)}.\nThis could be your savings on the 2nd year: ${int(secondr)}.\nThis could be your savings on the 3rd year: ${int(thirdr)}.\n\n------------------------------------------------------------------\n You could earn ${round(return_r, 2)} in the next 3 years\n------------------------------------------------------------------")
elif reinvestment.lower() == "no":
    print(f"\n------------------------------------------------------------------\n\nThis could be your savings on the 1st year: ${int(first)}.\nThis could be your savings on the 2nd year: ${int(second)}.\nThis could be your savings on the 3rd year: ${int(third)}.\n\n------------------------------------------------------------------\n You could earn ${round(return_, 2)} in the next 3 years\n------------------------------------------------------------------")
else:
    print("Sorry please type a valid character.")
