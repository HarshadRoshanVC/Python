import sys
def ReadFile(cardList):
    try:
        data = open('data.txt','r')
        lines = data.readlines()
    except:
        print('File reading failed')
        sys.exit(0)
    
    lineCount = 0
    for line in lines:
        cardList.append(line.strip())
        lineCount += 1
    data.close()
    return lineCount

def decode(cardList):
    for cardNumber in cardList:
        typeDigit = cardNumber[0:2]
        issueYear = cardNumber[2:4]
        expiryYear = cardNumber[4:6]
        expiryMonth = cardNumber[6:8]
        
        if cardNumber[8] == '1':
            cardType = 'Credit account'
        else:
            cardType = 'Debit account'
            
        accountNumber = cardNumber[8:]
        issuedBy = digitToType(typeDigit)
        message = cardNumber+": Was issued by " + issuedBy + " in 20" + issueYear + ". The card expires on " + expiryYear
        message += "/" + expiryMonth + ". The card is linked to a " + cardType + " with account number: "+accountNumber + "\n"

        writeFile(message)
        
        
def writeFile(message):
    try:
        outfile = open('Output.txt', 'a')
        outfile.write(message)
        outfile.close()
    except:
        print('Something went wrong while wrting to file')
    

def digitToType(digit):
    return {
        '01' : 'enRoute',
        '02' : 'JCB',
        '03' : "Diner's club",
        '04' : 'Visa',
        '05' : 'Master Card',
        '06' : 'UnionPay',
        '07' : 'Petroleum',
        '08' : 'TeleCom',
        '09' : 'National'
        }[digit]
    

if __name__=='__main__':
    cardList=[]
    print('Reading credit card numbers from file...')
    lineCount = ReadFile(cardList)
    print('Number of lines read:',lineCount)
    decode(cardList)
    
    
