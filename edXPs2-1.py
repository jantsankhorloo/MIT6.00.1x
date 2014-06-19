#Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

#The following variables contain values as described below:

#balance - the outstanding balance on the credit card

#annualInterestRate - annual interest rate as a decimal

#monthlyPaymentRate - minimum monthly payment rate as a decimal

#A summary of the required math is found below:

#Monthly interest rate= (Annual interest rate) / 12.0
#Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
#Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

#Test Case:
#balance = 4213
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04

MonthlyInterestRate = annualInterestRate/12.0
MinimumMonthlyPayment = monthlyPaymentRate*balance
TotalPaid = 0

for each in range(12):
    MinimumMonthlyPayment = monthlyPaymentRate*balance
    MonthlyUnpaidBalance = balance - MinimumMonthlyPayment
    balance = MonthlyUnpaidBalance +(MonthlyInterestRate*MonthlyUnpaidBalance)
    print "Month: "+str(round(each+1,2))
    print "Minimum monthly payment: "+str(round(MinimumMonthlyPayment,2))
    print "Remaining balance: "+str(round(balance, 2))
    TotalPaid += MinimumMonthlyPayment
print "Total paid: "+str(round(TotalPaid, 2))
print "Remaining balance:"+str(round(balance, 2))
