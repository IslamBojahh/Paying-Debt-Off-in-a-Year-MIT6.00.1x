# read readme file to find question description

balance=3926
annualInterestRate=0.2
mimumPayment=0
bal=balance
MonthyInterestRate=annualInterestRate/12

while balance >0 :
    for i in range(12):
        Monthlyunpaidbalance=balance-mimumPayment
        balance=Monthlyunpaidbalance+(Monthlyunpaidbalance*MonthyInterestRate)
        
    if balance>0:
        mimumPayment+=10
        balance=bal
    else:
        break

print("Lowest Payment: ",mimumPayment)

