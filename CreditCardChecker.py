#   A Valid credit card has to:
# -Respect Luhn algorithm
# -Should have a valid expiry date (current year-month max)
# -Number of CVV digits depends on the card issuer
import Functions
pan=input('Enter the pan: ')
if(Functions.verifyLuhn(pan)):
    expdate=int(input('Enter expiry date: '))
    if(Functions.verifyExpiryDate(expdate)):
        firstDigit=pan[0]
        cvv=input('Enter CVV: ')
        if(Functions.verifyCvv(firstDigit, cvv)):
            print('Valid '+Functions.determineBrand(pan[0])+' card!')
        else:
            print('Invalid CVV!')
    else:
        print('Invalid expiry date!')
else:
    print('Invalid personal account number!')
