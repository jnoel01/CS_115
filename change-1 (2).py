#Jessica Noel
#9/18/19
#Branch Recursion Lab4
#I Pledge my Honor that I have abided by the Stevens Honor System

def change(amount, coins):
    '''Will obtain the smallest amount of coins needed (coins are given in
7,24 and 42) to fufill the needed number'''
    if amount == 0:
        return 0
    elif coins == []:
        return float('inf')
    elif coins[0] > amount:
        return change(amount, coins[1:])
    else:
        loseIt= change(amount, coins[1:])
        useIt= change(amount - coins[0], coins)
        if loseIt > useIt:
            return 1+ useIt
        return loseIt
    
                
    
    
    
