def getFinalAmount (initialAmount , betResults):
    bet=1
    amm=initialAmount
    for x in betResults:
        if x=="W":
            amm+=bet
            bet=1
        else:
            amm-=bet
            bet=bet*2

        if(bet>amm):
            return amm
    return amm

print(getFinalAmount(100,["W","W","W","L","L","L","W","L","L","L","L","L","L","L","L","L","L"]))