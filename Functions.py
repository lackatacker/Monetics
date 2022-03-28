from datetime import date
#-----------------------------------------------------------------------------------------------------#
def verifyLuhn(pan):
    sum = 0
    i = len(pan) - 1
    count = 0
    pan = [int(x) for x in pan]
    check = pan[i]
    i -= 1
    pan = pan[i::-1]
    while (count + 1) <= i:
        u = pan[count] * 2
        if u > 9: u = 1 + u % 10
        sum += u + pan[count + 1]
        count += 2
    if (count == i):
        u = pan[i] * 2
    if u > 9: u = 1 + u % 10
    sum += u
    sum *= 9
    if (sum % 10 == check):return 1
    return 0
#-----------------------------------------------------------------------------------------------------#
def verifyExpiryDate(expiryDate):
    month = int(expiryDate / 100)
    year = expiryDate % 100
    if 13 > month > 0 and (
            date.today().year % 100 < year or
            (date.today().year % 100 == year and month >= date.today().month)):
        return 1
    return 0
#-----------------------------------------------------------------------------------------------------#
def verifyCvv(digit,cvv):
    if(digit==3 and cvv!=4):return 0
    elif(digit==4 and cvv!=3):return 0
    return 1
#-----------------------------------------------------------------------------------------------------#
def determineBrand(firstDigit):
    if (firstDigit == '3'): issuingBank = 'American Express'
    if (firstDigit == '4'): issuingBank = 'Visa'
    if (firstDigit == '5'): issuingBank = 'MasterCard'
    if (firstDigit == '6'): issuingBank = 'Discover'
    return issuingBank
