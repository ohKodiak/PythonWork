# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         11
# Assignment:   Lab9b_Act2
# Date:         11/11/21

#get inputs
file_name = input('Please enter the output filename: ')
amount = int(input('Please enter the principal amount: '))
length = int(input('Please enter the term length (months): '))
interest_rate = float(input('Please enter the annual interest rate: '))

#calculate j 
top = amount * (interest_rate / 12)
bottom = 1 - ((1/(1+(interest_rate/12)))**length)

monthly_payment = top / bottom

#inititialize variables
balance = amount
month_number= 0
accrued_interest = 0
total_accrued_interest = 0

#creat file, calculate months, accrued interest, loan balance
with open(file_name,'w') as userfile:
    userfile.write('Month,Total Accrued Interest,Loan Balance\n')
    userfile.write('0,$0.00,${:.2f}\n'.format(amount))
    while balance >= 0.01:
        
        accrued_interest = balance * (interest_rate / 12)
        total_accrued_interest += accrued_interest
        balance = (balance + accrued_interest) - monthly_payment
        month_number += 1
        if balance <= 0:
            balance = 0
            
        userfile.write(str(month_number) + ',${:.2f},${:.2f}\n'.format(total_accrued_interest,balance))


        


    

    
    

  
    


