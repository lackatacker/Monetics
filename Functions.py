from datetime import date
import random
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
def determineIssuerNetwork(firstDigit):
    if (firstDigit == '3'): issuingBankNetwork = 'American Express'
    elif (firstDigit == '4'): issuingBankNetwork = 'Visa'
    elif (firstDigit == '5'): issuingBankNetwork = 'MasterCard'
    elif (firstDigit == '6'): issuingBankNetwork = 'Discover'
    else: issuingBankNetwork = 'Unknown'
    return issuingBankNetwork
#-----------------------------------------------------------------------------------------------------#
def calculateDigit(pan):
    pan=pan[::-1]
    count=0
    sum=0
    i=len(pan)-1
    pan=[int(x) for x in pan]
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
    return sum%10
#------------------------------------------------------------------------------------------------------#
def generateNCards(number,IssuerNetworkID):
    count=0
    while(count<number):
        pan = ''
        while (len(pan) < 14):
            pan += str(random.randint(0, 9))
        pan = str(IssuerNetworkID) + pan
        pan += str(calculateDigit(pan))
        print(str(count+1)+' : '+ pan)
        count += 1


