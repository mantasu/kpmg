def toAgeGroup(age):
    if(age < 30):
        return "18-29"
    elif(age < 40):
        return "30-39"
    elif(age < 50):
        return "40-49"
    elif(age < 60):
        return "50-59"
    else:
        return "60+"

def toPastPurchasesGroups(pastPurchases):
    if(pastPurchases < 10):
        return "0-9"
    elif(pastPurchases < 20):
        return "10-19"
    elif(pastPurchases < 30):
        return "20-29"
    elif(pastPurchases < 40):
        return "30-39"
    elif(pastPurchases < 50):
        return "40-49"
    elif(pastPurchases < 60):
        return "50-59"
    elif(pastPurchases < 70):
        return "60-69"
    elif(pastPurchases < 80):
        return "70-79"
    elif(pastPurchases < 90):
        return "80-89"
    else:
        return "90-99"

def toTenureGroups(tenure):
    if(tenure < 4):
        return "00-03"
    elif(tenure < 8):
        return "04-07"
    elif(tenure < 12):
        return "08-11"
    elif(tenure < 16):
        return "12-15"
    elif(tenure < 20):
        return "16-19"
    else:
        return "20-22"