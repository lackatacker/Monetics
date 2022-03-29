import Functions
print('Which cards network are you looking for?\n1- American Express\n2- Visa\n3- MasterCard\n4- Discover')
id=int(input())
if(id==1):print('American Express Cards:')
if(id==2):print('Visa Cards:')
if(id==3):print('MasterCard Cards:')
if(id==4):print('Discover Cards:')
Functions.generateNCards(10,id+2)
