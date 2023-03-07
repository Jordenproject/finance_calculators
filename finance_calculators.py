import math
print("choose either 'investment' or 'bond' from the menu below to proceed:")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

# defines input variable
calculation = input("Please choose your calculation:")

# iterates through required variations of input
if calculation in ('Investment' 'INVESTMENT' 'investment'):

# requests below inputs from user for investment calculation
    deposit = float(input("Please enter your deposit:"))
    interest_rate = float(input("Please enter interest rate:"))
    num_years = float(input("Please enter number of years you are investing:"))
    interest = input("Please enter simple or compound interest:")
    r = interest_rate/100

# below is a a sum for simple and compound interest
# below will also print simple and compound interest sum
    simple_interest = deposit*(1+r*num_years)
    compound_interest = deposit*math.pow((1+r),num_years)
    if interest in ('simple'):
        print("Your simple interest is:" + str(simple_interest))
    elif interest in ('compound'):
        print("Your compound interest is:" + str(compound_interest))

# below requests values from user and prints amount that will have to repaid on a home loan each month
elif calculation in ('BOND' 'Bond' 'bond'):
    value_house = float(input("Please enter value of your home:"))
    interest_bond = float(input("Please enter interest rate:"))
    month_rate = interest_bond/12
    num_months = float(input("Please enter number of months you want to repay bond:"))
    repay_month = (month_rate.value_house)/(1 - (1+month_rate)^(-num_months))
    print(repay_month)

# if other than investment or bond is printed below will print   
else:
    print("Error")